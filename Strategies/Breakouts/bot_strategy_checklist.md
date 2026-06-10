# BOT Strategy — Complete Checklist

## Definition

A **BOT (Breakout)** trade targets the transition from a consolidation phase to a directional move. The consolidation is characterized by contracting price range and declining volume (supply drying up). The breakout is a sharp move above the consolidation range with volume confirmation, followed by a succession of higher highs and higher lows.

**What BOT is NOT:**
- Trend following with pullback entry
- Mean-reversion / bottom fishing
- Event bet (FOMC, earnings, jobs number)
- Parabolic move (already started)
- FOMO entry

---

## Trade-Type Classifier — Breakout vs Mean-Reversion

Both can be long, and both can start near a low — so "price is going up off a low" does **not** classify the trade. They differ in **what you're betting on and where price stops**, which dictates *opposite* stop/target/horizon logic. Misclassifying imports the wrong exit plan — the most common way these trades are mismanaged.

**Core distinction**
- **Breakout (BOT)** = a bet about **structure**: a level gave way and a **new trend started**, so price accelerates **away from the base**. Target is *open-ended* (continuation). You're trading the release of energy.
- **Mean reversion** = a bet about **price**: it's stretched too far from value and snaps **back toward the mean**. Target is *finite and overhead* (the MA / fair value). You're trading the rubber band.

**Two diagnostic questions**
1. *Where's my target, and why does price stop there?* — "Next resistance / open-ended, a trend began" → **breakout**. "Back to the mean, the dislocation corrected" → **mean reversion**.
2. *Where's my stop, and what does hitting it prove?* — "Back inside the base, the breakout was false" → **breakout**. "Below the extreme low, the overshoot was the new reality" → **mean reversion**.

**Full discriminator**

| Axis | Breakout (BOT) | Mean reversion |
|------|----------------|----------------|
| Trend / MAs | With trend; MAs rising, supportive below | Counter-trend; MAs falling, overhead |
| The low you're buying | **Old** — a base has formed since | **Fresh** (hours/days), unbased |
| Reference point | The level is **support** (below you) | The mean is the **target** (above you) |
| Target | Open-ended — continuation | Finite — the mean (e.g. 50 EMA) |
| Stop | Back **inside the base** (level fails) | Below the **extreme low** (the origin) |
| Volume | **Must expand** on the break; low vol = kill signal | Bought exhaustion; low-vol bounce *tolerable* for entry, but weak follow-through |
| Time | Can take time to develop | Must work **fast** (snap or fail) |
| Hitting the stop proves | "Breakout was false, back to chop" | "Overshoot was the new reality" |

**The BOT score already encodes this.** The Setup gates are the breakout fingerprint, and are exactly what a mean-reversion bounce fails: **S1 price > MA50**, **S2 MA50 sloping up**, **S4 OBV rising**, **BK4 vol surge ≥ 1.2×**. A reversion bounce reads price *below* MA50, MA50 *falling*, no volume surge → low/zero score. So: **high BOT score = breakout; if you're long with failing S1/S2/BK4, you are in a mean-reversion trade and must use mean-reversion stops/targets.** (Confirmed by the retroactive test: GOLD/AAPL correctly excluded as mean-reversion, not BOT.)

**Worked example — NVO vs MCL (both "rebounding from lows")**

| | NVO (breakout) | MCL Aug'26 (mean reversion) |
|---|---|---|
| Low | Months ago, **based** since | **Yesterday**, no base |
| vs MA50 | Reclaimed / breaking above | **Below**, MA falling |
| Target | Open-ended resistance | The mean — \$92 daily 50 EMA, overhead |
| Stop | Below the base / breakout level | Below washout / 0.618 (\$87.15) |
| Volume | Expansion (had it) | Bought exhaustion; "no interest" → thesis risk |
| Outcome | — | Stopped −\$444 on a flash sell that broke the \$85 washout |

Same words ("rebound from lows"), opposite trades: NVO's low is old and *based*, breaking **up** into a new trend → breakout. MCL's low is fresh and *unbased*, snapping **back** toward an overhead mean → reversion.

**Lifecycle — a bounce can mature into a breakout, but that's a NEW trade.** They are sequential phases, not one position. Enter the mean-reversion bounce (the rubber band); *if* it then bases and breaks out, re-enter or add as a breakout with its own stop/target. The reversion runner does **not** silently become a breakout hold — that's the "don't switch frameworks mid-trade" discipline applied to the lifecycle.

---

## Gate 0 — Market Regime

**Source:** SPX drawdown from All-Time High (not VIX, not MA50 alone)

| Regime | Definition | Action |
|--------|-----------|--------|
| **BULL** | SPX DD > -5% from ATH | All sectors eligible (stock-level filter applies, see Gate 2) |
| **CORRECTION** | SPX DD -5% to -10% | Prudence: only if sector gate long = TRUE AND stock RS > 0. Reduced size. |
| **BEAR** | SPX DD < -10% | Selective: Technology, Defence, Precious Metals only. Recovery breakouts. |

**Why not VIX?** VIX > 25 correlates with SPY +3% in next 20 days 55% of the time. High VIX = fear = often a buying opportunity, not a warning. VIX is informational, not a gate.

**Why not SPX < MA50?** SPX can be below MA50 during consolidation above support (happened 7 out of 15 periods in 5 years). Too many false negatives.

**Why DD from ATH?** The correction zone (-5% to -10%) is the worst for breakouts (WR 43.5%, R/R 0.73). Bull and bear both work, correction doesn't — breakouts in no-man's-land abort.

---

## Gate 1 — Sector Context

**Source:** swing_scanner sector gate + macro_context tailwinds/headwinds

| Check | Rule | Source |
|-------|------|--------|
| **Sector gate long** | ETF > MA20, MA20 slope > 0, ADX > 20 | swing_scanner/sector_gate.R |
| **No major headwinds** | Check macro_context headwinds for the sector | macro_context/scenarios.R |
| **No sector exclusion** | All sectors eligible — the macro context and stock-level criteria filter, not sector labels | See note below |

**No static sector exclusion.** Backtesting showed that within "bad" sectors, specific stocks work well (ADM in Agricultural: +6.0% mean, 67% WR; KR in Consumer: +1.8%, 71% WR). The filter is at stock level (sufficient beta/momentum), not sector level. The macro context determines which sectors are favorable at any given time.

**Dynamic sector selection** — the macro context determines which sectors have BOT potential:

| Macro condition | Sectors favored | Historical edge |
|----------------|----------------|-----------------|
| Inflation / commodities rising | Basic Materials, Energy, Agricultural (ADM, CTVA) | 20d mean +4-6%, R/R 1.6-1.9 |
| Geopolitical tension | Defence, Energy, Precious Metals | Defence R/R 1.90 in all regimes |
| Risk-on / recovery | Technology, Communications | Tech in bear: +6.27%, WR 74% |
| Consumer strength | Consumer (KR, WMT, TGT) | KR: 71% WR across all regimes |
| Gold rising | Precious Metals | Only works when gold_rising = TRUE |
| Rate cuts / liquidity | Financial, Industrial | Financial WR 68% but low returns |

---

## Gate 2 — Technical Breakout Setup

**10 criteria scored (minimum 7/10 to pass)**

### From swing_scanner (6 criteria, kept as-is)

| # | Criterion | Rule | Purpose |
|---|-----------|------|---------|
| L3 | Relative Strength | RS > 0 vs sector ETF | Stock outperforms sector |
| L4a | Price position | Price > MA50 | Uptrend confirmed |
| L4b | MA50 slope | MA50 slope > 0 (5 bars) | Trend rising |
| L5a | RSI momentum | RSI14 > 50 AND RSI slope > 0 | Momentum positive |
| F1a | OBV | OBV slope > 0 (20d) | Accumulation |
| F1b | Up/Down volume | Up/Down ratio > 1.1 | Buying pressure |

### Criteria organized by phase (Setup / Breakout)

> **Note (2026-06-06):** "MA50" throughout this doc = **50-period EMA** (changed from SMA in `calc_ind`) to match the live scanner/analyze gate and the user's TradingView. The regime SPX MA50 (`bear_market_check.py`) and breadth %-above-50DMA remain SMA by convention. The retroactive test (`bot_retroactive_test.py`) still computes SMA50 — re-run on EMA to keep its sample aligned with the live gate.

**SETUP (S: 0-6) — conditions that build the base over time**

| # | Theme | Criterion | Rule |
|---|-------|-----------|------|
| S1 | Trend | Price > EMA50 | Uptrend established |
| S2 | Trend | EMA50 slope > 0 | Trend confirmed |
| S3 | Accumulation | RS > 0 vs sector ETF | Relative strength built up |
| S4 | Accumulation | OBV slope > 0 (20d) | Institutional accumulation |
| S5 | Consolidation | Squeeze: range_20d / range_40d < 0.65 | Range contracting |
| S6 | Consolidation | Volume decline: vol_20d / vol_50d < 0.95 | Supply drying up |

**BREAKOUT (BK: 0-4) — conditions that confirm the breakout NOW**

| # | Theme | Criterion | Rule |
|---|-------|-----------|------|
| BK1 | Momentum | RSI14 > 50 AND slope > 0 | Momentum accelerating |
| BK2 | Momentum | Up/Down volume ratio > 1.1 | Buying pressure |
| BK3 | Confirmation | Price in top 30% of 20d range (rng_pct >= 70) | Pushing against resistance |
| BK4 | Confirmation | Volume surge >= 1.2x average | Volume confirmation today |

**Signal color:**
- **Green**: S >= 5 AND BK >= 3 → breakout confirmed
- **Amber**: S >= 5 with BK 1-2, or S >= 4 with BK >= 3 → watch
- **Grey**: insufficient setup or trigger

### Additional filters (not scored, but required)

| Filter | Rule | Purpose |
|--------|------|---------|
| **No re-breakout** | No breakout signal on same ticker in last 30 days, UNLESS price returned to consolidation zone AND new squeeze formed (B1 < 0.65 again) | Late momentum traps |
| **Not parabolic** | MA50 dist <= 15% (L5b) | Avoids FOMO entries |
| **Institutional quality** | Price > $3, avg volume > 500K | No penny stocks |
| **Sufficient beta** (soft prior, *not* a hard reject) | ATR14/price is a prior on move *capacity*, not a gate. Genuinely quiet names (PG/KO/PEP ~1% ATR) don't move — avoid for long options. But low-ATR ≠ untradeable: catalyst-mobile megacaps (AAPL ~1.6% ATR) make episodic 5–7% moves and won big with OTM options. Favor ATR14/price > 1.5%; below it, demand a real signal + skilled near-expiry strikes (or use shares/spread). **Calibration + realized-trade backtest below.** | Rich ATR raises the base rate of payable moves; the real graveyard is the MID 1.7–3% bucket, not the low one |
| **Not structurally mean-reverting** | Avoid fertilizer/commodity-cycle stocks (MOS, CF, IPI) where price reverts to production cost. ADM (food processing, demand-driven) is OK. | Mean-reverting stocks: breakout signals fire but reverse within 10-20 days |

**Sector-specific holding period note:** On Agricultural and Consumer stocks, the profit window is shorter (~10 days vs 20 days for Materials/Tech). Exit discipline must be tighter — take profits earlier, do not hold for full 20-day target.

### Expected-move calibration — ATR → N-day move (validated 2026-06-08)

The "Sufficient beta" filter quantified. Empirically validated on 5y daily across 12 tickers spanning 1.2–4.6% ATR (full report: `Reports/atr_move_heuristic_validation_20260608.md`; script `Strategies/Breakouts/atr_move_validation.py`). Use it to estimate a name's move and pick the vehicle.

**Formula** (random-walk √T scaling — confirmed, measured σ₁₀/σ₁ = 3.11 vs √10 = 3.16):

```
move(N) = C × ATR% × √N          (ATR% = ATR14 / price; N = sessions)

C_typical (median) = 0.48     →  10-day typical move ≈ 1.5 × ATR%
C_strong  (p90)    = 1.25     →  10-day strong  move ≈ 4   × ATR%
```

The typical move is **1.5× ATR%, not 3×** — the "√10 ≈ 3×" shortcut is an ~85th-percentile (strong) move, not the base case. Scale to any DTE with √N (e.g. 20-day typical = 0.48 × √20 = 2.15 × ATR%). Do NOT linearly extrapolate the multiple.

**Pay-for-entry frequency** — P(≥6% move in 10 days), the proxy for "an OTM call can ~triple" (the gate that decides whether long calls are viable):

| ATR% bucket | Examples | P(payable move) | Vehicle implication |
|---|---|---|---|
| ~1.5% (low-beta defensive) | PG, KO, JNJ, PEP | **6–8%** | Long calls structurally lose (theta ~93% of windows) → **shares or SELL premium** |
| ~2.0–2.3% (mid) | ABBV, MRK, TMO, UNH | 18–25% | Long calls viable but minority → **spreads / pay-for-entry discipline** |
| ~4% (high-beta) | NVDA, AMD, TSLA | **53–58%** | Convexity pays → **long OTM calls in sweet spot** |

**Sector calibration of C** (the coefficients carry a small, measurable sector tilt — the *level* difference is already in ATR%; C is the normalized shape; driver is trend/gap/event-density, not beta, so Financials cluster with Tech):

```
                  C_typical   C_strong
Tech / Financials   0.52        1.35     (fatter tails — nudge strong move up ~10%)
Healthcare/Energy   0.47        1.23
Staples             0.46        1.18
```

Default 0.48 / 1.25 is accurate to ~10% in any sector; C_typical spread is only ±6%, C_strong (the tail) is the more sector-dependent one.

**Realized-trade backtest — ATR vs actual BOT outcomes (104 trades, 2026-06-08).** Tested the framework against the real BOT trade log (`Strategies/Breakouts/bot_atr_validation.py`):

- **Winners ARE richer-ATR** — median 2.94% vs losers 2.33% (holds on the 99-trade options subset). The high-ATR (≥3%) bucket carried **+\$8,056** and 10 of the 20 biggest wins. As an aggregate prior, ATR is real.
- **But low-ATR is NOT a hard reject.** Low-ATR (<1.7%) option trades won **47%** (+\$4,098 net), including the 2nd/3rd biggest wins ever — **AAPL OTM call +\$1,346 and AAPL OTM put +\$1,277 at ~1.6% ATR** — plus JNJ/V/GLD. The unconditional 6–8% payable stat understates the *conditional* (post-signal) + skilled-near-expiry-strike hit rate.
- **ATR% conflates two "low" types:** genuinely quiet (PG/KO/PEP — never traded, correctly avoided) vs **catalyst-mobile megacaps** (AAPL — low range-average but episodic 5–7% movers). Do not reject the latter.
- **The real money-pit is the MID bucket (1.7–3% ATR): ~32% win rate, net negative.** Marginal-beta breakouts that abort. Scrutinize mid-ATR setups *harder* than low or high.

**Bottom line — treat ATR as a PRIOR + sizing input, not a gate:** rich ATR → higher base rate, size up; low ATR → demand a genuine signal + good strikes (megacaps OK); **mid ATR → the danger zone.**

---

## Gate 3 — Vehicle Selection

**The vehicle has intrinsic characteristics that constrain the exit strategy.**

### Decision tree

```
                    Breakout identified (Gates 0-2 passed)
                                  │
                        Options chain liquid?
                      (OI > 100, bid/ask < 20%)
                         /              \
                       NO               YES
                        │                │
                   STOCK DIRECT      Call OTM $1-2 exists
                   (stop + TP)       within budget ($400)?
                                      /           \
                                    NO            YES
                                     │              │
                               Call ATM/OTM     CALL OTM
                               costs > $3?      (standard BOT)
                                /       \
                              NO        YES
                               │         │
                           CALL OTM    BULL CALL SPREAD
                           (1-2 lots)  (3 lots for pay-for-entry)
```

### Vehicle characteristics and constraints

| Vehicle | Convexity | Max loss | Theta | Pay-for-entry | Exit strategy |
|---------|-----------|----------|-------|---------------|---------------|
| **Call OTM** ($1-2) | **Strong** (x3-x5) | Premium paid | Enemy — forces timing | Sell 1/3 at x3 | BS target grid + "no asymmetry" override |
| **Bull call spread** (3 lots) | **Capped** at spread width | Debit paid | Mixed | Sell 1/3 at ~60% max profit | At % of max profit targets |
| **Stock direct** | Linear | Stop loss | None | Sell 1/3 at 1st target | Stop + TP mechanical + qualitative "no asymmetry" |

### Vehicle selection criteria

| Factor | Stock | Call OTM | Spread |
|--------|-------|----------|--------|
| Underlying price < $10 | **YES** | No (illiquid options) | No |
| Underlying price $10-150 | Possible | **YES** (sweet spot) | If IV high |
| Underlying price > $150 | No (capital) | If call < $2 | **YES** |
| IVP < 60 | — | **YES** | — |
| IVP > 60 | — | No (expensive) | **YES** (vega neutral) |
| IV30 < RV30 (VRP < 0) | — | **YES** (cheap vol) | — |
| Expected hold > 30 days | **YES** (no theta) | No | No |
| Expected hold 8-14 days | — | **YES** (sweet spot) | OK |

### Key insight: spread is NOT just a cheaper call

A spread:
- Does NOT benefit from a vol spike (short call cancels long vega)
- CAN do pay-for-entry with 3 lots (sell 1 to cover cost of 3)
- Caps upside (prisoner if underlying explodes past short strike)
- Protects against IV crush
- Is a **moderate conviction** vehicle vs call OTM = **high asymmetry conviction**

---

## Gate 4 — Comfort (Go/No-Go)

**All must be checked — this is the anti-FOMO, anti-oversizing gate.**

| Check | Rule | Source |
|-------|------|--------|
| Max loss | <= $400 per trade | Budget discipline |
| No FOMO | Movement has NOT already started (not parabolic) | FOMO trades: GLD -$X, SLV -$X |
| Thesis in one sentence | Can explain the trade rationale clearly | If you cannot, do not trade |
| Holding period | Estimated 8-14 days (options) or 20-40 days (stock) | Sweet spot from historical data |
| Sleep test | Can hold this position overnight without anxiety | Non-negotiable |

---

## Exit Strategy

### A. Call OTM exit (standard BOT)

**Step 1 — Pay for entry**
- Sell 1/N of position when that call reaches N x entry price
- Example: 3 calls at $1.25 each ($375 total). Sell 1 call at $3.75 → trade is risk-free
- The required move depends on strike selection (moderately OTM = x3 achievable with 5-8% underlying move)

**Step 2 — BS target grid (on remaining N-1 calls)**
1. Define price target on underlying via Fibonacci extension, horizon ~10 days
2. Calculate option price at target using Black-Scholes:
   - Subtract theta for days remaining
   - Add IV expansion of +3-5% IF: IVP was low at entry AND IV30 < RV30
3. Spread limit sell orders between current option price and BS target price

**Step 3 — Momentum monitor (continuous, overrides grid)**

The grid is the default plan. But momentum can break before the grid is filled. Exit signals:

| Signal | What to look for | Action | Source |
|--------|-----------------|--------|--------|
| **Momentum break** | Succession of up AND down days replacing initial directional move. Range-bound behavior replaces trending. | Close remaining position | TGT +$729: "succession of ups and downs, no significant moves" |
| **Catalyst risk** | FOMC, earnings, holiday weekend approaching. IV may collapse or gap risk. | Close or reduce before event | NTR +$464: "FOMC today, not much upside to expect" |
| **No asymmetry left** | Remaining reward does not justify remaining risk given time left and theta cost | Close | GLD +$1,692: best trade ever |
| **Sector turning** | Sector ETF breaks below MA20, or macro headwind appears | Close — the wind has changed | Your sector gate turning negative |
| **Price reclaims consolidation zone** | Price falls back into the pre-breakout range | Close — breakout has failed | Breakout thesis is dead |

**The grid and the override are not contradictory.** The grid says "if momentum continues, here is where I sell." The override says "momentum is no longer continuing, sell now regardless of where the grid says."

**Step 4 — Time stop (vehicle rule, not a thesis rule)**

The clock is imported by the long-premium vehicle, not by the breakout setup. A clean breakout pays *early*; theta runs the whole time whether or not price moves. So the time stop catches the failure the price stop and momentum monitor both miss — the trade that quietly drifts sideways: it hasn't reclaimed the range (price stop silent) and isn't chopping in a clear reversal (momentum monitor silent), but it's a slow loss to decay.

- **Concrete test — bind it to the pay-for-entry milestone.** By mid-life of the option (~day 7–10 on a 2–4 week trade), has price reached the level where you take the Step 1 pay-for-entry sale? If not, the front-loading thesis has failed — close. This turns the time stop into a *dated price check*, not a feel: a specific price, tested on a specific date.
- Theta accelerates in the final 2 weeks — do not hope past mid-life.
- On Agricultural/Consumer stocks: tighter horizon (~10 days, not 20). The profit window is shorter, so move the mid-life checkpoint earlier.
- **Vehicle scope:** this is a long-call rule. Stock (C) has no decay clock — its forcing function is capital, not theta. The bull call spread (B) gets a softer version (do not hold to expiration).

### B. Bull call spread exit (3 lots)

**Step 1 — Pay for entry**
- Sell 1/3 lots when spread reaches ~60% of max profit → covers cost of 3 lots

**Step 2 — Remaining 2 lots**
- Set targets at 70%, 80%, 90% of max profit
- Be aware: approaching max profit requires underlying to be well above short strike at expiration
- Time value works differently (no pure theta decay like single call)

**Step 3 — Do NOT hold to expiration hoping for max profit**
- Spread at 80% of max with 5 days left → close. The last 20% is not worth the risk.

### C. Stock direct exit

**Step 1 — Define risk at entry**
- Stop loss: below consolidation zone (typically 1-1.5 ATR below breakout level)
- Take profit 1: Fibonacci extension or next resistance (1:2 risk/reward minimum)
- Both orders placed at entry ("set and forget")

**Step 2 — Pay for entry**
- Sell 1/3 at TP1 → move stop to breakeven → risk-free trade

**Step 3 — Remaining position**
- Trail stop using higher lows or MA20
- Momentum monitor applies (same signals as call OTM Step 3)
- No theta pressure → can hold longer (20-40 days), and no decay clock forcing an exit. The forcing function here is **capital allocation, not theta**: stock ownership ties up far more capital than an option, so capital parked in a name that has stopped moving is the real cost — there is no premium bleeding, but the capital is idle and could be redeployed.
- RIG (+\$344) and LAC (−\$172) were both exited when **momentum stopped** — correctly: both went sideways afterward. These are momentum trades, and the exits weren't "held too long," they freed high committed capital once the momentum thesis was spent. Qualitative (momentum gone), not mechanical.
- **Discipline rule:** when momentum stops, exit and redeploy — do not wait for the price stop, and do not leave large capital idle in a sideways name. The time stop's analogue for stock is a *capital-efficiency stop*: if the move is over, the capital should be working elsewhere.

---

## Performance Benchmarks (5-year backtest, 594 signals)

### Overall (strict criteria, stock returns, 20-day hold)

| Metric | Value |
|--------|-------|
| Win rate | 56.0% |
| Mean return | +1.54% |
| Reward/Risk | 1.25 |
| Max gain (avg) | +8.39% |
| Max DD (avg) | -6.74% |

### By regime

| Regime | N | 20d mean | WR | R/R |
|--------|---|----------|-----|-----|
| Bull | 428 | +1.73% | 53.9% | 1.32 |
| Correction | 47 | -1.89% | 43.5% | 0.73 |
| Bear | 119 | +1.16% | 56.3% | 1.10 |

### Best sectors (bull regime, R/R > 1.2)

| Sector | N | 20d mean | WR | R/R |
|---------|---|----------|-----|-----|
| Basic Materials | 47 | +6.10% | 61.7% | 1.90 |
| Defence | 30 | +4.47% | 53.3% | 1.90 |
| Communications | 23 | +1.90% | 60.9% | 1.52 |
| Technology | 81 | +2.40% | 55.6% | 1.42 |
| Healthcare | 37 | +1.44% | 51.4% | 1.41 |
| Energy | 35 | +3.26% | 60.0% | 1.28 |
| Industrial | 43 | +1.09% | 60.5% | 1.26 |
| Financial | 25 | +0.20% | 68.0% | 1.26 |

### Stocks to avoid (not sectors — stock-level filter)

| Pattern | Examples | Why |
|---------|----------|-----|
| Low-beta defensives | PG (0% WR), PEP (0% WR), KO | Move insufficient for pay-for-entry |
| Fertilizer/commodity cycle | MOS (0% WR), CF (0% WR), IPI (33%) | Structurally mean-reverting to production cost |
| "Stocks that do not move" | CSCO (0/3 in your trades) | Breakout signal fires but no follow-through |

### Stocks that work despite "bad" sector averages

| Ticker | Sector | N | 20d mean | WR | Why it works |
|--------|--------|---|----------|-----|-------------|
| ADM | Agricultural | 6 | +5.99% | 67% | Food processing = demand-driven, not commodity cycle |
| KR | Consumer non-cyc | 7 | +1.77% | 71% | Competitive dynamics, sufficient momentum |
| WMT | Consumer non-cyc | 4 | +0.84% | 50% | Scale advantage, earnings catalysts |
| MO | Consumer non-cyc | 2 | +5.39% | 100% | Dividend/yield-driven momentum |

---

## Key Lessons from Historical BOT Trades

### What works
- **Progressive exits** — AAPL +$1,346, GOLD +$1,116, DOW +$1,058
- **"No asymmetry left" exit** — GLD +$1,692 (best trade ever)
- **Pay-for-entry rule** — once 1/3 sold at cost, the rest runs risk-free. Works for calls AND spreads (buy 3 lots, sell 1)
- **BS-based target grids** — JNJ +$1,040, DOW +$1,058
- **Small position sizes** — 1-5 contracts, avg winner +$548
- **Momentum monitor override** — NTR +$464: sold at +10d when "not much upside momentum to expect" (backtest shows NTR reverts at 20d)
- **Cutting on thesis invalidation, not stop loss** — LAC -$172: "no more asymmetry, better to quit" (best loss ever)

### What fails
- **FOMO entries** — GLD "FOMO", SLV "FOMO", URA "FOMO" — all identified in notes
- **Event bets labeled BOT** — SPY straddles, FOMC plays. These are not breakouts.
- **Mean-reversion trades labeled BOT** — GOLD S:0 BK:1, AAPL S:0-1 BK:0. Profitable but not BOT — different framework.
- **Futures** — 0/3 win rate, -$740. No convexity, linear loss
- **Repositioning strike without duration** — USO -$507
- **Automatic profit targets** — STNG: left $200+ on table. The grid is default, but momentum monitor overrides it.
- **Oversizing** — positions > 5 contracts consistently underperformed
- **Laziness / delayed exits** — C -$324: "should have closed earlier, I was lazy"
- **Low-beta defensives** — PG (0% WR), PEP (0% WR): breakout signal fires but move insufficient for pay-for-entry
- **Structurally mean-reverting stocks** — MOS (0% WR), CF (0% WR): price reverts to production cost
- **Entering before the trigger** — DOW S:4 BK:0 at entry, breakout came 2 days later. Setup was visible but conviction entry, not signal entry.

### Key insight from retroactive test
The BOT screener captures a **specific type** of breakout (post-consolidation with squeeze). The best historical trades include mean-reversion (GOLD, AAPL) and conviction entries (DOW) that are **outside** the BOT framework. The screener is a discovery tool, not an exclusive filter. Trades outside the framework require higher conviction and tighter exit discipline.

---

## Backtest Files

- `breakout_backtest_5y.py` — 5-year backtest script (Yahoo Finance data)
- `breakout_5y_results.csv` — all 594 breakout signals with forward returns
- `bear_market_check.py` — regime analysis (SPX DD, VIX, sector by regime)
- `bot_analysis.md` — original BOT deep dive (2025)
- `bot_breakout_analysis_2026.md` — comprehensive BOT analysis with DOW screener

---

*Last updated: 2026-06-08 (added Expected-move calibration — validated ATR→N-day multiples, payable-frequency, sector C-coefficients)*
*Based on: 819 breakout signals across 152 stocks over 5 years (2021-2026)*
*Backtest method: squeeze < 0.65, vol decline < 0.95, daily return >= 1.5%, volume surge >= 1.2x*
