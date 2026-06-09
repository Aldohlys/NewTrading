# Routine App — TODO Bug Fixes

## Root Cause: JPY CASH `unPnL` = 101,447,385 in DB

The `U1804173` table stores a JPY CASH row with `unPnL = 101,447,385 CHF` — a completely wrong value that cascades into 3 visible bugs.

### How the 101M was computed

In `Tdata/R/cash.R` → `create_cash_portfolio_row()` (line 261):

```r
unrealized_pnl <- (exchange_rate - trade_cost_basis) * balance
```

- `exchange_rate = convert_to_base_date(1, "JPY", date)` ≈ **0.00496 CHF/JPY**
- `trade_cost_basis` from Trades DB `Prix` field = **201.665 JPY/CHF** (Trade 687: sold 1,300 CHF for JPY)
- `balance = -503,061 JPY`

**Unit mismatch**: `exchange_rate` is in CHF/JPY but `Prix` is in JPY/CHF — they are reciprocals. The subtraction `(0.005 - 201.665)` is meaningless, producing:

```
(0.005 - 201.665) × (-503,061) ≈ +101,447,385
```

### Trade 687 details (the JPY CASH trade)

```
TradeNr=687 | Instrument=CHF | Ssjacent=CASH | Pos=-1300 | Prix=201.665 | Currency=JPY
```

This is: "Sold 1,300 CHF at 201.665 JPY/CHF" — standard IBKR forex convention where Prix is the quote currency per base currency.

### Query mismatch (secondary issue)

`create_cash_portfolio_row("JPY", ...)` queries `WHERE Instrument = 'JPY'` but Trade 687 has `Instrument = 'CHF'`. The query should find nothing, defaulting `trade_cost_basis = exchange_rate` (giving unPnL=0). The 101M in the DB may be from a **previous code version** that queried differently (e.g., `WHERE Currency = 'JPY'`), or a manual override. Either way, the formula has a latent unit mismatch bug.

---

## Bug 1: Unclassified sector shows 101M unrealized PnL (File 6)

**File**: `Tuser/portfolio/logic/portf.R` → `enrich_portfolio_with_sectors()` (lines 42-50)

```r
Sector = case_when(
  symbol == currency & symbol == base_currency ~ "Cash",
  symbol == currency & symbol != base_currency ~ "Forex",
  is.na(Sector) ~ "Unclassified",   # ← CASH positions land here
  TRUE ~ Sector
)
```

**Problem**: CASH rows from `create_cash_portfolio_row` have `symbol = "JPY"` but `currency = "CHF"` (base_currency). Since `symbol ≠ currency`, the first two conditions fail. "JPY" isn't in the Tickers table, so `left_join` gives `Sector = NA` → falls to "Unclassified".

**Fix**: Add a `type == "CASH"` guard before the `is.na(Sector)` fallback:

```r
Sector = case_when(
  symbol == currency & symbol == base_currency ~ "Cash",
  symbol == currency & symbol != base_currency ~ "Forex",
  type == "CASH" ~ "Forex",          # ← NEW: CASH positions are Forex
  is.na(Sector) ~ "Unclassified",
  TRUE ~ Sector
)
```

---

## Bug 2: CHF currency row shows 101M unrealized PnL (File 7)

**File**: `Tuser/portfolio/logic/portf.R` → `aggregate_by_currency()` (lines 208-219)

```r
currency_summary <- portf |>
  group_by(currency) |>          # ← All CASH rows have currency = "CHF"
  summarize(
    mkt_value = sum(mktValue),
    unrealized_pnl = sum(unPnL),   # ← JPY CASH unPnL (101M) lands in CHF bucket
    ...
  )
```

**Problem**: `create_cash_portfolio_row` sets `currency = base_currency` ("CHF") for ALL CASH positions (line 286 of cash.R). So JPY, EUR, USD cash positions all group under CHF.

**Fix option A** (in `aggregate_by_currency`): For CASH rows, group by `symbol` instead of `currency`:

```r
portf <- portf |>
  mutate(grouping_currency = if_else(type == "CASH", symbol, currency))

currency_summary <- portf |>
  group_by(grouping_currency) |>
  ...
```

**Fix option B** (in `create_cash_portfolio_row`): Set `currency = currency` (the foreign currency) instead of `currency = base_currency`. But this changes the meaning of `mktValue` and `unPnL` — they'd need to be in native currency too, which is a bigger refactor.

**Note**: The DB-level query in `account.R` (line 1327-1332) already handles this correctly with a `CASE WHEN type = 'CASH' THEN symbol ELSE currency END` pattern. The R-side aggregation should follow the same logic.

---

## Bug 3: Gainers histogram — JPY bar at ~$120M (screenshot)

**File**: `Tuser/portfolio/logic/portf.R` → `portfolioPnL()` (lines 328-341)

```r
data = mutate(portf,
  unPnL = purrr::pmap_dbl(list(unPnL, currency, orig_date), convert_to_usd_date))
data = data %>% group_by(symbol, currency) %>% summarize(unPnL = sum(unPnL))
```

**Problem**: Same root cause — JPY CASH row has `unPnL = 101M` with `currency = "CHF"`, so `convert_to_usd_date(101447385, "CHF", date)` ≈ $120M USD. This dwarfs all other positions in the chart.

**Fix**: Once the root cause (Bug 0 — wrong unPnL computation) is fixed, this chart will auto-correct. Optionally, `portfolioPnL` could also use `symbol` for CASH grouping, same as Bug 2.

---

## Bug 0 (Root): Fix `create_cash_portfolio_row` unPnL computation

**File**: `Tdata/R/cash.R` → `create_cash_portfolio_row()` (lines 210-294)

### Issues to fix:

1. **Unit mismatch in unPnL formula** (line 261): `exchange_rate` (CHF/JPY) vs `Prix` (JPY/CHF) are in different quoting conventions. The fix depends on the IBKR convention for storing Prix:

   - If Prix is always "quote/base" (JPY per CHF for a CHF/JPY trade): convert to same unit as exchange_rate → `trade_cost_basis = 1 / Prix`
   - Alternatively: compute unPnL as `balance * (exchange_rate - 1/Prix)`

2. **Query doesn't match the trade** (lines 244-247): Trade 687 has `Instrument = "CHF"`, `Currency = "JPY"`, but the query searches `Instrument = 'JPY'`. For a CHF→JPY trade, the cash balance is in JPY, but the Instrument is CHF.

   **Fix**: Query should also search by `Currency`:
   ```sql
   SELECT TradeNr, Prix, Instrument, Currency FROM Trades
   WHERE Account = ? AND (Instrument = ? OR Currency = ?) AND Ssjacent = 'CASH'
     AND Statut != 'Fermé'
   ORDER BY TradeDate DESC LIMIT 1
   ```
   Then determine the quoting direction from which column matched.

3. **`currency = base_currency`** (line 286): All CASH rows get `currency = "CHF"`, which breaks downstream grouping by currency. Consider setting `currency` to the actual foreign currency code and expressing `mktValue`/`unPnL` in that currency.

---

## Summary of files to modify

| Priority | File | Function | Issue |
|----------|------|----------|-------|
| P0 | `Tdata/R/cash.R` | `create_cash_portfolio_row` | Unit mismatch in unPnL formula + wrong query + currency field |
| P1 | `Tuser/portfolio/logic/portf.R` | `enrich_portfolio_with_sectors` | CASH → Unclassified (add `type == "CASH"` guard) |
| P1 | `Tuser/portfolio/logic/portf.R` | `aggregate_by_currency` | CASH groups under CHF (use `symbol` for CASH) |
| P2 | `Tuser/portfolio/logic/portf.R` | `portfolioPnL` | Gainers chart (auto-fixes with P0, but could add CASH grouping) |

## Immediate DB fix

After fixing the code, the stale 101M value in U1804173 needs to be corrected. Either:
- Re-run portfolio snapshot (will overwrite with correct value)
- Or manual SQL: `UPDATE U1804173 SET unPnL = <correct_value> WHERE symbol = 'JPY' AND type = 'CASH' AND date = <latest_date>`
