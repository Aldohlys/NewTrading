# XOP — Triangle Breakout Long (Call Plan)

**Created:** 2026-06-08 · **Status:** PENDING (awaiting trigger) · **Direction:** Long

Energy-sector long, de-concentrated away from the oil majors (XLE is ~42% XOM+CVX with
large Middle-East upstream exposure). XOP = US-domestic E&P / shale barrels, minimal
foreign-asset risk. Selected over single-name refiners (DK/DINO — rich IV, wide options,
late in their move) and over XLE/XES/CRAK on the June 8 screen.

## Thesis

XOP is coiling in a symmetrical/continuation triangle after the rally to the ~\$190 high.
A break above the descending trendline projects a **retest of the \$188–190 highs**.
/analyze tags it `stage = continuation, ALIGNED`, structural target **\$190.36**
(targets_agreeing 2, fib_confirms TRUE), move only ~23% through the base→target leg →
real headroom (+12% band). Sector rank 4/19 vs SPY.

**Vol backdrop is the edge:** unlike the refiners (IVP mid-80s, rich), XOP is
**IVP 66 / VRP negative / term contango** — IV is mid/cheap with room to *expand*.
This is the one name in the screen where buying premium outright isn't a vega tax, and
where an upside break (energy has positive spot-vol correlation on supply-driven moves)
can add a vega kicker on top of delta.

## ⚠️ Entry is a TRIGGER, not a market order

As of June 8 the breakout has **not** fired — breakout sub-score **0/4**:
RSI 44.9 (<50), up/down vol 0.92, range position 22.7% (near the *low*), volume 0.70×.
The pre-market poke at the trendline is not a confirmed break. Do **not** anticipate.

| | Level | Note |
|---|---|---|
| **Trigger** | cash-session hold **> \$172–173** on volume expansion | clears descending trendline + recent swing |
| **Stop** | **~\$162** (below \$163.36 swing / lower trendline) | structural; mechanical 5% = \$161.08 |
| **Target 1** | **\$180** | prior congestion / first scale |
| **Target 2** | **\$188–190** | retest of highs = analyze \$190.36 |

Fade/no-trade: gaps up then fades back under ~\$169 = failed break, let it re-coil.
Opens 169–172 = still inside triangle, wait.

## Vehicle — Jul17 \$185 calls (2-lot base)

**Expiry = Jul17 (39 DTE), the standard monthly.** Not the weeklies:

- Jul10 weekly had the cheapest IV (31.9% vs 33.2%) but only **119 total call OI** →
  wide spreads. The ~1.3 vol-pt IV saving is a mirage for an outright (you'd give it
  back crossing the bid/ask).
- Jul17 monthly carries **~8,686 call OI (≈70× Jul10)** → the tradeable chain.
- (The original /analyze 53% ATM spread probed Jul24 — a thin 68-OI weekly — wrong
  expiry to judge liquidity.)

**Strike = \$185** (chosen for a \$1–2 handle + leg-in/out within a \$300–400 budget):

| Strike | ~Mid | Δ | IV | OI | ~Contracts in \$350 | Breakeven |
|---|---|---|---|---|---|---|
| 180 | \$2.45 | 0.26 | 33.0 | **39 — avoid (empty)** | 1 | 182.45 |
| 182 | ~\$2.10 | 0.22 | ~33.0 | 1,416 (deepest OTM) | 1–2 | ~184.1 |
| **185** | **\$1.76** | 0.19 | 33.1 | 879 | **2 (≈\$352)** | 186.76 |
| 190 | \$1.46 | 0.13 | 33.3 | 552 | 2–3 | 191.46 |

Why \$185: true \$1–2 handle, 2 contracts ≈ \$352 with room to scale, 879 OI for clean
legging, breakeven \$186.8 sits inside the \$188–190 retest target. **Don't use the round
\$180** — only 39 OI. Alternative: **\$182** if you want more delta/participation per
contract (deepest OTM OI at 1,416).

Two reasons OTM is *better* not just cheaper here:
1. **No vol penalty** — call skew is flat to \$190 (IV ~33 at 182/185/190 = same as ATM).
2. **Sharpens the vega thesis** — if the break bids the call wing and skew steepens, the
   OTM strikes gain the most IV. 185 is better positioned for the "IV expands on break"
   kicker than 175 was.

## Management

- Sell the **first lot into the move to ~\$180** (T1), ride the rest toward \$188–190.
- **Theta caveat:** \$185 is ~0.19 delta — far-OTM, more theta as % of premium; it pays
  only if XOP actually breaks and runs. If it coils at 178–180 the 185s lag. Manage
  actively; you're selling the pop, not holding to expiry.
- If the break is slow/grindy, the vega kicker is small (mostly delta). If violent/news-
  driven, vega + skew-steepening pay extra.

## Pre-execution checklist

- [ ] Cash-session (post-15:30 CET) hold above **\$172–173** on volume — the trigger.
- [ ] Re-confirm Jul17 \$185 live mid/spread ~20 min after the open (expect the tightest
      quote on the board given 879 OI). All current numbers are **pre-market marks**.
- [ ] Spot was \$167.8 pre-market June 8 (drifted off the +2% poke); re-check at entry.
- [ ] Size: 2× \$185 ≈ \$352, within \$300–400 budget, legging room preserved.

## Data appendix (June 8, pre-market)

**Term structure / call skew (call IV − ATM IV, vol pts):**

| Expiry | DTE | ATM IV | 25Δc IV | skew 25Δ | skew 10Δ |
|---|---|---|---|---|---|
| Jun26 | 18 | 33.3 | 33.4 | +0.2 | +1.7 |
| Jul02 | 24 | 33.5 | 34.2 | +0.7 | +2.3 |
| Jul10 | 32 | 31.9 (cheapest) | 31.6 | −0.3 | −0.3 |
| Jul17 | 39 | 33.2 | 33.1 | −0.1 | +0.3 |
| Jul24 | 46 | 33.7 | 33.8 | +0.1 | +1.0 |
| Aug21 | 74 | 32.6 | 34.0 | +1.4 | — |

No XOP skew history stored in DB (`option_skew_history` holds only 7 unrelated names) —
skew read is cross-sectional, not vs-history.

**Call OI (strikes 155–190):** Jul10 119 · **Jul17 8,686** · Jul24 68 · Aug21 4,716
(but Aug21 is a lopsided 185-strike lump of 4,601 — 170–180 band empty, unusable).

Reports: `Reports/analyze_XOP_20260608.html`; scratch scripts
`Reports/xop_callskew.R`, `Reports/xop_oi.R`.
