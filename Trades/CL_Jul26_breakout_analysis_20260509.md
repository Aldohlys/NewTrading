# CL Jul'26 — Breakout Trade (Closed)

**Dates:** Plan 2026-05-09 → Entry 2026-05-11 → Close 2026-05-18 (7 trading days)
**Vehicle:** MCL Jul'26 futures (NYMEX, multiplier \$100/pt)
**Result:** **+\$1,604** (3 lots)
**Status:** Closed — final document

---

## 1. Setup analysis (2026-05-08 / 2026-05-09)

### Term structure (CL Jul'26 across the curve)

- Front (Jun'26): ~\$95
- Dec'26: ~\$70 — **steep \$25 backwardation in 7 months**
- Long-dated (Dec'36): ~\$53 — structural energy-transition discount
- Front contracts \$6-7 below 1w ago; back contracts \$1.5-2 above 1w ago → **curve flattening**

**Read:** prompt premium bleeding off, long-dated firming. **Spot is dislocated, not the curve.** The \$25 front-end drop is a prompt-month spike (geopolitical / supply); long-dated \$53 reflects structural energy-transition discount. ~70% of the bullish narrative was already priced.

### Daily chart (CL Jul'26)

- O 94.00 H 94.52 L 90.25 C 91.78 (2026-05-08), EMA50 = \$85.58
- Pattern: long base → spike → climactic high → corrective bounce on light volume (distribution into rallies)
- Structure-defining level: **\$85 (50 EMA)**. Above = uptrend intact, spike thesis alive. Below = climax done, next \$5-10 is down.

### IV regime (Jul'26 smile)

| Reference | ATM IV (~91 strike) | 95 call IV | Smile slope (79→97) |
|---|---|---|---|
| 2 weeks ago | ~52% | ~55% | +6 pts |
| Today (2026-05-09) | ~63% | ~64.5% | +4 pts (flatter) |

- IV **doubled in 2 weeks** — major-event regime (historical CL ATM IV: 25-50%)
- Positive smile (call skew > put skew) — commodity supply-shock signature
- Past week: put wing bid (86 strike: 58.5% → 62%, **+3.5 pts**), call wing eased (95-97: -1 pt). Fear rotating from "miss the spike" to "miss the rollover"

### Thesis

Another spike possible if no Middle East truce + transport disruption continues. **But:** 63% IV already prices the existing narrative — needs an *incremental* catalyst (Hormuz closure, Saudi facility, new front) for next leg. Without specific catalyst, expected outcome = chop + vol bleed.

### Probability math (10-DTE, σ ≈ 12.5%)

- 1-σ 10-day move = \$91.28 × 0.63 × √(10/252) ≈ **\$11.45 (~12.5%)**
- P(S > \$97 in 10d) ≈ **31%**
- P(S > \$100 in 10d) ≈ **22%**
- 96/97 call spread EV ≈ break-even (positive only with informational edge on catalyst timing)

---

## 2. Vehicle selection

**Critical correction:** CL options multiplier = **1000** (MCL = 100). Initial premium calcs were 10× too low.

Natural technical stop (\$85, 50 EMA) is \$6+ from spot — too far for CL outright futures (\$6,280 risk/contract) and 6× lot cap for the meaningful 95/100 call spread (~\$1,800 risk).

| Vehicle | Risk | Verdict |
|---|---|---|
| CL futures, stop \$85 (50 EMA) | \$6,280 | Way over cap |
| CL 95/100 call spread | ~\$1,800 | 6× lot cap |
| CL 96/97 call spread | \$330 | Fits cap but ~22% mid-life hit-rate |
| **MCL futures, stop \$85** | **\$628** | **Selected — same instrument, 1/10 size, respects technical** |

MCL options ruled out: thin chain, wide bid-ask, harder to leg into spreads at mid.

---

## 3. Original plan (bypassed)

**Staged ladder:** Limit buy 2× MCL @ \$89.50 GTC, stop \$85.
- Entry zone (89-90) below 2026-05-08 low, captures meaningful retest
- Total risk \$900, expected R:R 2.33:1 if filled
- Red-line (chase): \$93.50+ only on breakout with volume

**Outcome:** \$89.50 never traded. Plan re-routed to the **breakout-confirmation branch** after Iran-war catalyst gap on Sunday 2026-05-11.

---

## 4. Live execution

### T0 — Lot 1 entry (2026-05-11, 00:30 CET)
- **Long 1× MCL @ \$94.35** at Sunday-night CME open after ~+3% Iran-war gap
- Catalyst confirmed the breakout branch (incremental event: new geopolitical front)
- Initial: SL **\$91.00** (below the gap), TP **\$100.00**, R:R 1.69:1

### T+1 — Lot 2 add (2026-05-12 morning)
- **+1 lot @ \$96.30** (buy stop at \$96 triggered, 30¢ slippage accepted)
- 2 lots, avg **\$95.325**
- Tightened SL to **\$93.70** across both (avg − \$1.50 ≈ \$295 risk, under \$300/lot cap)
- Working sell limit \$100 on 1 lot, runner on the other

### T+2 — Lot 3 add (2026-05-14)
- Current quote \$97.03; front WTI \$101.48 (crisis-level **\$4+ backwardation**)
- **Buy STP LMT \$99.00 / \$99.20** placed — above \$98 round + recent local high
- **Per-lot stop on Lot 3 at \$97.50** (NOT global stop). Rejected global \$94.87 design that would have forced Lot 3 into 0.73:1 R/R — negative expectancy even at 100% win
- Existing \$93.70 stop on Lots 1+2 unchanged
- TP raised to **\$102 for all 3 lots** (structural prior-resistance target)
- Worst-case system loss: -\$470 (under \$500 cap)
- Lot 3 filled at **\$99.20** (STP LMT cap, on rally through the level)

---

## 5. Monitoring framework (applied throughout)

| Signal | Bullish (hold/add) | Bearish (exit/abort) |
|---|---|---|
| **Term structure** | Front/back spread holding or widening | Front-back re-flattens (back catches up) → supply-shock narrative unwinding |
| **ATM IV** | Holding 60%+ → tail risk still priced | Crushing to 50% → spike thesis dying |
| **15m structure** | Above \$91.50-92.00 shelf (gap floor) | Break of shelf with volume → abort regardless of nominal stop |
| **Front-Jul spread** | JUL participating in rally | JUL lagging while front decays → back won't catch up |

**Invariant:** Below \$91.00 the trade closes unconditionally. The gap defined the move; lose the gap, lose the thesis. No averaging down, no widening the stop. Once Lot 3 added, per-lot stop discipline replaced "average price" thinking.

---

## 6. Close (2026-05-18, Sunday-night CME open)

### Sequence

- Sunday-night re-open: price gapped to **\$104 high**, retraced to **\$102.26**
- **TP \$102 hit:** 2 lots sold at **\$101.95** (5¢ slippage on \$102 limit)
- Runner SL moved to **\$101.95** (tighter than the \$100 alternative — see Lesson 5)
- **Runner stopped at \$101.94** — full position closed

### P&L

| Lot | Entry | Exit | P&L |
|---|---|---|---|
| 1 | \$94.30 | \$101.95 | **+\$765** |
| 2 | \$96.30 | \$101.95 | **+\$565** |
| 3 | \$99.20 | \$101.94 | **+\$274** |
| **Total** | | | **+\$1,604** |

### vs. plan

- Max plan outcome (all 3 at \$102): \$1,640
- **Captured 98% of plan**
- Expected profit range was \$1,000-\$1,500; landed just above

---

## 7. Lessons banked

### 1. Per-lot R/R audit when pyramiding
A global stop sized to cap total system loss forces the latest add (highest cost basis) to absorb the largest dollar loss. If the add's per-lot R/R drops below 1:1, the marginal unit is negative expectancy even at 100% win — system R/R math hides it. Use **per-lot structural stops** on adds, not the global stop.
→ [[feedback-pyramid-per-lot-rr-audit]]

### 2. Verify futures contract month before quoting prices
Front-month CL=F (\$101.48) vs JUL contract MCL (\$97.03) had \$4+ divergence in crisis-level backwardation. Quoting front-month proxy when the user holds back-month produces materially wrong P&L and risk estimates.
→ [[feedback-verify-futures-contract-month]]

### 3. Don't switch frameworks mid-trade
This was a BOT trade (2-4 week structural breakout, target prior resistance \$102). Mid-trade temptation to switch to a macro framework ("Hormuz + no peace = hold for higher") would have broken the discipline that made the trade tractable. Macro is a SEPARATE trade with different horizon/sizing/stop logic — open a new position, don't extend the runner.
→ [[feedback-dont-switch-frameworks-midtrade]]

### 4. Hard to exit winners
Exiting at the structural target felt harder than the math suggested it should. Cognitive asymmetry: losers exit themselves; winners require active choice. The macro narrative was actively offering reasons to extend — exactly when discipline matters most. Pre-commit limit orders at the structural target before price arrives; treat 90% of plan as success.
→ [[feedback-hard-to-exit-winners]]

### 5. Runner SL must sit meaningfully below scale-out level
After scaling 2 lots at \$101.95, the runner SL was placed at the same \$101.95 (only \$0.31 below current \$102.26). Effectively a delayed exit of the whole position at the same price — not a real runner. A runner needs structural room (typically \$1-2 below scale-out). Cost on this trade was minimal (price didn't continue up), but the structural lesson is real: if exit-everything-at-X is the intent, sell-all-at-X is the order.

### 6. STP LMT direction
For a buy stop limit, LMT must be ≥ STP (typically STP + \$0.10-0.20 slippage budget). Reversing fills only on a post-trigger pullback, missing breakout continuation.
→ [[reference-buy-stop-limit-direction]]

---

## 8. TWS reference tools (kept for repeat use)

- **Price term structure (curve plot):** right-click on any CL contract row in Quote Monitor → **Charts** → **Term Structure**. Window title "Futures TS - CL @NYMEX"
- **IV term structure:** same right-click menu → **Charts** → **Implied Volatility Viewer**
- **IV smile/skew at one expiry:** same Viewer with single expiry checkbox selected

Related memory: [[reference-tws-futures-term-structure]], [[reference-cl-options-multiplier]] (CL = 1000, MCL = 100)
