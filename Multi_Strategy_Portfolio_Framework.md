# MULTI-STRATEGY OPTIONS PORTFOLIO FRAMEWORK
**For CHF-Based Investor | IBKR with Eurex Access**

---

## YOUR ACTUAL TRADING STRATEGIES

### Strategy 1: BOT (Breakout Trades)
- **Type:** Directional long options (calls/puts)
- **Duration:** 8-14 days typical holding period
- **Entry:** 15-28 DTE
- **Capital:** Premium paid upfront (~CHF 500-800 per trade)
- **Risk:** Limited to premium paid
- **Cash requirement:** LOW (just premium)

### Strategy 2: Short Puts (Mean Reversion)
- **Type:** Sell 20 delta puts, buy 5 delta puts (defined risk spread)
- **Duration:** 45 DTE at entry, close at 21 DTE or 50% profit
- **Capital:** Collateral for width of spread
- **Risk:** Defined (max = spread width - premium received)
- **Cash requirement:** HIGH (need cash if assigned)
- **Example:** Sell SAP €220 put, buy €200 put
  - Max risk: €20 × 100 - premium = ~€1,800 per spread
  - Assignment risk: €22,000 cash needed if stock assigned

### Strategy 3: Strangles (Volatility Collection)
- **Type:** Sell both 20 delta call + 20 delta put
- **Duration:** 10-30 DTE
- **Capital:** Margin/collateral for both sides
- **Risk:** Undefined (can be assigned on either side)
- **Cash requirement:** VERY HIGH (need cash for potential assignment)
- **Example:** Sell SAP €240 call + €200 put (stock at €220)
  - Assignment risk: €24,000 (call) or €20,000 (put) cash needed

---

## CASH ALLOCATION BY STRATEGY

### Current Portfolio: CHF 104,100

**Current Allocation:**
- CHF: 69.6% (CHF 72,510 - mostly cash)
- USD: 25.9% ($33,904 = CHF ~29,850)
- EUR: 11.7% (€13,169 = CHF ~12,640)

**Why 70% Cash is NOT Excessive:**
- Short puts require cash collateral
- Strangles require cash for assignment
- New year reset (closed 2024 positions)
- **1.1% CHF inflation** (low opportunity cost vs 2.1% in 2023)

---

### Revised Cash Requirements by Strategy

**For Multi-Strategy Portfolio (10-15 total positions):**

| Strategy | Positions | Capital Type | CHF Required | % of Portfolio |
|----------|-----------|--------------|--------------|----------------|
| **BOT Trades** | 5-7 | Premium | CHF 3,500-5,600 | 3-5% |
| **Short Put Spreads** | 3-5 | Collateral | CHF 5,400-9,000 | 5-9% |
| **Strangles** | 2-3 | Collateral | CHF 12,000-18,000 | 12-17% |
| **Reserve Cash** | - | Buffer | CHF 20,000-30,000 | 20-30% |
| **Total Deployed** | 10-15 | | CHF 40,900-62,600 | 40-60% |

**Recommended Allocation:**
- **Deployed Capital:** 50-60% (CHF 52,000-62,000)
  - BOT: 5% (~CHF 5,000 in premiums)
  - Short puts: 10-15% (~CHF 10,000-15,000 collateral)
  - Strangles: 15-20% (~CHF 15,000-20,000 collateral)
  - T-Bills/Hedges: 10-15% (~CHF 10,000-15,000)
- **Reserve Cash:** 40-50% (CHF 42,000-52,000)
  - For assignment risk
  - For new opportunities
  - Safety buffer

**Your current 70% cash is defensible, but can deploy another CHF 10,000-20,000**

---

## CURRENCY ALLOCATION BY STRATEGY

### BOT Trades (5-7 positions, CHF 5,000 total premium)

**Currency split:**
- USD: 40-50% (2-3 BOT positions, CHF 2,000-2,500)
- EUR: 30-40% (2-3 BOT positions, CHF 1,500-2,000)
- CHF: 10-20% (1 BOT position, CHF 500-1,000)

**Why:** BOT is short-term (8-14 days), high turnover, need liquidity
- USD has best liquidity
- EUR needed for hedge
- CHF for base currency exposure

---

### Short Put Spreads (3-5 positions, CHF 10,000-15,000 collateral)

**Currency split:**
- USD: 30-40% (1-2 positions, CHF 3,000-6,000)
- EUR: 40-50% (2-3 positions, CHF 4,000-7,500)
- CHF: 10-20% (0-1 position, CHF 1,000-3,000)

**Why:** Short puts = willing to own stock, longer duration (45 DTE)
- **EUR emphasis** because 30% of your expenses are EUR
- If assigned EUR stock (SAP, Siemens), you're long EUR = hedges EUR expenses
- EUR stocks less correlated to USD macro
- CHF stocks for base currency

**Key:** Only sell puts on stocks you WANT to own at strike price
- EUR: SAP, Siemens, ASML, TotalEnergies, Airbus
- CHF: Novartis, UBS, ABB
- USD: AAPL, MSFT, WMT, JNJ

---

### Strangles (2-3 positions, CHF 15,000-20,000 collateral)

**Currency split:**
- USD: 40-50% (1-2 strangles, CHF 6,000-10,000)
- EUR: 30-40% (1 strangle, CHF 4,500-8,000)
- CHF: 10-20% (0-1 strangle, CHF 1,500-4,000)

**Why:** Strangles = undefined risk, need highest quality/liquidity
- USD: Largest options market, tightest spreads
- EUR: Need high IV + liquid options (ASML, SAP)
- CHF: Limited strangle opportunities (Swiss market smaller)

**Key:** Only strangles on stocks with:
- High IV (volatility to collect)
- Tight option spreads (<3%)
- You're willing to own OR short (assignment both sides)

---

### Total Currency Allocation (All Strategies Combined)

**Target Allocation:**

| Currency | BOT | Short Puts | Strangles | Total Target | Your Current | Gap |
|----------|-----|------------|-----------|--------------|--------------|-----|
| **USD** | CHF 2,250 | CHF 4,500 | CHF 8,000 | **CHF 14,750** (28%) | CHF 29,850 (29%) | ✓ OK |
| **EUR** | CHF 1,750 | CHF 6,000 | CHF 6,000 | **CHF 13,750** (26%) | CHF 12,640 (12%) | **Need +CHF 1,000** |
| **CHF** | CHF 750 | CHF 2,000 | CHF 2,000 | **CHF 4,750** (9%) | CHF 72,510 (70%) | Way over (cash) |

**Plus Reserve Cash:** CHF 45,000-50,000 (for assignment, opportunities)

**Revised Assessment:**
- USD: 29% current vs 28% target = ✓ **Perfectly balanced**
- EUR: 12% current vs 26% target = **Need +CHF 1,000-2,000 EUR deployed**
- CHF: 70% current vs 54% total (9% deployed + 45% reserve) = **CHF 15,000 excess cash**

**Not as bad as I first thought! You mainly need:**
1. Deploy CHF 1,000-2,000 into EUR positions (short puts or BOT)
2. Optionally deploy CHF 10,000-15,000 excess cash into strategies

---

## EUR STOCK UNIVERSE BY STRATEGY

### For SHORT PUTS (Quality Stocks You Want to Own)

**Criteria:**
- Strong balance sheet (can weather downturn)
- Stable or growing business
- Good liquidity
- You're willing to hold long-term if assigned

**TIER 1 - Best EUR Stocks for Put Selling:**

| Stock | Price | Sector | Why Sell Puts | Risk |
|-------|-------|--------|---------------|------|
| **SAP** | €220-240 | Tech | Enterprise software moat, stable | ✓ Low |
| **Siemens** | €180-200 | Industrial | German industrial leader, dividend | ✓ Low |
| **ASML** | €900 | Tech | Chip equipment monopoly | ⚠ High price, tech cyclical |
| **TotalEnergies** | €60-65 | Energy | Integrated oil, dividend, €-denominated | ✓ Low |
| **Airbus** | €160-170 | Aerospace | Duopoly with Boeing, order backlog | ✓ Low |
| **Schneider Electric** | €220-240 | Industrial | Electrification trend | ✓ Low |

**Example Short Put Trade (SAP):**
- Stock: €230 (current)
- **Sell:** SAP €210 put, 45 DTE (20 delta) → Collect €4.50 premium
- **Buy:** SAP €190 put, 20 DTE (5 delta) → Pay €0.80 premium
- **Net credit:** €3.70 per share = €370 per spread
- **Max risk:** (€210 - €190) - €3.70 = €16.30 = **€1,630** collateral needed
- **Assignment risk:** If SAP drops below €210, you own SAP at €210
  - Need €21,000 cash per contract (if not using spread)

---

### For STRANGLES (High IV, Liquid Options)

**Criteria:**
- High implied volatility (premium to collect)
- Tight bid-ask spreads (<3%)
- You're willing to own OR short the stock
- Stable range-bound or earnings volatility

**TIER 1 - Best EUR Stocks for Strangles:**

| Stock | IV Rank | Options Liquidity | Why Strangle | Avoid If |
|-------|---------|-------------------|--------------|----------|
| **ASML** | Medium-High | Excellent | Tech volatility, earnings | Breaking out strongly |
| **SAP** | Medium | Very Good | Software, stable range | Trending strongly |
| **Siemens** | Low-Medium | Good | Industrial, dividend support | Low IV = low premium |
| **TotalEnergies** | Medium | Good | Oil volatility, range-bound | Oil spiking/crashing |
| **LVMH** | Medium | Good | Luxury, China exposure vol | Strong trend either way |

**Example Strangle (SAP €230 current):**
- **Sell:** SAP €250 call, 20 DTE (20 delta) → €3.50
- **Sell:** SAP €210 put, 20 DTE (20 delta) → €3.80
- **Total credit:** €7.30 per share = €730 per strangle
- **Profit zone:** Stock stays between €202.70 - €257.30 at expiration
- **Assignment risk:** Need €25,000 (call) or €21,000 (put) cash

---

### For BOT (Momentum, Breakouts)

**Same as before:**
- SAP, ASML, Siemens, TotalEnergies, Airbus, Deutsche Telekom, Infineon

**Different mindset:**
- BOT: Want momentum, trending, breaking out
- Short puts: Want mean reversion, support levels, oversold
- Strangles: Want range-bound, high IV, stable

**Same stocks, different strategies at different times!**

---

## CHF STOCK UNIVERSE BY STRATEGY

### For SHORT PUTS (Quality Swiss Stocks)

**TIER 1:**

| Stock | Price | Sector | Why Sell Puts | Quality |
|-------|-------|--------|---------------|---------|
| **Novartis** | CHF 90-95 | Pharma | Defensive, dividend, stable | ⭐⭐⭐ |
| **Roche** | CHF 270-280 | Pharma | Quality, healthcare moat | ⭐⭐⭐ |
| **UBS** | CHF 27-30 | Banking | Post-CS acquisition, growth | ⭐⭐ |
| **ABB** | CHF 50-55 | Industrial | Automation, electrification | ⭐⭐ |
| **Nestlé** | CHF 85-90 | Consumer | **WAIT** - In bear market, but bottoming? | ⚠ |

**Nestlé consideration:**
- Down from CHF 120 to CHF 85 (29% decline)
- **Could be opportunity for SHORT PUTS if bottoming**
- Sell CHF 80 put, 45 DTE = collect premium on quality name
- IF assigned at CHF 80, you own Nestlé 33% below highs
- **Only if you believe bottom is in**

---

### For STRANGLES (CHF Stocks)

**Limited opportunities (Swiss market smaller, lower IV):**

| Stock | IV | Liquidity | Strangle Viability |
|-------|----|-----------|--------------------|
| **UBS** | Medium | Good | ✓ Possible (post-CS volatility) |
| **Novartis** | Low | Good | ⚠ Low IV, low premium |
| **Roche** | Low | Medium | ⚠ Low IV |
| **ABB** | Low-Medium | Medium | ⚠ Limited |

**Recommendation:** Focus strangles on USD (best liquidity) and EUR (decent liquidity)

---

## POSITION SIZING BY STRATEGY

### BOT Trades (Premium Risk)

**Standard BOT position:**
- Premium: CHF 500-800 per trade
- Contracts: Depends on underlying price
  - €50-150 stocks: 3-5 contracts
  - €700-900 stocks: 1-2 contracts
- **Total BOT allocation:** 5-7 positions = CHF 3,500-5,600

---

### Short Put Spreads (Collateral Risk)

**Standard put spread:**
- Width: €20-30 or CHF 20-30 (strike difference)
- Net credit: €3-5 or CHF 3-5
- Max risk: €15-25 or CHF 15-25 per spread = **€1,500-2,500 per spread**
- **Total put allocation:** 3-5 spreads = CHF 5,400-9,000

**If selling naked puts (cash-secured):**
- Stock price × 100 = cash needed
- SAP €230 naked put = €23,000 cash needed
- **Much higher capital requirement**
- Safer: Use spreads (defined risk)

---

### Strangles (Margin/Collateral Risk)

**Standard strangle:**
- Stock price: €200-300 or CHF 50-100
- Strikes: ±10-15% from current price
- Credit: €6-10 or CHF 6-10 per strangle
- Margin: Stock price × 100 × 0.20 (typical) = **€4,000-6,000 per strangle**
- **Total strangle allocation:** 2-3 strangles = CHF 12,000-18,000

**Assignment risk much higher:**
- If breaches either strike, assigned
- Need full cash to buy stock (put side) or short stock (call side)
- Keep 2-3× margin as reserve cash

---

## REVISED DEPLOYMENT PLAN

### Current State

| Currency | Current | Breakdown |
|----------|---------|-----------|
| CHF | CHF 72,510 (70%) | 100% cash |
| USD | CHF 29,850 (29%) | $2,013 cash + $31,892 positions (unrealized -$371) |
| EUR | CHF 12,640 (12%) | €7,155 cash + €6,015 positions (unrealized -€141) |

**Total:** CHF 104,100

---

### Target State (Multi-Strategy)

**Strategy Allocation:**

| Strategy | Positions | CHF Capital | USD | EUR | CHF |
|----------|-----------|-------------|-----|-----|-----|
| **BOT** | 5-7 | CHF 5,000 | 2-3 | 2-3 | 1 |
| **Short Puts** | 3-5 | CHF 10,000 | 1-2 | 2-3 | 0-1 |
| **Strangles** | 2-3 | CHF 15,000 | 1-2 | 1 | 0-1 |
| **T-Bills + FX Hedge** | - | CHF 10,000 | ✓ | | |
| **Reserve Cash** | - | CHF 45,000 | | | |
| **Total** | 10-15 | **CHF 85,000** | | | |

**Currency Breakdown:**

| Currency | Deployed | Reserve | Total | % |
|----------|----------|---------|-------|---|
| **USD** | CHF 15,000 | CHF 15,000 | CHF 30,000 | 29% |
| **EUR** | CHF 14,000 | CHF 8,000 | CHF 22,000 | 21% |
| **CHF** | CHF 5,000 | CHF 22,000 | CHF 27,000 | 26% |
| **T-Bills** | CHF 10,000 | - | CHF 10,000 | 10% |
| **Cash Reserve** | - | CHF 15,000 | CHF 15,000 | 14% |
| **Total** | CHF 44,000 | CHF 60,000 | **CHF 104,100** | 100% |

---

### Deployment Actions

**You're closer than I thought! Main need:**

1. **EUR: Deploy CHF 1,000-2,000 more**
   - Current: CHF 12,640 (12%)
   - Target: CHF 14,000-22,000 (13-21%)
   - **Action:** Add 1-2 EUR positions (short put or BOT)

2. **USD: Maintain current level**
   - Current: CHF 29,850 (29%)
   - Target: CHF 30,000 (29%)
   - **Action:** None needed (perfect!)

3. **CHF: Deploy CHF 5,000-10,000 from excess cash**
   - Current: CHF 72,510 (70%)
   - Target: CHF 45,000-50,000 reserve (43-48%)
   - **Action:** Deploy CHF 10,000-15,000 into strategies

**Total Deployment Needed: CHF 10,000-20,000**
- EUR: +CHF 2,000
- Mixed (USD/EUR/CHF): +CHF 8,000-18,000 across strategies

**Much less aggressive than my first recommendation!**

---

## THIS WEEK: PRACTICAL ACTIONS

### Monday-Tuesday: Plan

1. **Scan for EUR short put opportunities:**
   - SAP: Below €220? (support level)
   - Siemens: Below €180? (support level)
   - TotalEnergies: Below €60? (support level)

2. **Scan for BOT setups (all currencies):**
   - USD: AAPL, GLD, NFLX, WMT breaking out?
   - EUR: SAP, ASML, Siemens breaking out?
   - CHF: Novartis, UBS, ABB breaking out?

3. **Check IV for strangle opportunities:**
   - Which stocks have elevated IV?
   - ASML earnings coming? (IV spike)
   - SAP range-bound? (good strangle)

---

### Wednesday-Friday: Execute

**Deploy CHF 10,000-15,000:**

**Option A: Conservative (Add 3-4 positions)**
- 1 EUR short put (SAP or TotalEnergies) = CHF 2,000 collateral
- 2 BOT trades (1 EUR, 1 USD) = CHF 1,200 premium
- 1 Strangle (USD or EUR, depending on IV) = CHF 6,000 margin
- **Total: CHF 9,200**

**Option B: Balanced (Add 4-6 positions)**
- 2 EUR short puts (SAP + TotalEnergies) = CHF 4,000 collateral
- 3 BOT trades (2 EUR, 1 CHF) = CHF 1,800 premium
- 1 Strangle (ASML or SAP) = CHF 6,000 margin
- **Total: CHF 11,800**

**Option C: Aggressive (Add 6-8 positions)**
- 3 EUR short puts = CHF 6,000 collateral
- 4 BOT trades = CHF 2,400 premium
- 2 Strangles = CHF 12,000 margin
- **Total: CHF 20,400**

**Recommendation:** Start with **Option A or B** (conservative/balanced)
- You just reset for new year
- Test EUR liquidity first
- Build positions gradually over 2-4 weeks

---

## STRATEGY-SPECIFIC RULES

### Short Put Rules

1. **Only sell puts on stocks you want to own at strike price**
   - If SAP €210 put assigned, are you happy owning SAP at €210?
   - If YES → Sell the put
   - If NO → Don't sell

2. **Sell at support levels:**
   - Previous lows
   - Fibonacci retracement levels
   - Round numbers (€200, €100, CHF 50)

3. **Duration: 45 DTE entry, close at 21 DTE or 50% profit**
   - Theta decay accelerates after 21 DTE
   - 50% profit in <24 days = excellent return

4. **Use spreads for defined risk:**
   - Sell 20 delta put (45 DTE)
   - Buy 5 delta put (20 DTE or same expiration)
   - Width = max loss you accept (€20-30 typical)

5. **Currency consideration:**
   - EUR puts = willing to own EUR stocks
   - Good for you (30% EUR expenses)
   - Assignment = long EUR hedge

---

### Strangle Rules

1. **Only in range-bound, high IV environments:**
   - IV rank >50% (elevated volatility)
   - Stock not trending strongly
   - Tight option spreads

2. **Duration: 10-30 DTE**
   - Sweet spot: 20 DTE
   - Close at 50% profit or 7 DTE (whichever first)

3. **Position sizing: Small**
   - Undefined risk = position can move against you fast
   - Max 2-3 strangles at once
   - Keep 3× margin as reserve cash

4. **Avoid during:**
   - Strong trends (will breach one side)
   - Low IV (not enough premium)
   - Earnings (unless intentional earnings strangle)

---

### BOT + Short Put Coordination

**Can use same stock, different strategies:**

**Example: SAP**
- **Scenario 1:** SAP at €230, consolidating
  - Action: Sell €210 put (mean reversion bet)
  - If drops to €210, collect premium

- **Scenario 2:** SAP breaks above €240 resistance
  - Action: Buy €245 call (BOT trade)
  - Ride the breakout momentum

- **Scenario 3:** SAP at €230, high IV, range-bound
  - Action: Sell €250 call + €210 put strangle
  - Collect premium from volatility

**Different market conditions = different strategies on same stock!**

---

## EUR STOCK RECOMMENDATION SUMMARY

### For ALL Strategies (Short Puts, BOT, Strangles)

**TIER 1 - Trade Frequently:**

| Stock | Price | BOT | Short Puts | Strangles | IBKR Liquidity |
|-------|-------|-----|------------|-----------|----------------|
| **SAP** | €220-240 | ✓✓ | ✓✓✓ | ✓✓ | Excellent |
| **ASML** | €900 | ✓✓✓ | ✓✓ | ✓✓✓ | Excellent |
| **Siemens** | €180-200 | ✓✓ | ✓✓✓ | ✓ | Very Good |
| **TotalEnergies** | €60-65 | ✓✓ | ✓✓✓ | ✓✓ | Good |

**TIER 2 - Selective Use:**

| Stock | Price | BOT | Short Puts | Strangles | Notes |
|-------|-------|-----|------------|-----------|-------|
| Airbus | €160-170 | ✓✓ | ✓✓ | ✓ | Aerospace cycle |
| Schneider Electric | €220-240 | ✓ | ✓✓ | ✓ | Electrification |
| Deutsche Telekom | €25-27 | ✓ | ✓✓ | ⚠ | Low IV |
| Infineon | €30-35 | ✓ | ✓ | ✓ | Semiconductor cycle |
| LVMH | €700 | ✓ | ✓ | ✓✓ | Luxury, China exposure |

**Start with TIER 1 (SAP, ASML, Siemens, TotalEnergies)**

---

## FINAL RECOMMENDATION

### Your Situation is Actually Good!

**Current allocation:**
- USD: 29% ✓ (perfect)
- EUR: 12% (need +2-5%)
- CHF: 70% (high, but justified for multi-strategy)

**Cash needs:**
- Short puts: Collateral
- Strangles: Margin + assignment risk
- Reserve: Safety buffer
- **70% cash is defensible given your strategies**

**Inflation cost:**
- CHF inflation: 1.1% (very low)
- Holding CHF cash: -1.1%/year opportunity cost
- **Not urgent to deploy all cash**

---

### Immediate Actions (This Week)

1. **Add 1-2 EUR positions (CHF 2,000-4,000):**
   - **Short put:** SAP €210 put spread (if at support)
   - **BOT:** ASML call (if breaking out)
   - **Priority: EUR to hedge USD**

2. **Add 2-3 other positions (CHF 6,000-10,000):**
   - 1-2 USD BOT or strangles
   - 0-1 CHF position (Novartis short put or BOT)

3. **Total deployment: CHF 8,000-14,000**
   - Brings cash from 70% to 60-65%
   - EUR from 12% to 15-18%
   - Maintains reserves for assignment

---

### Questions for Refinement

1. **What's your target # of positions?**
   - Currently planning 10-15 total
   - Do you prefer 15-20 smaller positions?
   - Or 8-12 larger positions?

2. **Short put preference:**
   - Spreads (defined risk) or naked (cash-secured)?
   - Width of spreads (€20, €30, €50)?

3. **Strangle preference:**
   - How many strangles typically open at once?
   - Preferred duration (10, 20, or 30 DTE)?

4. **Nestlé:**
   - Interested in selling puts at CHF 80 (bottom fishing)?
   - Or avoid until confirms bottom?

5. **EUR stock preferences:**
   - SAP (tech) vs Siemens (industrial) vs TotalEnergies (energy)?
   - Which sectors do you want EUR exposure in?

**Your setup is more sophisticated than typical retail. Just need minor EUR rebalancing!**
