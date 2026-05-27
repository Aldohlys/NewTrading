# XOP long — analyze run + vol-structure verification

**Date:** 2026-05-27
**Direction probed:** long
**Spot:** \$165.01 (intraday, EOD ~\$166.10)
**Verdict from /analyze:** SKIP at phase B (price < MA50, MISMATCH for long)

This document captures the full run, the bug it surfaced in the OI-cap logic, the patch I shipped, and the wider vol-structure read on whether opening a long-premium XOP trade today makes sense.

---

## 1. /analyze XOP long — phase results

| Phase | Result | Key reading |
|---|---|---|
| A — Option liquidity | INFO | 16 expiries · 5 tradeable in 14-90 DTE |
| B — Trend & sector RS | **SKIP** | stage=none · MISMATCH (price \$166.10 < MA50 \$172.81) · sector rank 7/19 |
| C — Cheap + Vol Funnel | **SKIP** | cheap_score 2-3/9 · neutral/short side |
| D — Setup / Chain / R:R | **SKIP** | targets_agreeing=2 · R:R 0.20 · PRICED OUT |
| E — Classification | **SKIP** | phase_of_drop=B |

Setup 3/6 (S2 MA50 slope ✓, S5 squeeze ✓, S6 vol decline ✓; S1, S4 fail). Breakout 0/4. Sector rank 7/19 just inside the long cutoff (≤10).

---

## 2. Bug surfaced — OI cap was direction-blind

### Original behavior

The pipeline pulled `oi_cap_call = \$135` for a long XOP trade with spot \$166. That implied the \$135 strike was "resistance" — except \$135 is **18.7% below spot**, i.e. deep ITM call OI, which carries no dealer-hedging / pin dynamic. The "lower of structural target and OI cap" rule then pulled `effective_target = \$135` below entry, producing R:R = -0.97 and a meaningless PRICED OUT verdict.

### Root cause

`.summarize_oi()` in `RStudies/reports/shared/live_sources.R` (line 455-475) used `which.max(calls$open_interest)` across the full ±25% band with no OTM filter. For XOP:

- Strike \$135 C: 300 OI (deep ITM, stock-replacement)
- Strike \$163 C: 179 OI (ATM)
- Strike \$160 C: 166 OI (ATM)
- Highest OTM call OI: \$170 with ~100-179 OI, depending on snapshot
- Strike \$185 C: 13 OI — almost no OTM positioning at all

### Fix shipped

1. **OTM filter** — calls restricted to `strike > spot`, puts to `strike < spot`. Deep-ITM call OI (stock-replacement / covered-call cover) no longer treated as resistance. Mirror for puts.
2. **Thin-chain bypass** — if max OTM OI on a side falls below `thin_oi_threshold` (default 100), that side's cap is set to NA. Caller already falls back to the structural target when cap is NA.
3. **chain_state = "thin"** when both sides bypass.
4. **Concentration metric** (top-3 / total) now computed over the OTM portion only, not mixing in deep-ITM LEAP/stock-replacement positions.
5. Threshold is now config-driven: `default.analyze.thin_oi_threshold` in `RStudies/config.yml`.

### Post-fix results

| Field | Before | After |
|---|---|---|
| oi_cap_call | \$135 (ITM) | \$170 (OTM) |
| oi_cap_put | \$130 | \$130 |
| effective_target | \$135 | \$170 |
| R:R | -0.97 | 0.20 |

The post-fix \$170 cap is still only \$3.90 above spot — that's why R:R remains low. But it's now mechanically *correct* low (real OTM call wall) rather than nonsensical (ITM longs being treated as resistance).

---

## 3. XOP price action — sharp leg down

Daily closes (last 10 sessions):

| Date | Close | Daily % | Volume |
|---|---|---|---|
| 05-15 | \$174.13 | +2.90% | 3.16M |
| 05-18 | \$176.21 | +1.19% | 3.46M |
| **05-19** | **\$178.56** | +1.33% | 2.18M | ← peak |
| 05-20 | \$174.73 | -2.14% | 6.25M |
| 05-21 | \$170.65 | -2.34% | 5.52M |
| 05-22 | \$171.95 | +0.76% | 2.50M |
| 05-26 | \$166.10 | -3.40% | 3.57M |
| 05-27 | \$165.01 | -0.66% | 1.80M (intraday) |

- **5d return: -7.59%**
- 10d return: -2.79%
- 20d return: -3.87%

Sharp -7.6% leg over 6 sessions from \$178.56 peak. Today (05-27) is decelerating (-0.66% on lower volume vs -3.4%, -2.3%, -2.1% on the down days). Possible exhaustion candle forming, but no confirmation yet.

---

## 4. Vol structure — IVP rich, but VRP "cheap" is a window artifact

### Headline numbers (live IBKR, 2026-05-27)

- IV30: 33.55% (slightly off yesterday's 35.1%)
- 1y IVP: **78.4%** — rich, not extreme
- HV30 (IBKR): 35.4% (as of 2026-05-26)
- VRP_log per analyze report: -3.0 vol-points

### The window-effect trap

IBKR's HV30 dropped sharply over the past 2 weeks — but not because realized vol fell:

```
Date        IV30%   HV30%    VRP(IV-HV)
2026-05-11   33.4    45.5    -12.1 vp   ← HV peak
2026-05-13   32.8    44.5    -11.7 vp
2026-05-18   33.5    42.0     -8.5 vp
2026-05-19   34.1    42.1     -8.0 vp
2026-05-20   34.9    35.0     -0.1 vp   ← HV crashed -7vp in one session
2026-05-21   34.5    35.2     -0.7 vp
2026-05-26   35.1    35.4     -0.3 vp
2026-05-27   33.55   n/a       n/a
```

The May 19→May 20 step-down of -7vp in one session is the smoking gun for a **rolling-window artifact**: a large daily move from ~30 sessions earlier dropped out of the trailing window. HV30 didn't fall because XOP got quieter — it fell because the data point being subtracted was bigger than the data point being added.

### Forward path of realized

Rolling RV on yfinance closes (annualized, log returns):

```
RV(20d): 37.1%    ← contains the 5/6 -6.24% gap
RV(10d): 31.2%
RV(5d):  26.1%    ← misleading low; today's drop not yet included
```

The current sell-off is producing 2-3% daily moves. Over the next 5-10 sessions these get absorbed into the HV30 window and **push HV30 back up**, not down. The "VRP = -3vp, cheap" signal the analyze report is showing is fragile — it's measured against a HV30 reading that's mechanically depressed right now.

### Practical read

- **IV is sticky at 33-35%** — has not moved much for 6 weeks despite HV30's swings from 45→35.
- **IVP 78% is real richness** — premium is expensive to buy.
- **VRP cheap is partly artifact** — don't size up on it. If XOP stabilizes, IV may compress to 28-30% (early-April level), which is vega P&L hit on long premium.
- **If XOP keeps falling**, IV expands further before topping; long calls bleed delta while gaining vega — directional thesis fights price.

---

## 5. XOP option chain — too thin for OI-cap analysis

Total OI in ±25% band of spot: ~2,000 contracts across **all** strikes. Single-strike max OI is 300 (\$135 C deep ITM). Highest OTM call: \$170 with ~100 OI. Highest OTM put: \$130 with 166 OI.

For comparison, an SPY/QQQ option chain has 5-figure single-strike OI routinely. XOP is closer to a single-name midcap in option depth than to a major ETF.

**Implication:** even with the OTM filter fix, OI caps on XOP carry low information. The "support/resistance from dealer positioning" signal isn't really there. Phase D's `effective_target` should default to the structural target for this kind of thin chain, not the OI cap — which is exactly what the new thin-chain bypass does.

---

## 6. Bottom line for long XOP today

Setup breaks at multiple layers:

1. **Trend layer** — price below MA50 with negative breakout score. MISMATCH for long.
2. **Vol layer** — IVP 78%; VRP-cheap signal is window-fragile; vega risk asymmetric (IV crush on stabilization vs further IV expansion on continued downside).
3. **Chain layer** — too thin to extract resistance from. Structural target \$190 is reachable in theory but needs a 15%+ rally against current momentum.
4. **R:R layer** — even using the more-honest \$170 cap, R:R = 0.20, below the 0.5 calibrated floor.

This is not a buy-the-dip-and-collect-vol-cheap setup. The cheap-vol signal is partly noise; the directional thesis fights price; the chain provides no structural support. SKIP is correct.

---

## 7. Code changes shipped this session

| File | Change |
|---|---|
| `RStudies/reports/shared/live_sources.R` | `.summarize_oi()` OTM filter + thin-chain bypass + concentration over OTM only |
| `RStudies/reports/shared/live_sources.R` | `resolve_chain_oi()` accepts `thin_oi_threshold` param |
| `RStudies/reports/analyze/structures.R` | reads `config$thin_oi_threshold`, plumbs into resolver |
| `RStudies/config.yml` | new `default.analyze.thin_oi_threshold: 100` |

## 8. Follow-up ideas (not shipped)

- Surface OTM-side OI counts (n_otm_calls, n_otm_puts, max_otm_call_oi, max_otm_put_oi) in the Chain section of the HTML report so the user immediately sees when a chain is thin.
- Flag in report when `effective_target` is < N% above spot (long) / below spot (short) — the user shouldn't have to derive R:R-too-low diagnosis manually.
- Surface trailing RV5/RV10/RV20 alongside HV30 in Phase C.2 to expose window-effect artifacts in VRP — the current single-row VRP is fragile when realized vol is in transition.

## Verification scripts (in `scripts/`)

- `pull_xop_oi.py` — live IBKR chain OI for one expiry, sorted desc
- `check_xop_pa_iv.py` — yfinance price action + rolling RV
- `check_xop_iv_history.py` — IBKR IV30 + HV30 daily history, 1y IVP
