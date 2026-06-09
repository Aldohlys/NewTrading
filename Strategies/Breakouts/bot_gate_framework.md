# BOT Trade Selection — Gate Framework

*Created: 2026-03-18 | Based on 96 closed BOT trades (Jul 2022 – Mar 2026) + vol profile analysis of winners/losers*

---

## Problem Statement

The swing scanner + WITT sessions generate **dozens of BOT candidates per week**. Capacity is **1-2 new BOTs per week, 10-15 total trades open**. This framework filters candidates down to the highest-conviction setups by passing them through 5 sequential gates.

---

## GATE 1: Direction × Macro Regime

**Purpose**: Avoid fighting the market. Use macro breadth to determine whether long or short BOTs are appropriate.

| S&P 500 Breadth (% > MA50) | Long BOT | Short BOT |
|:---:|:---:|:---:|
| < 20% (capitulation) | **HIGH CONVICTION** | NO — shorts exhausted |
| 20-35% (oversold) | **PREFERRED** | CAUTION — only if Gate 3 is A+ |
| 35-65% (neutral) | Yes | Yes |
| 65-80% (overbought) | CAUTION | PREFERRED |
| > 80% (euphoria) | NO — longs exhausted | **HIGH CONVICTION** |

**Data source**: macro_context report → Section 03 Breadth.

**Additional regime checks**:
- VIX > 30 → high uncertainty, reduce position size
- VIX term structure in backwardation → stress regime, favor puts
- DXY trend → impacts precious metals and commodities directionally
- Event calendar → **no entry within 24h of FOMC, CPI, or OpEx**

---

## GATE 2: Scanner Quality + Directional Fit

**Purpose**: Only consider names with strong technical setups in the regime-appropriate direction.

| Criterion | Threshold |
|-----------|-----------|
| Scanner score | **≥ 8** (TRADE signal, not WATCH/SKIP) |
| Direction | Must align with Gate 1 regime ruling |
| Relative strength (RS_vs_ETF) | Positive for longs, negative for shorts |

**No sector exclusion** — all sectors eligible. Historical sector performance informs conviction level but doesn't eliminate:

| Sector | Historical BOT Edge | Note |
|--------|:---:|------|
| Precious Metals | +$395 avg, 66.7% WR | Best sector — trending behavior |
| Consumer non-cyclical | +$264 avg, 60% WR | Clean breakouts |
| Technology | +$214 avg, 44.4% WR | Decent but noisier |
| Basic Materials | +$134 avg, 36.4% WR | Mixed |
| Energy | -$66 avg, 30% WR | Weak historically BUT macro-dependent (oil regime matters) |

---

## GATE 3: Vol Profile (4 Dimensions)

**Purpose**: Identify mispriced options — the "calm before the storm" setup. Derived from analysis of all BOT winners and losers, not just DOW #692.

### Primary Criteria (need ≥ 3 of 4 to pass)

| # | Criterion | Threshold | Rationale |
|---|-----------|-----------|-----------|
| 1 | **IV30 < 40%** | Low absolute vol | Winners avg 27.7% vs losers 35.9% — buy when calm |
| 2 | **IVP < 60%** | Room for IV expansion | You want to enter before vol reprices upward |
| 3 | **RVP > 30%** | Some momentum exists | Stock is moving, not sleeping — breakout has fuel |
| 4 | **VRP context check** | See below | Negative VRP can be good or bad depending on context |

### VRP Interpretation (IV30 - RV30)

VRP requires nuance because IV is forward-looking and RV is backward-looking:

| VRP | IVP | Reading | Action |
|:---:|:---:|---------|--------|
| Negative (IV < RV) | **Low (< 50%)** | Options cheap AND IV hasn't repriced yet → **mispricing, opportunity** (DOW pattern) | **PASS** |
| Negative (IV < RV) | **High (> 70%)** | IV already expanded but RV spiked more → likely **end of move, chasing** | **FAIL** |
| Near zero | Any | Fair pricing, no vol edge either way | Neutral — rely on other gates |
| Positive (IV > RV) | Low | Options slightly expensive but vol is quiet → breakout not started | Acceptable if IVP is low |
| Positive (IV > RV) | High | Expensive options AND high IV → **overpaying** | **FAIL** |

### The DOW A+ Setup (all 5 = highest conviction)

When a candidate passes all of the below, it's an A+ setup:

1. Negative VRP (options cheap vs realized)
2. Low IVP (< 50% — room for expansion)
3. High RVP (> 60% — stock already moving)
4. Large IVP-RVP gap (< -15 pts — market hasn't priced the movement)
5. Technical breakout confirmed

### 4-Dimension IV Assessment (for A+ candidates)

| Dimension | What to check | Favorable |
|-----------|--------------|-----------|
| **1. IVP** | IV vs own history | Low (< 50%) |
| **2. Peer VRP** | IV vs similar stocks | Cheapest in peer group |
| **3. Term structure** | Near-term vs longer-term IV | Near-term cheaper (contango) |
| **4. Skew** | Put/call skew percentile | Flat — OTM options not penalized |

**Data source**: Prices table in DB (`SELECT * FROM Prices WHERE sym = ? AND iv30 IS NOT NULL ORDER BY ROWID DESC LIMIT 1`) or TWS vol tab for real-time data.

---

## GATE 4: Execution Viability

**Purpose**: Ensure the trade can be properly managed per BOT rules.

| Criterion | Type | Rule |
|-----------|:---:|------|
| **Min 3 contracts** | Hard | Enables partial exit plan (sell 1 at 3x or sell 2 at 2x to go risk-free) |
| **Asymmetry articulable** | Hard | Write the R/R in 1 sentence before entry. If you can't, skip. Trades with noted asymmetry: +$349 avg vs +$51 without |
| **BS target grid feasible** | Hard | Risk-free achievable at T+5 with ≤ 5% underlying move |
| **No sector overconcentration** | Soft | Max 2 BOTs in same sector |
| **Tuesday/Wednesday entry** | Soft | Tue +$177 avg, best entry day. Wed acceptable. Avoid Mon/Thu/Fri |
| **Delta at entry 0.25-0.40** | Soft | Sweet spot for breakout options — enough gamma, not too expensive |
| **Outright option** | Hard | No pure vertical spreads (0% WR), no futures (0% WR). Bull call spread OK only if you plan to buy back short leg |
| **No event within 24h** | Hard | FOMC, CPI, earnings within DTE window = skip |

---

## GATE 5: Kill Signals (any one = immediate skip)

- Delta at entry < 0.20 (lottery ticket, not a trade)
- Earnings within DTE window
- Already have 2+ BOT open in same sector
- You can't explain why *now* and not last week
- 2-leg trade plan (no management plan = net loser historically: -$117 avg)
- Chasing: underlying already moved > 5% in the direction you want to trade in the last 5 days

---

## POST-ENTRY MANAGEMENT

These rules apply once a BOT trade is open. They are as important as entry selection — the difference between 2-leg trades (-$117 avg) and 3+ leg trades (+$283 avg) is entirely management.

### Partial Profit / Risk-Free Protocol

| Contracts | Risk-Free Target | How |
|:---------:|:---:|------|
| 3 | Sell 1 at 3x entry cost | Covers total cost, 2 remain free |
| 4 | Sell 2 at 2x entry cost | Covers total cost, 2 remain free |
| 5+ | Sell enough to cover cost | Remaining contracts = pure upside |

**Impact**: Trades with partial profit/risk-free: 92.3% WR, +$637 avg. Without: 33.7% WR, +$13 avg.

### Exit Rules

| Signal | Action |
|--------|--------|
| All BS targets hit | Close remaining |
| Price falls back inside fib zone for 2+ days | Close — breakout failed |
| Delta drops below 10 | Cut — option is dying |
| "No more asymmetry" | Close immediately (your best exit signal historically) |
| Day 10-12 without profit | Tighten stop to entry cost |
| Day 25+ | Close — diminishing returns (sweet spot is 6-14 days) |
| Last week before expiration | Close (your rule) |
| Never reposition strike without duration | If adjusting, extend expiry too (USO #404 lesson) |

### Duration Sweet Spot

| Duration | Win % | Avg P&L |
|----------|:-----:|--------:|
| 0-5 days | 25.0% | +$56 |
| **6-14 days** | **52.0%** | **+$146** |
| 15-25 days | 40.6% | +$120 |
| 26+ days | 39.1% | +$43 |

---

## WEEKLY WORKFLOW

```
MONDAY
├─ Run macro_context → determine regime (Gate 1)
├─ Check event calendar for the week
└─ Review open BOTs: delta, P&L, days in trade

TUESDAY (primary entry day)
├─ Run swing_scanner → filter score ≥ 8 in regime direction (Gate 2)
├─ Pull vol profiles for survivors (Gate 3)
├─ Apply execution viability checks (Gate 4)
├─ Kill signal check (Gate 5)
├─ If candidate passes all gates:
│   ├─ Compute BS target grid
│   ├─ Write asymmetry note
│   └─ Enter: outright option, min 3 contracts, set partial profit orders
└─ If no candidate passes → no trade this week (discipline > activity)

WEDNESDAY-FRIDAY
├─ Manage open BOTs per exit rules
├─ Execute partial profits if targets hit
└─ Cut zombies (delta < 10, duration > 25 days)
```

---

## REFERENCE: Top Winner Patterns

All top 10 winners shared these traits:
1. Active position management (scaling out progressively)
2. Pre-defined targets (BS-model or fib-based)
3. Risk removed early (cost covered by first partial sale)
4. Duration 6-20 days (not held to expiration)
5. Clear thesis documented at entry

## REFERENCE: Top Loser Patterns

All top 10 losers shared these traits:
1. No active management (2-leg trades left to die)
2. Wrong instrument (futures, pure spreads)
3. Chasing (entering after the move)
4. Ignoring own rules (bad R/R, missing confirmation)
5. Repositioning strike without repositioning duration
