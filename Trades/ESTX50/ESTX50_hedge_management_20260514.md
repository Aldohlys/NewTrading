# ESTX50 Hedge Management — 18-SEP-26 5200 P

**Date:** 2026-05-14
**Account:** U1804173
**Position:** ESTX50 18-SEP-26 5200 P, long 1 lot
**Spot:** ESTX50 ≈ 5,900 (5,929 at close)
**Underlying-vs-strike:** 5,200 / 5,900 = **88.1% moneyness** (option 11.9% OTM)
**Days to expiry:** 127 (~4.2 months)

---

## 1. Executive Summary

The 5,200P hedge is bleeding because we bought it at an outlier IV spike (37% own-IV on 26-Mar during the late-March selloff). Vol has since fully reverted to 26%, the index has rallied +6.6%, and the position is down 1,488 EUR (–66% of premium paid).

The right action is **NOT** to sell the wing today at trough vol. The right action is to **hold the 5,200P unchanged and pre-commit to selling the 4,700P wing into a future vol spike** — capturing roughly +950 to +1,250 EUR/lot of extra value vs converting today.

This document lays out the analysis, the four candidate actions evaluated, and the operational trigger plan for the recommended strategy.

---

## 2. Current Position Snapshot

| Field | Value |
|---|---|
| Strike | 5,200 |
| Right | Put |
| Expiry | 2026-09-18 |
| Lots | 1 |
| Multiplier | 10 EUR / index point |
| Avg cost | 224.13 EUR/share (paid 2,241 EUR total) |
| Mark (14-May close) | 75.4 EUR/share (753 EUR) |
| **unPnL** | **–1,488 EUR** |
| Delta | –0.184 |
| Gamma | 0.000322 |
| Vega | 9.27 EUR per IV point |
| Theta | –0.79 EUR/share/day (≈ –8 CHF/day) |
| Own-IV (CSV historical) | 26.1% |
| Underlying iv30 (U1804173) | 24.5% |

---

## 3. Why It Bled — Decomposition (26-Mar entry → 14-May)

| Driver | Move | Avg Greek | P&L (EUR/share) |
|---|---|---|---|
| **Vega** (own-IV) | 37.1% → 26.1% = **–11.0 vol pts** | ~11 | **–121** |
| **Delta** | spot 5,561 → 5,929 = **+368 pts** | –0.24 | **–88** |
| **Theta** | 49 days | –0.85 | **–42** |
| Gamma + 2nd-order offset | (positive on rally) | — | **+91** |
| **Total** | | | **–160 EUR/share** ✓ |

**Key finding:** Vega is the dominant driver (≈75% of the gross loss before second-order offsets), not delta or theta. The 5,200P specifically was caught in a put-skew IV spike on entry day (only 23-Mar / 27-Mar had higher IV in the whole dataset since Aug 2025).

**Important methodological note:** the `U1804173.IV` column tracks the underlying's ATM iv30 (24.5% today), NOT the per-option implied vol (26.1% today). The DB column understates vega P&L for OTM strikes. For vol decomposition of held options, use IBKR historical option CSV exports.

---

## 4. Why It Continues to Bleed Daily

A –18 delta, 9-vega put on a calm or rallying tape will print expected daily P&L per the following table:

| Scenario | Expected daily P&L |
|---|---|
| Spot flat, IV flat | –8 to –10 CHF (pure theta) |
| Spot +0.5% (~+30 pts), IV flat | –50 to –60 CHF |
| Spot +1%, IV flat | –100 to –115 CHF |
| Spot flat, IV –1 vol pt | –85 CHF |
| Spot +0.5% AND IV –0.5 pt | **–100 CHF** ← today's print |

A –100 CHF day on ESTX50 rallying ~0.5% with IV slipping ~0.5 pt is the **mathematically expected output** of this position. It is not malfunctioning.

**Bounded downside from here:** mark value 753 EUR/lot. Maximum additional loss to expiry is 753 EUR if ESTX50 stays above 5,200 at 18-Sep-26. **The painful part of the trade is now behind us.**

---

## 5. The Wing-Sale Asymmetry — Why Timing Matters

Selling the 4,700P (or 4,500P) wing converts the naked long into a bear put spread. The premium collected on the wing depends entirely on the vol regime at the moment of sale:

| Regime | 4,700 P own-IV | Approx mid | Cash collected per lot |
|---|---|---|---|
| **Today (calm)** | ~28-29% | ~45 EUR/share | **450 EUR** |
| Moderate stress (–5% drop) | ~32-34% | ~70-90 EUR | 700-900 EUR |
| **Sharp stress (–10% drop)** | ~38-42% | ~140-170 EUR | **1,400-1,700 EUR** |
| Crash (–15% drop) | ~45-55% | ~220-280 EUR | 2,200-2,800 EUR |

The 4,700 wing is worth **3-4× more in a vol spike** than today. Selling it today monetizes the optionality at its weakest point.

---

## 6. Strategic Options Evaluated

| Option | Action | Cash today | Daily theta | –10% drop payout | –20% drop payout | Caps protection? |
|---|---|---|---|---|---|---|
| **A** | Hold 5,200P unchanged | 0 | ~8 CHF | +650-950 EUR | ~+3,500 EUR | No |
| **B** | Convert today: sell 4,700P at 45 EUR | +450 in | ~4 CHF | +650-950 EUR | +5,000 EUR (capped) | Yes, at 4,700 |
| **C** | Layer fresh 5,300/4,700 spread on top | –1,100 out | ~12 CHF combined | ~+2,200 EUR | ~+9,500 EUR | Partial |
| **D** | Replace 5,200P with fresh 5,300/4,700 | –350 out | ~4 CHF | +1,300-1,700 EUR | +5,000 EUR (capped) | Yes, at 4,700 |
| **E (RECOMMENDED)** | Hold today, wing-sale into vol spike | 0 | ~8 CHF | trigger-dependent (see §7) | up to +4,200 EUR | Conditionally |

---

## 7. Recommended Strategy: Wait-and-Convert (Option E)

### Rationale

1. **Existing 5,200P is long vega at trough vol** — we want to preserve, not unwind, this position.
2. **Wing-sale value is path-dependent** — selling at IV 38-42% nets 3-4× more cash than selling at IV 28%.
3. **Realized loss is psychological, not economic** — the 753 EUR remaining mark is the true forward-looking position; the 1,488 EUR is sunk cost.
4. **GOnet portfolio +6% YTD** can comfortably fund the carrying cost (~8 CHF/day theta) over the next ~30-60 days while waiting for a trigger.

### The Default State

- **Hold 5,200P unchanged.** Accept ~8 CHF/day theta + delta sensitivity on rallies as the cost of preserving long-vol convexity.
- **Maximum further loss:** 753 EUR/lot if ESTX50 ≥ 5,200 at expiry.
- **Trigger monitoring:** track ESTX50 spot AND 4,700P own-IV (or 4,500P own-IV) daily.

### Pre-Committed Trigger Plan

The discipline challenge with this strategy is real — in the moment of an actual selloff, the temptation to either freeze (wanting full convexity) or sell too early (at the first vol pop, before the real spike) is high. Trigger rules need to be **pre-defined and staged as TWS limit orders** so they execute mechanically.

#### Trigger 1 — Moderate stress (PRIMARY)

- **Condition:** ESTX50 ≤ 5,430 (–8% from current 5,900) **AND** 4,700P own-IV ≥ 35%
- **Action:** Sell 1 lot ESTX50 18-SEP-26 4,700 P at limit ≥ 100 EUR
- **Position outcome:** 5,200 / 4,700 bear put spread
- **Effective cost basis:** 2,241 paid – 1,000 collected = **1,241 EUR/lot**
- **Max gain (ESTX50 ≤ 4,700 at expiry):** 5,000 – 1,241 = **+3,759 EUR/lot**
- **Max additional loss (above 5,200):** capped at –1,241 EUR/lot (vs current –1,488 unPnL)

#### Trigger 2 — Sharp stress (SECONDARY)

- **Condition:** ESTX50 ≤ 5,150 (–12.7% from current 5,900) **AND** 4,500P own-IV ≥ 40%
- **Action:** Sell 1 lot ESTX50 18-SEP-26 **4,500** P at limit ≥ 200 EUR (further-OTM wing preserves more downside convexity)
- **Position outcome:** 5,200 / 4,500 bear put spread
- **Effective cost basis:** 2,241 paid – 2,000 collected = **241 EUR/lot**
- **Max gain (ESTX50 ≤ 4,500 at expiry):** 7,000 – 241 = **+6,759 EUR/lot**
- **Max additional loss (above 5,200):** capped at –241 EUR/lot

**Important:** Trigger 1 and Trigger 2 are mutually exclusive. If Trigger 1 fires, the position becomes 5,200/4,700 and Trigger 2 is cancelled. If the market skips Trigger 1 (gaps past it), Trigger 2 captures a richer wing at the deeper level.

#### Trigger 3 — Time-decay fallback (TERTIARY)

- **Condition:** 60 days remaining (≈ 14-Jul-26) **AND** no other trigger has fired **AND** 4,700P mid ≥ 30 EUR
- **Action:** Re-evaluate. By this point time decay accelerates and waiting becomes lower-EV. Consider selling 4,700P at whatever vol prevails to recover some premium, or close the entire position.
- **Rationale:** below 60 DTE the wing premium decays faster and the wait-and-convert strategy loses its edge.

### What can go wrong

1. **No drop occurs.** Full bleed continues. Loss at expiry up to 753 EUR/lot. *Acceptable — already absorbed.*
2. **Slow grind down (–5%, modest vol move).** Triggers don't fire. Long put gains some but bleeds time. Trigger 3 fallback captures whatever residual wing value remains.
3. **Sharp drop with insufficient vol spike.** Trigger condition not met (IV < threshold). Re-evaluate trigger thresholds manually. May choose to execute at modified levels.
4. **Discipline failure.** Trigger fires but user doesn't pull the lever. *Mitigation: stage the conditional orders in TWS today, so they execute mechanically.*

---

## 8. Daily Monitoring Plan

| Item | Source | Threshold |
|---|---|---|
| ESTX50 spot | TWS live | Alert at 5,500 / 5,430 / 5,200 / 5,150 |
| 5,200P own-IV | TWS option chain | Alert at ≥30%, ≥35% |
| 4,700P own-IV | TWS option chain | Alert at ≥35%, ≥40% |
| 4,500P own-IV | TWS option chain | Alert at ≥40%, ≥45% |
| 4,700P mid | TWS | Alert at ≥100, ≥150 EUR |
| 4,500P mid | TWS | Alert at ≥200, ≥250 EUR |
| VSTOXX | TWS | Alert at ≥25, ≥30 |

Set TWS alerts on these levels tonight so notification fires before the trigger conditions are actually met (gives time to verify limit orders are staged correctly).

---

## 9. Execution Checklist (Tomorrow Morning)

- [ ] Verify ESTX50 spot and current 5,200P / 4,700P / 4,500P quotes match the assumptions above. If significantly different, recompute.
- [ ] Confirm the wait-and-convert strategy still fits portfolio risk (no major change in GOnet exposure since this report was written).
- [ ] In TWS, set the alert levels in §8.
- [ ] Stage Trigger 1 conditional order: SELL 1 ESTX50 SEP26 4,700 P @ limit 100 EUR, condition = ESTX50 ≤ 5,430 (use TWS conditional order builder; note CME-style trigger limitations may apply on EUREX — verify mechanics).
- [ ] Stage Trigger 2 conditional order: SELL 1 ESTX50 SEP26 4,500 P @ limit 200 EUR, condition = ESTX50 ≤ 5,150.
- [ ] Add Trigger 3 calendar reminder: 14-Jul-26 re-evaluation.
- [ ] Update Trades DB with the trigger plan in Remarques on the 5,200P entry for traceability.

---

## 10. Appendix: Data Sources

- Position snapshot: `U1804173` table in `mydb.db`, row dated 2026-05-14 19:39 UTC
- Historical option data: `historical_ESTX50_5200Put_20260918_2026-05-14.csv` (MIDPOINT) and `historical_ESTX50_5200Put_20260918_2026-05-14 (1).csv` (TRADES), IBKR EUREX, hourly bars Aug 2025 - May 2026
- Entry trade: Trades table, TradeNr 706, opened 26-Mar-26 at 224.0 EUR/share, Strategy = LTO
- IV source for decomposition: option own-IV from CSV (not U1804173.IV — see §3 methodological note)

### Key historical reference points (5,200P MIDPOINT close)

| Date | Mid (EUR) | Own-IV | DTE | Comment |
|---|---|---|---|---|
| 18-Feb-26 | 93.1 | 23.0% | 212 | Late-Feb IV trough |
| 02-Mar-26 | 114.3 | 25.4% | 200 | Early-March benchmark |
| 23-Mar-26 | 236.5 | 41.5% | 179 | Peak IV (skew spike) |
| **26-Mar-26** | **235.8** | **37.1%** | **176** | **Our entry** |
| 27-Mar-26 | 256.5 | 38.8% | 175 | Day after entry |
| 01-Apr-26 | 170.3 | 32.2% | 170 | First IV mean-reversion |
| 15-Apr-26 | 93.7 | 26.0% | 156 | Full reversion |
| 12-May-26 | 95.6 | 28.3% | 129 | Recent vol uptick |
| **14-May-26** | **75.2** | **26.1%** | **127** | **Now** |

---

*Document prepared 2026-05-14 evening; review and execute 2026-05-15 morning.*
