# ATR → Multi-Day Move Heuristic — Empirical Validation

*Date: 2026-06-08 · Method: 5-year daily OHLC, 12 tickers across the ATR spectrum · Pure realized-price test (no IV)*

## Purpose

The BOT checklist's **"Sufficient beta"** filter asserts that low-beta defensives (PG/PEP/KO type) "produce breakouts that abort before reaching the pay-for-entry threshold." That was a qualitative claim with a proxy (ATR14/price > 1.5%). This report tests the underlying rule of thumb empirically and converts it into usable multiples:

> **Working heuristic under test:** a *strong* 10-day move ≈ 3–4 × daily ATR%, derived from √T scaling.

The result generalizes: **given any ticker's ATR% (its beta proxy), we can estimate its typical and strong N-day move, and the frequency with which it produces a move large enough to pay for a long-option entry.**

## The theory being tested

Price dispersion follows a random walk, so it scales with the **square root of time**:

- N-day move ≈ daily move × √N. For N = 10, √10 = **3.16**.
- ATR is *true range* (incl. gaps), larger than close-to-close σ: ATR ≈ 1.3–1.6 × daily σ.
- For a normal distribution, |move| has median ≈ 0.67σ, p90 ≈ 1.65σ.

Combining these (ATR ≈ 1.4σ) gives the **predicted multiples** of 10-day |move| to ATR%:

| Statistic | Predicted multiple (× ATR%) |
|---|---|
| median | 1.52 |
| p75 | 2.60 |
| p90 ("strong") | 3.72 |
| 1.5σ directional | 3.39 |

## Results (5y daily, horizon = 10 sessions)

| Ticker | Beta | ATR% | ATR/σ | σ₁₀/σ₁ | median 10d | k_med | p90 10d | k_p90 | P(≥6%/10d) |
|---|---|---|---|---|---|---|---|---|---|
| XLV | mid | 1.23 | 1.32 | 2.97 | 1.8% | 1.43 | 4.7% | 3.85 | 3% |
| KO | low | 1.41 | 1.39 | 3.05 | 2.0% | 1.43 | 5.1% | 3.61 | 6% |
| PG | low | 1.47 | 1.31 | 2.98 | 2.2% | 1.51 | 5.5% | 3.74 | 7% |
| JNJ | low | 1.53 | 1.44 | 3.10 | 2.3% | 1.49 | 5.5% | 3.63 | 8% |
| PEP | low | 1.60 | 1.38 | 2.99 | 2.3% | 1.46 | 5.5% | 3.43 | 7% |
| ABBV | mid | 1.97 | 1.36 | 3.23 | 2.8% | 1.44 | 7.6% | 3.86 | 18% |
| MRK | mid | 2.01 | 1.34 | 3.17 | 3.0% | 1.48 | 8.2% | 4.06 | 19% |
| UNH | mid | 2.22 | 1.07 | 3.35 | 3.2% | 1.44 | 10.5% | 4.74 | 25% |
| TMO | mid | 2.34 | 1.37 | 3.03 | 3.1% | 1.32 | 8.8% | 3.76 | 22% |
| NVDA | high | 3.84 | 1.19 | 3.03 | 6.4% | 1.66 | 17.0% | 4.42 | 53% |
| AMD | high | 4.28 | 1.23 | 3.19 | 7.3% | 1.72 | 12.7%→18.4% | 4.30 | 57% |
| TSLA | high | 4.56 | 1.23 | 3.26 | 7.4% | 1.63 | 20.9% | 4.59 | 58% |

**Legend:** `k_med` = median 10d |move| ÷ ATR%; `k_p90` = p90 10d |move| ÷ ATR%; `σ₁₀/σ₁` = realized 10-day vs 1-day sigma; `P(≥6%/10d)` = fraction of 10-day windows with a ≥6% move (proxy for "an OTM call can ~triple" = pay-for-entry).

### Theory vs. tape — all three pillars hold

| Quantity | Theory | Measured (pooled) | Verdict |
|---|---|---|---|
| √T scaling (σ₁₀/σ₁) | 3.16 | **3.11** | Confirmed — random walk is the right model |
| ATR / daily σ | 1.3–1.6 | **1.30** | Confirmed (low end; 1.6 ceiling slightly high) |
| median 10d move / ATR% | 1.52 | **1.50** | Exact |
| strong (p90) 10d move / ATR% | 3.72 | **4.00** | Confirmed, slightly *above* theory = fat tails |

## Headline finding (and a correction)

The shorthand "**10-day move ≈ 3 × ATR%**" overstates the *typical* case by ~2×:

- **Typical (median) 10-day move ≈ 1.5 × ATR%.**
- **Strong (p90) 10-day move ≈ 4 × ATR%** (a hair above normal theory, due to fat tails).
- The "√10 ≈ 3×" shortcut describes roughly an **85th-percentile move** — the *good* case, not the base case.

So the specific claim "**1% ATR → a strong 10-day move of 3–4%**" is **validated** (low-beta bucket p90 multiple ≈ 3.6). What was loose was implying 3× is the average; the average is half that.

### General multiples (any ticker, any horizon)

| Move type | Multiple of ATR% (10d) | General form (N days) |
|---|---|---|
| Typical (median) | **1.5 ×** | 0.48 × ATR% × √N |
| Strong (p90) | **4 ×** | 1.25 × ATR% × √N |

(For N = 10: 0.48 × √10 = 1.52; 1.25 × √10 = 3.95.)

## The decision-relevant result — pay-for-entry frequency

The right-most column quantifies *why* low-beta names fail as long-option vehicles. P(≥6% move in 10 days) — the proxy for an OTM call tripling:

| ATR% bucket | Examples | P(payable move) |
|---|---|---|
| ~1.5% (low-beta defensive) | PG, KO, JNJ, PEP | **6–8%** |
| ~2.0–2.3% (mid) | ABBV, MRK, TMO, UNH | **18–25%** |
| ~4% (high-beta) | NVDA, AMD, TSLA | **53–58%** |

A ~**7× difference** in payable-move frequency between the low- and high-beta ends. A 1.5%-ATR name delivers a monetizable move ~1 window in 14 — you pay theta the other ~93% of the time, which is why PG/PEP go ~0% WR buying breakout calls. **The convexity edge lives almost entirely in the right half of the ATR distribution.**

## Sector calibration of C

C is normalized by each name's own ATR%, so the large cross-sector *level* differences (tech's daily range is ~2× staples') live in the ATR% **input**, not in C. C captures only the distribution **shape**, which is far more universal. Tested across 5 sectors (8–10 names each, 5y daily):

| Sector | ATR% (level) | C_med | C_p90 (strong) |
|---|---|---|---|
| Tech/Semi | 3.09 | 0.52 | 1.35 |
| Energy | 2.69 | 0.47 | 1.22 |
| Financials | 2.29 | 0.52 | 1.33 |
| Healthcare | 2.13 | 0.46 | 1.25 |
| Staples | 1.59 | 0.46 | 1.18 |

- **C_med spread is only ~±6%** (0.46–0.52) — the default 0.48 is accurate to ~10% in any sector.
- **C_p90 (the tail) is more sector-dependent** (1.18–1.35): Tech/Financials carry fatter tails. A healthcare-calibrated 1.25 understates a tech strong-move by ~10%.
- **The driver of C is trend / gap / event-density, not beta.** Financials cluster with Tech (C_med 0.52, C_p90 1.33) despite moderate ATR% — they trend and gap on rate/credit surprises. Staples chop within their range (more mean-reverting) → lower C. Tech and financials accumulate more displacement per unit of daily range.

**Per-sector coefficients to use:**

```
                  C_med   C_p90 (strong)
Tech / Financials  0.52      1.35
Healthcare/Energy  0.47      1.23
Staples            0.46      1.18
```

Default (0.48 / 1.25) is fine to ~10%; nudge up for Tech/Financials, especially the tail coefficient.

## Application

For any ticker:
1. Compute **ATR14 / price** (the beta proxy).
2. **Typical 10-day move ≈ 1.5 × ATR%; strong move ≈ 4 × ATR%.** Scale to other horizons with √N.
3. Read the **payable-frequency bucket** to judge vehicle fit:
   - **Low ATR (≲1.7%):** long OTM calls structurally lose. Use **shares** (linear, no theta hurdle) or **SELL premium** (profit from the name *not* moving).
   - **Mid ATR (~2%):** long calls viable but the payable move is still a minority outcome — favor spreads / pay-for-entry discipline.
   - **High ATR (≳3.5%):** convexity pays — long OTM calls are in their sweet spot.

## Caveats

- **Unconditional** — these are *all* 10-day windows, not windows following a breakout signal. Conditioning on a real BOT entry (positive drift) raises every payable number; the *cross-sectional ordering* (the point) is signal-independent, and the multiples k_med/k_p90 are vol properties, largely signal-independent.
- **"6% = payable"** is a rough stand-in for the true strike/DTE/IV-dependent triple.
- **Overlapping windows** — percentiles are robust but effective N < raw N.
- **UNH ATR/σ = 1.07** is distorted by gap risk during the 2025 collapse (gaps inflate close-to-close σ relative to range).

## Framework backtest vs realized BOT trades

The forward study above (Section "Results") measures *move capacity* unconditionally. This section tests whether that capacity actually showed up in the **realized BOT trade log** — do winners skew rich-ATR? Script: `Strategies/Breakouts/bot_atr_validation.py` (104 closed BOT trades from `mydb.db`, ATR% measured **at each trade's entry date**).

> **Data-handling note (bug fixed mid-analysis):** the first pass keyed the option-vs-stock flag off the `Right` DB column, which is null on 182 of 339 BOT legs (older trades). That misclassified every pre-2025 option trade as "stock" — including both AAPL OTM-option winners. Corrected by parsing the vehicle from the `Instrument` string (last token `C`/`P`). 99 of 104 trades are options. All figures below are post-fix.

### Winners vs losers

| (options, n=99) | n | median ATR% | avg PnL |
|---|---|---|---|
| Winners | 42 | **2.94** | +\$511 |
| Losers | 57 | **2.33** | −\$191 |

Winners carry higher ATR than losers (2.94 vs 2.33) — but the PnL↔ATR% correlation is weak (Pearson 0.17, Spearman 0.07).

### By ATR bucket (U-shaped, not monotonic)

| ATR bucket | n | win rate | avg PnL | total PnL |
|---|---|---|---|---|
| low <1.7% | 17 | 47% | +\$241 | +\$4,098 |
| **mid 1.7–3%** | 48 | **31%** | −\$11 | **−\$517** |
| high ≥3% | 39 | 54% | +\$207 | **+\$8,056** |

### Findings

1. **Aggregate support holds:** rich-ATR wins more often and bigger; the high bucket carries +\$8,056 and 10 of the 20 biggest wins.
2. **Low-ATR is NOT a hard reject:** low-ATR option trades won 47% (+\$4,098), including the 2nd/3rd biggest wins ever — AAPL OTM call +\$1,346 and AAPL OTM put +\$1,277 at ~1.6% ATR — plus JNJ/V/GLD. This refutes the strong "low-ATR can't pay for entry with OTM options" claim.
3. **Reconciliation with the 6–8% payable stat:** that figure is *unconditional*; these trades were entered *on a breakout signal* (positive drift) with skilled near-expiry strike selection, which lifts the hit rate far above the unconditional base rate. The two studies measure different things; they do not conflict.
4. **ATR% conflates two "low" types:** genuinely quiet names (PG/KO/PEP — never traded, correctly avoided) vs catalyst-mobile megacaps (AAPL — low range-average but episodic 5–7% movers). The filter must not reject the latter.
5. **The real money-pit is the MID bucket (1.7–3%, ~32% WR, net negative)** — marginal-beta breakouts that abort.

### Verdict

ATR is validated as a **prior and sizing input** (rich ATR → higher base rate of payable moves, larger aggregate wins), **not as a hard gate or a trade-selection edge.** Low-ATR names with a genuine signal and good strikes can and did pay for entry. The actionable surprise is the mid-ATR graveyard. The checklist "Sufficient beta" filter was revised accordingly (soft prior + megacap-catalyst exception). Caveats: n=104 (39 in earlier subsets), polluted strategy label (mean-reversion/futures trades tagged BOT), selection bias (the worst quiet names were never entered — a *used* filter can't show the disasters it prevented).

## Reproducibility

- Realized-trade backtest: `Strategies/Breakouts/bot_atr_validation.py`
- Validation script: `Strategies/Breakouts/atr_move_validation.py`
- XLV component breakout screen: `Strategies/Breakouts/xlv_screen.py`
- Data: yfinance, 5y daily, auto-adjusted. Re-run to refresh.
- Canonical BOT reference: `Strategies/Breakouts/bot_strategy_checklist.md` ("Sufficient beta" filter).
