# BOT STRATEGY - COMPREHENSIVE CHECKLIST
**Complete Decision Framework for Breakout Option Trades**
**Max Risk Per Trade: CHF 600 | Base Currency: CHF**

---

# SECTION A: ENTRY

## A1. MACRO BACKDROP & SECTOR FILTER

### A1.1 Macro Regime Assessment

**Before ANY BOT trade, answer these questions:**

**Question 1: What is the current market regime?**

| Regime | Characteristics | BOT Action |
|--------|-----------------|------------|
| **Risk-On** | VIX <16, equities rising, credit tight | Favor CALLS on growth sectors (Tech, Consumer) |
| **Risk-Off** | VIX >22, flight to safety | Favor PUTS on cyclicals, or CALLS on Gold/TLT |
| **Transitional** | VIX 16-22, mixed signals | Be selective, tighter position sizing |
| **High Volatility** | VIX >25, fear elevated | AVOID index options, use SPREADS not outrights |

**Question 2: Is the underlying aligned with the dominant regime?**

| Underlying Sector | Risk-On | Risk-Off | Neutral |
|-------------------|---------|----------|---------|
| **Precious Metals** (GLD, SLV, GOLD) | Neutral | Favorable | OK |
| **Technology** (AAPL, SAP, ASML) | Favorable | Unfavorable | OK |
| **Healthcare** (JNJ, ABBV, Novartis) | Neutral | Favorable | OK |
| **Consumer Retail** (WMT, MCD) | Favorable | Neutral | OK |
| **Energy** (XOM, TotalEnergies) | Favorable | Unfavorable | Selective |
| **Financials/Banks** | Favorable | Unfavorable | Avoid |
| **Indices** (SPY, SPX) | Avoid unless VIX rising | Avoid | Avoid |

**Comment:** Your historical data shows:
- Precious Metals: +$4,303 total, 46% WR (best sector)
- Tech Mega Cap: +$2,685, 57% WR
- Consumer Retail: +$957, 100% WR
- **Indices: -$610, 33% WR (WORST) - IV crush trap**

---

### A1.2 Sector-Specific Validation

**For each sector, check specific considerations:**

**PRECIOUS METALS (GLD, SLV, GOLD):**
- [ ] USD trend? (Gold inversely correlated to USD strength)
- [ ] Real rates direction? (Falling real rates = bullish gold)
- [ ] Geopolitical/inflation catalyst present?
- **TIER 1:** GLD, SLV, GOLD
- **AVOID:** GC futures (sizing issues), GDX/NEM (miners underperform metal)

**TECHNOLOGY (AAPL, SAP, ASML, NFLX):**
- [ ] Is the broader tech sector showing leadership?
- [ ] Earnings calendar: Avoid entry 5 days before earnings
- [ ] Is this a sector breakout or individual stock story?
- **TIER 1:** AAPL, NFLX, SAP, MU, QCOM
- **AVOID:** CSCO (0% WR!), GOOG (poor track record)

**ENERGY (XOM, TotalEnergies, EQT):**
- [ ] Is the narrative already overcrowded? (Geopolitical premium?)
- [ ] Crude oil trend: Strong trend or choppy?
- [ ] Sector vs single stock: Is XOM outperforming sector?
- **TIER 1:** XOM only (100% WR), EQT, RRC (nat gas), TotalEnergies (EUR)
- **AVOID:** USO (-$1,010!), MCL futures, HAL, OVV (0% WR)

**HEALTHCARE (JNJ, ABBV, Novartis):**
- [ ] Catalyst: FDA approvals, earnings, M&A?
- [ ] Defensive rotation: Is money flowing to healthcare?
- **TIER 1:** JNJ (100% WR), ABBV (100% WR), Novartis (CHF)
- **AVOID:** PFE, GILD, MRK (all 0% WR)

**CONSUMER RETAIL (WMT, MCD):**
- [ ] Consumer sentiment: Is consumer spending strong?
- [ ] Seasonal factors: Holiday season, back-to-school?
- **TIER 1:** WMT (100% WR), MCD (100% WR)
- **Comment:** Small sample but excellent track record

---

### A1.3 Narrative & Crowding Check

**Question 3: Is this trade already consensus?**

| Check | Method | Red Flag |
|-------|--------|----------|
| **Media coverage** | Financial news, Twitter | "Everyone" talking about it |
| **Options OI** | Check open interest at strike | Unusually high OI = crowded |
| **Recent performance** | Has it already moved 10%+? | Late to the party |
| **Analyst sentiment** | Upgrades/downgrades | Too many upgrades = priced in |

**Your own lesson:** USO trade #348: "Completely unexpected move downwards. Seems it was an overcrowded trade."

**Rule:** If trade feels "too easy" or "obvious," add extra caution. Crowded trades reverse violently.

---

## A2. RISK CONSIDERATIONS

### A2.1 Position Risk

**Hard Rule: Max CHF 600 per trade**

| Structure | How to Calculate Max Risk |
|-----------|---------------------------|
| **Outright Call/Put** | Premium × Contracts ≤ CHF 600 |
| **Debit Spread** | (Width - Credit) × Contracts × 100 ≤ CHF 600 |

**Position Sizing Examples:**

| Stock | Price | Premium | Contracts | Total Risk | OK? |
|-------|-------|---------|-----------|------------|-----|
| TotalEnergies | €62 | €1.80 | 3 | €540 (CHF 518) | ✓ |
| SAP | €230 | €5.50 | 1 | €550 (CHF 528) | ✓ |
| ASML | €900 | €22 | 1 | €2,200 (CHF 2,112) | ✗ Too expensive |
| UBS | CHF 28 | CHF 0.80 | 6 | CHF 480 | ✓ |
| Novartis | CHF 92 | CHF 3.50 | 1 | CHF 350 | ✓ |
| GLD | $265 | $4.50 | 1 | $450 (CHF 396) | ✓ |

**ASML Note:** Too expensive for CHF 600 limit. Options:
1. Skip ASML for outright BOT
2. Use debit spread (reduces cost)
3. Accept as exception with explicit larger risk

---

### A2.2 Currency Risk

**You are a CHF-based investor. USD is a trading vehicle, not your wealth currency.**

**Target Currency Allocation:**

| Currency | Target | Rationale |
|----------|--------|-----------|
| **USD** | 30-40% | Best options liquidity, proven winners |
| **EUR** | 40-50% | Hedge USD, matches 30% EUR expenses |
| **CHF** | 10-20% | Base currency anchor |

**Before each BOT trade, check:**

- [ ] **Current USD exposure:** $_________ = CHF _________ (___%)
- [ ] **Current EUR exposure:** €_________ = CHF _________ (___%)
- [ ] **Current CHF exposure:** CHF _________ (___%)
- [ ] **Is the currency I'm entering under-allocated?**

**Currency Decision Matrix:**

| If USD | If EUR | If CHF | Action |
|--------|--------|--------|--------|
| >50% | <30% | Any | Prioritize EUR trades |
| <30% | >50% | Any | Prioritize USD trades |
| 30-50% | 30-50% | <10% | Add CHF trade |
| Balanced | Balanced | Balanced | Choose best technical setup |

**Comment:** Your current exposure (from earlier):
- CHF: 70% (mostly cash)
- USD: 26%
- EUR: 12% ← **Under-allocated** (target 40-50%)
- **Priority: Add EUR BOT positions**

---

### A2.3 Sector Concentration Risk

**Rule: No more than 2-3 positions in same sector simultaneously**

**Before entry, count existing positions:**

| Sector | Max Positions | Current Positions | Can Add? |
|--------|---------------|-------------------|----------|
| Precious Metals | 2-3 | _____ | |
| Technology | 3-4 | _____ | |
| Energy | 2 | _____ | |
| Healthcare | 2 | _____ | |
| Consumer | 2 | _____ | |
| Financials | 1-2 | _____ | |

**Correlation Warning:**
- GLD + SLV + GOLD = Highly correlated (count as 1 "super position")
- AAPL + SAP + ASML = Less correlated (can hold all 3)
- XOM + USO + TotalEnergies = Highly correlated (oil price)

**Your lesson:** Having 3 oil positions (XOM + USO + MCL) means triple exposure to oil price swings.

---

### A2.4 Portfolio-Level Risk Budget

**Weekly Risk Budget:**

| Metric | Target | This Week |
|--------|--------|-----------|
| **New positions added** | 2-3 BOT trades | |
| **Total new risk deployed** | CHF 1,200-1,800 | |
| **Total open BOT risk** | Max CHF 6,000 | |
| **Open position count** | 5-7 BOT trades | |

**Rule:** Don't add new positions if total open BOT risk exceeds CHF 6,000 (10 × CHF 600 max)

---

## A3. TECHNICAL ANALYSIS

### A3.1 Breakout Validation

**All 4 conditions must be met:**

**Condition 1: Price Action Confirmation**

- [ ] **Breakout above/below key level?**
  - Resistance broken (for calls)
  - Support broken (for puts)
  - Must close beyond level, not just intraday touch

- [ ] **Fibonacci zone breached?**
  - Price exited consolidation zone
  - Not just testing the edge, but clearly through

**Condition 2: Trend Alignment**

- [ ] **DMA (Daily Moving Average) confirmation?**
  - For CALLS: Price above 25 DMA AND 50 DMA
  - For PUTS: Price below 25 DMA AND 50 DMA
  - Mixed (above one, below other) = CAUTION

- [ ] **Higher timeframe alignment?**
  - Weekly chart confirms direction
  - Monthly trend not counter to trade

**Condition 3: Volume Confirmation**

- [ ] **Volume on breakout?**
  - Volume >1.5× average on breakout day
  - Low volume breakout = higher failure rate
  - "Volume precedes price"

**Condition 4: Breakout Quality**

| Breakout Type | Win Rate | Comment |
|---------------|----------|---------|
| **Continuation** | Higher | Already trending, breaking new level |
| **First attempt** | Lower | Breaking from long consolidation, may fail |
| **Retest & go** | Highest | Broke, pulled back, confirmed, continuing |

- [ ] **Is this a continuation or first attempt?**
  - Continuation (preferred): Already in trend, breaking to new highs/lows
  - First attempt (riskier): Breaking out of range for first time
  - Retest: Broke out, pulled back, now resuming (best)

---

### A3.2 Target Definition

**Before entry, define your exit target:**

**Target 1: Fibonacci Extension**

| Fib Level | Probability | Action |
|-----------|-------------|--------|
| **1.0 extension** | High | Take 1/3 profit here |
| **1.272 extension** | Medium | Take another 1/3 here |
| **1.618 extension** | Lower | Trail stop for final piece |

- [ ] **Fib extension target calculated?** Level: _______

**Target 2: Measured Move**

- Prior swing height projected from breakout level
- Example: Stock consolidated $100-110, breaks $110, target = $120 (=$10 swing)

- [ ] **Measured move target?** Level: _______

**Target 3: Prior Resistance/Support**

- Previous swing high (for calls)
- Previous swing low (for puts)

- [ ] **Prior swing target?** Level: _______

**Use the nearest target as your primary exit level.**

---

### A3.3 Momentum Assessment

**Question: Is there momentum, or is this a choppy range?**

**Momentum Indicators (at least 2 should confirm):**

| Indicator | Bullish Signal | Bearish Signal | Current |
|-----------|----------------|----------------|---------|
| **RSI** | >50 and rising | <50 and falling | |
| **MACD** | Histogram positive, expanding | Histogram negative, expanding | |
| **ADX** | >25 (strong trend) | <20 (weak/no trend) | |
| **Price vs MAs** | Above 10, 25, 50 MA | Below all MAs | |

- [ ] **Momentum confirmed?** (2+ indicators agree)

**Warning Signs (Avoid Entry):**

- RSI divergence (price makes new high, RSI doesn't)
- Momentum slowing into resistance
- ADX <20 (no trend)
- Multiple failed breakout attempts

---

## A4. OPTION PRICING CONSIDERATIONS

### A4.1 IV Percentile Assessment

**Step 1: Check IV Percentile (IV Rank)**

**What is IV Percentile?**
- Compares current IV to past 52-week range
- IV at 30%ile = Current IV is lower than 70% of the past year
- IV at 80%ile = Current IV is higher than only 20% of the past year

**How to find IV Percentile:**
- IBKR: In option chain, look for "IV Rank" or "IV%"
- Alternative: Compare current IV to 52-week high/low
- Formula: (Current IV - 52wk Low) / (52wk High - 52wk Low) × 100%

**Example:**
- Stock IV: 35%
- 52-week IV range: 20% - 60%
- IV Percentile: (35-20)/(60-20) = 37.5%ile (Low-Normal)

**IV Percentile Decision Matrix:**

| IV Percentile | Assessment | BOT Structure | Rationale |
|---------------|------------|---------------|-----------|
| **<30%** | Very Low | OUTRIGHT option | Max vega benefit from IV expansion |
| **30-50%** | Low-Normal | OUTRIGHT option | Good - room for IV expansion |
| **50-70%** | Neutral-High | DEBIT SPREAD | Protect from IV crush |
| **>70%** | High | TIGHT SPREAD or PASS | High IV crush risk |

- [ ] **IV Percentile checked?** Current IV%ile: _______%
- [ ] **Structure selected?** Outright / Spread

---

### A4.2 Outright vs Debit Spread Decision

**Decision Tree:**

```
┌─────────────────────────────────────────────────────────┐
│           OUTRIGHT vs SPREAD DECISION                   │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
              ┌──────────────────────┐
              │ IV Percentile > 60%? │
              └──────────────────────┘
                    │         │
                   YES        NO
                    │         │
                    ▼         ▼
           ┌─────────────┐  ┌────────────────────────┐
           │ USE SPREAD  │  │ Is premium > CHF 600? │
           │             │  └────────────────────────┘
           │ Benefits:   │        │         │
           │ -IV crush   │       YES        NO
           │  protection │        │         │
           │ -Defined    │        ▼         ▼
           │  risk       │  ┌─────────────┐ ┌──────────────┐
           └─────────────┘  │ USE SPREAD  │ │ USE OUTRIGHT │
                            │ (cost       │ │              │
                            │ reduction)  │ │ Benefits:    │
                            └─────────────┘ │ -Full vega   │
                                            │  exposure    │
                                            │ -Home run    │
                                            │  potential   │
                                            └──────────────┘
```

**Additional Spread Considerations:**

| Factor | Favor Outright | Favor Spread |
|--------|----------------|--------------|
| **IV level** | Low (<50%ile) | High (>50%ile) |
| **Premium cost** | Within CHF 600 budget | Exceeds budget |
| **Conviction** | High (want max upside) | Medium (want defined risk) |
| **Stock type** | Single stock | Index ETF |
| **Underlying** | High-priced (ASML) | Lower-priced |
| **Earnings** | None upcoming | Pre-earnings |

---

### A4.3 Strike Selection (Delta-Based)

**Rule: Use DELTA, not absolute premium price**

**Delta Guidelines:**

| Conviction | Delta | Strike Type | Profile |
|------------|-------|-------------|---------|
| **High** | 45-55 | ATM (At the Money) | Fastest P&L, higher cost, lower leverage |
| **Medium** | 30-40 | Slightly OTM | Balanced - MOST COMMON for BOT |
| **Low/Testing** | 20-30 | OTM | Cheaper, higher leverage, needs bigger move |
| **Avoid** | <20 | Deep OTM | Lottery ticket, usually loses |

**Your data proves:**
- Options with <20 delta (far OTM, cheap): 13.8% WR ← AVOID
- Options with 30-50 delta (moderate OTM to ATM): 70%+ WR ← USE THESE

**How to find Delta:**
- IBKR: Option chain shows delta for each strike
- Rule of thumb: ATM ≈ 50 delta, add/subtract ~5 delta per strike

**Strike Selection Process:**

1. **Find ATM strike** (closest to current price)
2. **For HIGH conviction:** Use ATM (50 delta)
3. **For MEDIUM conviction:** Go 1-2 strikes OTM (35-45 delta)
4. **For LOWER conviction:** Go 2-3 strikes OTM (25-35 delta)
5. **NEVER:** Go >4 strikes OTM (<20 delta)

**Example (SAP at €230):**

| Strike | Delta | Type | Premium | Verdict |
|--------|-------|------|---------|---------|
| €230 | 50 | ATM | €8.50 | High conviction |
| €235 | 40 | OTM | €5.50 | **Medium conviction (standard)** |
| €240 | 30 | OTM | €3.50 | Lower conviction |
| €250 | 18 | Deep OTM | €1.20 | **AVOID** |

- [ ] **Delta selected:** _____ (target 30-50)
- [ ] **Strike selected:** _______

---

### A4.4 Spread Construction (When Using Spreads)

**For Debit Call Spread (Bullish):**

| Component | Strike | Delta | Action |
|-----------|--------|-------|--------|
| **Buy** | Near ATM or slightly OTM | 40-50 | Long call |
| **Sell** | At Fib target OR 2-3 strikes higher | 20-30 | Short call |

**For Debit Put Spread (Bearish):**

| Component | Strike | Delta | Action |
|-----------|--------|-------|--------|
| **Buy** | Near ATM or slightly OTM | 40-50 | Long put |
| **Sell** | At Fib target OR 2-3 strikes lower | 20-30 | Short put |

**Spread Width Guidelines:**

| Spread Width | Cost | Max Profit | Risk/Reward |
|--------------|------|------------|-------------|
| **Narrow (€5-7.5)** | Lower | Lower | Higher leverage |
| **Medium (€10-15)** | Medium | Medium | Balanced |
| **Wide (€20-30)** | Higher | Higher | Lower leverage |

**Rule:** Sell strike at or near your technical target (Fib extension)

**Example: SAP Call Spread (stock at €230, target €245)**

| Leg | Strike | Delta | Premium | Action |
|-----|--------|-------|---------|--------|
| Buy | €235 | 40 | €5.50 | Pay |
| Sell | €245 | 25 | €2.50 | Receive |
| **Net** | | | **€3.00 debit** | |

- **Max risk:** €300 per spread (fits CHF 600 budget) ✓
- **Max profit:** €1,000 - €300 = €700 per spread
- **Breakeven:** €238 (€235 + €3)

- [ ] **Spread strikes selected?** Buy: ______ / Sell: ______
- [ ] **Net debit calculated?** €/CHF _______
- [ ] **Max risk ≤ CHF 600?** ✓ / ✗

---

### A4.5 Duration Selection (DTE)

**Sweet Spot: 15-28 DTE at Entry**

| DTE at Entry | Verdict | Reasoning |
|--------------|---------|-----------|
| **<10 DTE** | Avoid | Theta decay accelerating, less time for thesis |
| **10-14 DTE** | Acceptable | Only for very high conviction, fast breakouts |
| **15-21 DTE** | **Optimal** | Balance theta decay and time for move |
| **22-28 DTE** | Good | More time, but more expensive |
| **>28 DTE** | Caution | Paying for time you may not need |
| **>40 DTE** | Avoid | Too much capital tied up, theta too slow |

**Your Data:**
- **8-14 day holding period:** 64.3% WR (SWEET SPOT)
- **22-28 day holding period:** 22.2% WR (GRAVEYARD)

**Duration Selection Process:**

1. **Calculate target exit date:** Entry + 8-14 days
2. **Select expiration:** 7-14 days AFTER target exit date
3. **This gives you:** 15-28 DTE at entry, with buffer if trade takes longer

**Example:**
- Entry: January 15
- Target exit: January 25 (10 days later)
- Expiration: February 7 (23 days away)
- DTE at entry: 23 days ✓

- [ ] **DTE selected:** _____ days
- [ ] **Expiration date:** ____________

---

### A4.6 Pre-Entry Exit Planning

**Before clicking "buy," define these:**

**1. Profit Target(s):**

| Exit Level | Size | Trigger |
|------------|------|---------|
| **1st exit** | 33% of position | Hit 2R (2× risk) OR halfway to Fib target |
| **2nd exit** | 33% of position | Hit Fib target OR 3R |
| **Final exit** | Remaining 33% | Trail with stop OR asymmetry exhausted |

**2. Stop Loss:**

| Stop Type | Trigger | Action |
|-----------|---------|--------|
| **Technical** | Price closes back below breakout level | Close immediately |
| **Dollar** | -50% of premium OR CHF 300 loss | Close |
| **Time** | Day 21 if not profitable | Close or roll (+21 DTE) |

**3. Automatic Orders (Set at Entry):**

| Order | Price | Notes |
|-------|-------|-------|
| Limit sell (1/3) | Option price at 2× entry | First profit target |
| Limit sell (1/3) | Option price at Fib target | Second profit target |
| GTC (Good Till Cancelled) | | |

**Your JNJ trade used Black-Scholes to calculate sell prices:**
- Entry option price → calculate future option price at target spot → set limit orders
- This removes emotion from exit decision

- [ ] **Profit targets defined?**
  - 1st exit at: _______
  - 2nd exit at: _______
  - Final trailing stop: _______
- [ ] **Stop loss defined?** At: _______
- [ ] **Automatic orders to be placed?** ✓

---

## A5. ENTRY CHECKLIST SUMMARY

### Quick Validation (5 Minutes)

**A1. MACRO/SECTOR (1 minute):**
- [ ] A1.1 Market regime identified (Risk-on/Risk-off/Transitional)
- [ ] A1.2 Sector aligned with regime (TIER 1 sector?)
- [ ] A1.3 Not an overcrowded consensus trade

**A2. RISK (1 minute):**
- [ ] A2.1 Position risk ≤ CHF 600
- [ ] A2.2 Currency allocation checked (prioritize under-allocated currency)
- [ ] A2.3 Sector concentration OK (≤2-3 in same sector)
- [ ] A2.4 Within weekly risk budget

**A3. TECHNICAL (1 minute):**
- [ ] A3.1 Breakout confirmed (price action + Fib breach)
- [ ] A3.2 Target defined (Fib extension / measured move)
- [ ] A3.3 Momentum present (2+ indicators confirm)
- [ ] A3.4 Above/below relevant DMAs

**A4. OPTION PRICING (2 minutes):**
- [ ] A4.1 IV Percentile checked (<50% outright, >50% spread)
- [ ] A4.2 Structure selected (outright vs spread)
- [ ] A4.3 Delta 30-50 (not far OTM lottery ticket)
- [ ] A4.4 Spread strikes at technical levels (if applicable)
- [ ] A4.5 DTE 15-28 days
- [ ] A4.6 Exit plan defined (profit targets + stop loss)

**SCORING:**
- All boxes checked: **ENTER TRADE** ✓
- 1-2 boxes unchecked (minor): **Proceed with caution**
- 3+ boxes unchecked: **PASS ON TRADE** ✗

---

# SECTION B: MONITORING

## B1. DAILY QUICK CHECK (2 MINUTES)

**Run this at market close or before next morning:**

### B1.1 Status Dashboard

| Metric | Green ✓ | Yellow ⚠ | Red ✗ | Current |
|--------|---------|----------|-------|---------|
| **Days Held** | 0-14 | 15-21 | >21 | |
| **Price vs Breakout** | Above (call)/Below (put) | Testing breakout level | Broke back through | |
| **Fib Structure** | In extension zone | At target zone | Violated Fib zone | |
| **IV Movement** | Expanding/stable | Contracting slowly | Crushed >20% | |
| **P&L** | Profitable | -25% to +25% | Down >50% premium | |
| **Asymmetry** | Room to run | Nearing exhaustion | No asymmetry left | |

### B1.2 Action Matrix

| Status | Action |
|--------|--------|
| **All Green** | Hold, let it run, no action needed |
| **1 Yellow** | Monitor more closely tomorrow |
| **2 Yellow** | Prepare exit, tighten mental stop |
| **Any Red** | Execute red flag action IMMEDIATELY |

### B1.3 Red Flag Actions

| Red Flag | Immediate Action |
|----------|------------------|
| **Days >21** | Close position OR roll with +21 DTE extension |
| **Broke back through breakout** | Close immediately, thesis invalidated |
| **Violated Fib zone** | Close, trade is dead |
| **IV crushed >20%** | Reassess - close if spot also adverse |
| **Down >50% premium** | Check stop loss, likely close |
| **No asymmetry left** | Close, take profit |

---

## B2. WEEKLY REVIEW (FRIDAYS, 5 MINUTES)

**For EACH open BOT position, answer:**

### B2.1 Continuation Test

**Question 1: Would I enter this trade TODAY at current levels?**

| Answer | Action |
|--------|--------|
| **YES** | Hold through weekend |
| **NO** | Close Monday morning at open |
| **UNSURE** | Reduce position by 50% |

**Question 2: Has the thesis changed?**

- [ ] Sector rotation occurred (leadership changed)
- [ ] Macro narrative shifted (regime change)
- [ ] Technical structure broken (below breakout, Fib violated)
- [ ] Original catalyst expired or changed

**If ANY box checked → Close or reduce position**

### B2.2 Days Held Check

| Days Held | Action |
|-----------|--------|
| **<14 days** | OK to hold if technical intact |
| **14-21 days** | Review closely, prepare exit plan |
| **21+ days** | Close Monday OR roll with duration extension |

**Your data: 22-28 day holding = 22.2% WR (graveyard zone)**

### B2.3 Currency Exposure Review

**Recalculate currency allocation:**

| Currency | Target | Current | Gap | Action Needed |
|----------|--------|---------|-----|---------------|
| USD | 30-40% | ___% | | |
| EUR | 40-50% | ___% | | |
| CHF | 10-20% | ___% | | |

**If out of balance:** Prioritize next week's trades in under-allocated currency

---

## B3. IV MONITORING

### B3.1 IV Tracking

**For each position, track:**

| Metric | Entry | Current | Change | Concern Level |
|--------|-------|---------|--------|---------------|
| Stock IV | | | | |
| VIX (context) | | | | |

**IV Change Impact:**

| IV Change | Impact on Long Options | Action |
|-----------|------------------------|--------|
| **IV expanding** | Good - vega gain | Hold, consider taking profit |
| **IV stable** | Neutral | Continue holding |
| **IV contracting 5-10%** | Minor drag | Monitor closely |
| **IV contracting >15%** | Significant drag | Consider exit even if spot favorable |
| **IV crushed >20%** | Major damage | EXIT (your SPY loss: -$320 from IV alone) |

### B3.2 VIX-Specific Monitoring

**For CALLS:**
| VIX Move | Your Call Position | Action |
|----------|-------------------|--------|
| VIX rising sharply | May hurt (market stress) | Tighten stop, consider exit |
| VIX stable | Neutral | Continue |
| VIX falling from high | May help (risk-on) | Hold |

**For PUTS:**
| VIX Move | Your Put Position | Action |
|----------|-------------------|--------|
| VIX rising sharply | Helps (fear premium) | Take profits faster |
| VIX stable | Neutral | Continue |
| VIX falling | Hurts (fear subsiding) | Tighten stop |

---

# SECTION C: EXIT

## C1. PROFIT-TAKING EXITS

### C1.1 Automatic Profit Targets

**Set these at entry, execute automatically:**

| Exit Level | Trigger | Position Size | Notes |
|------------|---------|---------------|-------|
| **1st exit** | 2R (2× initial risk) | 33% | Lock in profit |
| **2nd exit** | Fib target reached | 33% | Technical completion |
| **3rd exit** | Asymmetry exhausted | 34% (remainder) | Trailing stop |

**2R Calculation:**
- Initial risk (premium paid): CHF 500
- 2R = CHF 1,000 gain (option now worth CHF 1,500)
- Action: Sell 1/3 of position

### C1.2 Technical Profit Exits

**Exit when price reaches:**

| Technical Level | Action | Reasoning |
|-----------------|--------|-----------|
| **Fib 1.0 extension** | Take 1/3 profit | First target reached |
| **Fib 1.272 extension** | Take 1/3 profit | Second target |
| **Fib 1.618 extension** | Close remainder OR trail | Maximum target |
| **Prior swing high/low** | Consider exit | Natural resistance/support |

### C1.3 Asymmetry-Based Exit

**Your most profitable exit signal from actual trades:**

> "Break out is over here as we are in the target zone and no asymmetry any more." (GLD +$1,692)

> "Close the 3rd piece of the trade as planned - before Friday evening as no asymmetry any more" (SLV +$1,633)

**What "no asymmetry" means:**
- Target zone reached (limited upside remaining)
- Risk/reward now unfavorable
- Easy money has been made
- Market structure suggests exhaustion

**Rule:** When you recognize asymmetry is gone, EXIT IMMEDIATELY. Don't wait for "a little more."

### C1.4 Time-Based Profit Exit

**If profitable and approaching Day 21:**
- Take all profits
- Don't let a winner become a loser in the graveyard zone

---

## C2. STOP LOSS EXITS

### C2.1 Technical Stops

| Trigger | Action | Reasoning |
|---------|--------|-----------|
| **Price closes below breakout level (calls)** | Close immediately | Breakout failed |
| **Price closes above breakout level (puts)** | Close immediately | Breakout failed |
| **Fib zone violated** | Close immediately | Structure broken |
| **DMA cross against** | Close or tighten stop | Trend changing |

**Your lesson (GM trade):** "Broke out of fib on upside - breakout trade is dead."

### C2.2 Dollar Stops

| Trigger | Action |
|---------|--------|
| **-50% of premium** | Mandatory close (unless technical intact) |
| **-CHF 300** | Hard stop (half of max risk) |
| **-CHF 600** | Absolute maximum - should never reach if managing properly |

### C2.3 Time Stops

| Days Held | If Profitable | If Not Profitable |
|-----------|---------------|-------------------|
| **Day 14** | Continue | Review position closely |
| **Day 18** | Take partial profits | Prepare to close |
| **Day 21** | Take all profits | **MANDATORY CLOSE OR ROLL** |

**Your data: 22-28 days = 22.2% WR**
**Rule: Day 21 is the deadline. No exceptions without rolling duration.**

---

## C3. MANUAL/DISCRETIONARY EXITS

### C3.1 Discipline Breakdown Signals

**Close IMMEDIATELY when you notice:**

- [ ] "I should probably close this" (you know, act on it)
- [ ] Feeling "lazy" about managing the trade
- [ ] Avoiding looking at the position
- [ ] Rationalizing why to hold despite signals

**Your lesson (C trade -$324):** "Should have been closed earlier. I have been lazy on this one."

**Rule:** When you "know" you should close, you should close.

### C3.2 Repositioning Rule

**NEVER reposition strike without extending duration**

| Scenario | Bad Action | Good Action |
|----------|------------|-------------|
| Strike now far OTM | Roll to closer strike, same expiry | Close OR roll strike + extend 21+ days |
| Need more time | Keep same strike, roll to next month | OK if adding 21+ DTE |
| Strike overshot | Roll to capture more upside | Just close, take profit |

**Your lesson (USO trade -$507):** "In retrospect it is not worth trying to reposition in strike if not in duration as well - as it is then a new trade."

### C3.3 Sector/Macro Shift Exit

**Close when:**

- Sector rotation evident (your sector losing leadership)
- Macro regime changed (Risk-on → Risk-off or vice versa)
- Correlation breakdown (your stock diverging from sector)

---

## C4. EXIT CHECKLIST SUMMARY

### Before ANY Exit, Confirm:

**For Profit Exits:**
- [ ] Has technical target been reached?
- [ ] Is asymmetry exhausted?
- [ ] Am I at 2R or better?
- [ ] Is Day 21 approaching?
- [ ] Have I followed scaling plan (1/3, 1/3, 1/3)?

**For Stop Loss Exits:**
- [ ] Has technical structure broken?
- [ ] Is position down >50% of premium?
- [ ] Has IV crushed while spot adverse?
- [ ] Is Day 21+ without profit?

**For Discretionary Exits:**
- [ ] Do I "know" I should close?
- [ ] Has my thesis changed?
- [ ] Would I enter this trade today?

---

# QUICK REFERENCE CARD

```
╔══════════════════════════════════════════════════════════════════╗
║                BOT COMPREHENSIVE CHECKLIST                       ║
╠══════════════════════════════════════════════════════════════════╣
║ A. ENTRY (5 min)                                                 ║
║ ─────────────────                                                ║
║ □ Macro: Regime identified, sector aligned                       ║
║ □ Risk: ≤CHF 600, currency balanced, sector not concentrated    ║
║ □ Technical: Breakout confirmed, Fib target defined, momentum   ║
║ □ Option: IV%ile checked, delta 30-50, DTE 15-28                ║
║ □ Structure: Outright (IV<50%) or Spread (IV>50%)               ║
║ □ Exit plan: Targets + stops defined BEFORE entry               ║
║                                                                  ║
║ B. MONITORING (2 min daily)                                      ║
║ ──────────────────────────                                       ║
║ □ Days held <21?                                                 ║
║ □ Price still above/below breakout?                              ║
║ □ Fib structure intact?                                          ║
║ □ IV stable or expanding?                                        ║
║ □ Would I enter today?                                           ║
║                                                                  ║
║ C. EXIT                                                          ║
║ ────────                                                         ║
║ PROFIT: 2R → 1/3 | Fib target → 1/3 | Trail → remainder         ║
║ STOP: -50% premium | Breakout violated | Day 21 unprofitable    ║
║ RULE: When you "know" → ACT IMMEDIATELY                         ║
║                                                                  ║
║ FORBIDDEN                                                        ║
║ ─────────                                                        ║
║ ✗ Delta <20 (lottery tickets)                                   ║
║ ✗ Index options when VIX >20                                    ║
║ ✗ Reposition strike without +21 DTE                             ║
║ ✗ Hold past Day 21 without rolling                              ║
║ ✗ Hold from laziness when you "know"                            ║
╚══════════════════════════════════════════════════════════════════╝
```

---

**Document Version:** 1.0
**Based on:** 279 BOT trades analysis, multi-strategy portfolio framework, currency risk management
**Last Updated:** January 2026
