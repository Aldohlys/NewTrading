# BOT STRATEGY - CURRENCY RISK MANAGEMENT FRAMEWORK
**For CHF-Based Investor Trading Global Markets**

---

## THE CURRENCY RISK PROBLEM

### Your Situation

**Base Currency:** Swiss Francs (CHF)
- Wealth, income, most expenses in CHF
- Some expenses in EUR (European travel, etc.)
- Living in Geneva, Switzerland

**Trading Vehicle:** US Dollars (USD)
- US stocks traded in USD
- Options priced in USD
- But you don't want USD wealth - just using it for trading

**The Risk:**
Even if your BOT trade wins, you can lose money in CHF terms due to currency moves.

---

### Currency Risk Example (Real Scenario)

**Trade Setup:**
- Buy AAPL call for $500 (equivalent to CHF 450 at USD/CHF 0.90)
- Position size: $10,000 total USD exposure across portfolio
- Trade duration: 14 days (typical BOT)

**Scenario 1: Trade Wins BUT USD Weakens**

| Event | USD Value | USD/CHF Rate | CHF Value |
|-------|-----------|--------------|-----------|
| Entry | $500 premium | 0.90 | CHF 450 |
| Exit (14 days) | $1,200 profit (+140%) | 0.85 (-5.5%) | CHF 1,020 |
| **Without FX impact** | +$700 | 0.90 (stable) | **CHF 630** |
| **With FX impact** | +$700 | 0.85 (weaker USD) | **CHF 595** |
| **FX Loss** | - | -5.5% | **-CHF 35 (5.5% of profit!)** |

**Net result:** Made +$700 on trade, but lost CHF 35 to currency (kept CHF 595 of CHF 630 potential)

**On full $10,000 portfolio:**
- USD profit: +$700
- FX loss on total exposure: $10,000 × 5.5% = -$550
- **Net in CHF:** +$150 instead of +$700 (78% of profit lost to FX!)

---

**Scenario 2: Trade Loses AND USD Weakens (Double Hit)**

| Event | USD Value | USD/CHF Rate | CHF Value |
|-------|-----------|--------------|-----------|
| Entry | $500 premium | 0.90 | CHF 450 |
| Exit (loss) | $0 (expired worthless) | 0.85 | CHF 0 |
| **Without FX impact** | -$500 | 0.90 (stable) | **-CHF 450** |
| **With FX impact** | -$500 | 0.85 (weaker USD) | **-CHF 588** |
| **FX Loss ADDED** | - | -5.5% | **-CHF 138 extra pain** |

You lost the trade AND lost more in CHF terms because USD weakened!

---

**Scenario 3: Trade Wins AND USD Strengthens (Double Win!)**

| Event | USD Value | USD/CHF Rate | CHF Value |
|-------|-----------|--------------|-----------|
| Entry | $500 premium | 0.90 | CHF 450 |
| Exit (win) | $1,200 profit | 0.95 (+5.5%) | CHF 1,140 |
| **Without FX impact** | +$700 | 0.90 (stable) | **CHF 630** |
| **With FX impact** | +$700 | 0.95 (stronger USD) | **CHF 665** |
| **FX Gain ADDED** | - | +5.5% | **+CHF 35 bonus!** |

This is what you want - trade profit + currency tailwind!

---

### Historical USD/CHF Volatility

**Recent moves (2023-2025):**
- USD/CHF range: 0.83 - 0.95 (14% range)
- Average 2-week move: 1-2%
- Extreme 2-week move: 3-5% (SNB intervention, Fed pivots)

**For your 8-14 day BOT trades:**
- Expected FX impact: 1-2% on total USD exposure
- Extreme FX impact: 3-5%

**On a $10,000 USD portfolio:**
- Typical 2-week FX risk: CHF 100-200
- Extreme 2-week FX risk: CHF 300-500

This is NOT negligible - it's 20-100% of a typical BOT trade profit!

---

## THE SOLUTION: CURRENCY-BALANCED PORTFOLIO

### Strategy 1: Natural Currency Hedge

**Concept:** Balance USD exposure with EUR and CHF trades

**Target Allocation:**

| Currency | % of Portfolio | Rationale |
|----------|----------------|-----------|
| **USD** | 40-50% | Largest, most liquid options market |
| **EUR** | 30-40% | Hedge USD, covers EUR expenses |
| **CHF** | 10-20% | Base currency, limited liquid options |

**Why this works:**
- USD and EUR often move inversely vs CHF
- When USD weakens vs CHF, EUR often weakens less (or strengthens)
- CHF exposure provides base currency anchor
- Diversifies currency risk across 3 major currencies

---

### Strategy 2: Directional Currency Overlay

**Concept:** Adjust currency exposure based on macro FX view

**If you expect USD to strengthen vs CHF:**
- Increase USD allocation to 60-70%
- Reduce EUR/CHF allocation
- Benefit from both trade profit + FX tailwind

**If you expect USD to weaken vs CHF:**
- Decrease USD allocation to 30-40%
- Increase EUR/CHF allocation to 60-70%
- Reduce FX headwind

**If uncertain on USD/CHF:**
- Maintain balanced 40% USD / 40% EUR / 20% CHF
- FX movements offset each other

---

### Strategy 3: Position Sizing by Currency Exposure

**Track TOTAL currency exposure, not just number of trades**

**Example: 10 open BOT positions**

| Position | Security | Currency | Size | CHF Equivalent |
|----------|----------|----------|------|----------------|
| 1 | AAPL call | USD | $500 | CHF 450 |
| 2 | GLD call | USD | $400 | CHF 360 |
| 3 | NFLX call | USD | $600 | CHF 540 |
| 4 | WMT call | USD | $300 | CHF 270 |
| 5 | ASML call | EUR | €500 | CHF 540 |
| 6 | LVMH call | EUR | €400 | CHF 432 |
| 7 | SAP call | EUR | €350 | CHF 378 |
| 8 | Novartis call | CHF | CHF 600 | CHF 600 |
| 9 | Roche call | CHF | CHF 450 | CHF 450 |
| 10 | UBS call | CHF | CHF 300 | CHF 300 |

**Currency Exposure:**
- USD: $1,800 = CHF 1,620 (36%)
- EUR: €1,250 = CHF 1,350 (30%)
- CHF: CHF 1,350 (30%)
- **Total: CHF 4,320**

**Balanced! ✓**

---

## EUR/CHF TRADING UNIVERSE FOR BOT

### European Securities (EUR-Denominated)

#### TIER 1 - High Priority EUR Additions

**Technology:**

| Ticker | Company | Exchange | Market Cap | Why Trade |
|--------|---------|----------|------------|-----------|
| **ASML** | ASML Holding | Amsterdam (Euronext) | €300B+ | Semiconductor equipment monopoly, strong trends |
| **SAP** | SAP SE | Frankfurt (XETRA) | €180B+ | Enterprise software, clean breakouts |
| **ADYEN** | Adyen NV | Amsterdam | €40B+ | Payments (like your V winner) |

**Healthcare/Pharma:**

| Ticker | Company | Exchange | Market Cap | Why Trade |
|--------|---------|----------|------------|-----------|
| **NVO** (US ADR) | Novo Nordisk | Copenhagen/NYSE | $400B+ | Obesity drugs, massive momentum |
| **SAN** | Sanofi | Paris (Euronext) | €110B+ | Pharma, like your ABBV |

**Luxury/Consumer:**

| Ticker | Company | Exchange | Market Cap | Why Trade |
|--------|---------|----------|------------|-----------|
| **MC** (US ADR) | LVMH | Paris/NYSE | €350B+ | Luxury leader, strong trends |
| **RMS** | Hermès | Paris (Euronext) | €200B+ | Ultra-luxury, quality |
| **ITX** | Inditex (Zara) | Madrid | €120B+ | Fast fashion, like WMT consistency |

**Energy:**

| Ticker | Company | Exchange | Market Cap | Why Trade |
|--------|---------|----------|------------|-----------|
| **TTE** | TotalEnergies | Paris (Euronext) | €140B+ | Like XOM (your winner) |
| **SHEL** | Shell | London/Amsterdam | €200B+ | Integrated oil major |

**Defense (Geopolitical Catalyst):**

| Ticker | Company | Exchange | Market Cap | Why Trade |
|--------|---------|----------|------------|-----------|
| **BA.** | BAE Systems | London (LSE) | £35B+ | UK defense, Ukraine/NATO theme |
| **RHM** | Rheinmetall | Frankfurt (XETRA) | €25B+ | German defense, strong momentum |
| **HO** | Thales | Paris (Euronext) | €25B+ | French defense & aerospace |
| **AIR** | Airbus | Paris (Euronext) | €110B+ | Aerospace, commercial + defense |

**Industrials:**

| Ticker | Company | Exchange | Market Cap | Why Trade |
|--------|---------|----------|------------|-----------|
| **SIE** | Siemens | Frankfurt (XETRA) | €130B+ | Industrial automation |
| **STLA** | Stellantis | Paris/Milan | €60B+ | Automotive (better than GM/F?) |

---

### Swiss Securities (CHF-Denominated)

#### TIER 1 - High Priority CHF Additions

**Healthcare/Pharma:**

| Ticker | Company | Exchange | Market Cap | Why Trade |
|--------|---------|----------|------------|-----------|
| **NOVN** | Novartis | SIX Swiss | CHF 180B+ | Pharma leader, quality |
| **ROG** | Roche | SIX Swiss | CHF 230B+ | Pharma + diagnostics |
| **LONN** | Lonza | SIX Swiss | CHF 35B+ | Pharma manufacturing |

**Financials:**

| Ticker | Company | Exchange | Market Cap | Why Trade |
|--------|---------|----------|------------|-----------|
| **UBSG** | UBS Group | SIX Swiss | CHF 90B+ | Banking, post-Credit Suisse |
| **ZURN** | Zurich Insurance | SIX Swiss | CHF 65B+ | Insurance |

**Luxury/Consumer:**

| Ticker | Company | Exchange | Market Cap | Why Trade |
|--------|---------|----------|------------|-----------|
| **CFR** | Compagnie Financière Richemont | SIX Swiss | CHF 70B+ | Luxury (Cartier, etc.) |
| **SREN** | Swatch Group | SIX Swiss | CHF 10B+ | Watches |

**Industrials:**

| Ticker | Company | Exchange | Market Cap | Why Trade |
|--------|---------|----------|------------|-----------|
| **ABBN** | ABB Ltd | SIX Swiss | CHF 60B+ | Electrical equipment, automation |
| **GEBN** | Geberit | SIX Swiss | CHF 18B+ | Plumbing/construction |

**Food/Consumer:**

| Ticker | Company | Exchange | Market Cap | Why Trade |
|--------|---------|----------|------------|-----------|
| **NESN** | Nestlé | SIX Swiss | CHF 260B+ | Food/beverage giant (like WMT stability?) |
| **GIVN** | Givaudan | SIX Swiss | CHF 40B+ | Flavors & fragrances |

---

### Trading EUR/CHF Securities - Special Considerations

#### Options Availability

**GOOD NEWS:**
- European options markets exist (Eurex for German/Swiss, Euronext for French/Dutch)
- Many large EUR stocks have liquid options
- Some European stocks have US ADRs with USD options (easier for you?)

**CHALLENGE:**
- Less liquid than US options (wider spreads)
- Not all European stocks have options
- May need to use US ADRs for some (but then you're back in USD!)

**RECOMMENDATION:**

| Approach | Securities | Currency | Pros | Cons |
|----------|------------|----------|------|------|
| **US ADRs** | NVO, MC, ASML (US-listed) | USD options | Liquid options, easy to trade | Still USD exposure! |
| **European exchanges** | SAP, LVMH, Novartis | EUR/CHF options | True EUR/CHF exposure | Less liquid, wider spreads |
| **Mix both** | Some ADRs + some European | Mixed | Flexibility | Need multiple accounts |

**For your currency hedge, you MUST use European exchange options (EUR/CHF), not US ADRs (which are USD)!**

---

#### Exchange & Broker Requirements

**To trade EUR/CHF options:**

1. **Eurex (European options exchange):**
   - Covers German, Swiss, some European stocks
   - SAP, Novartis, Roche, Siemens options
   - Need broker with Eurex access

2. **Euronext (Paris/Amsterdam options):**
   - LVMH, TotalEnergies, ASML options
   - Need Euronext access

3. **SIX Swiss Exchange:**
   - Swiss stocks (Novartis, Roche, UBS, Nestlé)
   - Options via Eurex or SOFFEX

**Broker Recommendations (Geneva-based):**
- **Interactive Brokers** - Best for multi-currency, Eurex + Euronext access
- **Swissquote** - Swiss broker, good for CHF securities
- **Saxo Bank** - European focus, multi-currency

You probably already have this access if you're in Geneva!

---

## CURRENCY-BALANCED TRADING FRAMEWORK

### Daily Position Sizing Workflow

**BEFORE entering new BOT trade:**

**Step 1: Calculate current currency exposure**

```
Current USD exposure: Sum of all USD positions in CHF terms
Current EUR exposure: Sum of all EUR positions in CHF terms
Current CHF exposure: Sum of all CHF positions

Total portfolio: USD + EUR + CHF
```

**Step 2: Check target allocation**

```
Target: 40-50% USD, 30-40% EUR, 10-20% CHF

Current allocation:
- USD: X%
- EUR: Y%
- CHF: Z%
```

**Step 3: Determine which currency to trade**

```
IF USD < 40% → Prioritize USD security
IF EUR < 30% → Prioritize EUR security
IF CHF < 10% → Prioritize CHF security

IF USD > 50% → AVOID USD security (over-allocated)
IF EUR > 40% → AVOID EUR security
IF CHF > 20% → AVOID CHF security
```

**Step 4: Find BOT setup in needed currency**

```
Scan Tier 1 securities in target currency:
- USD: AAPL, GLD, NFLX, WMT, JNJ, V
- EUR: ASML, LVMH, SAP, TotalEnergies
- CHF: Novartis, Roche, UBS

Pick best technical setup in needed currency
```

---

### Example: Currency-Balanced Entry Decision

**Current Portfolio:**

| Currency | Exposure (CHF) | % of Total | vs Target | Action |
|----------|----------------|------------|-----------|--------|
| USD | CHF 2,500 | 55% | Over (target 40-50%) | AVOID USD |
| EUR | CHF 1,200 | 26% | Under (target 30-40%) | **PRIORITIZE EUR** |
| CHF | CHF 800 | 18% | OK (target 10-20%) | Neutral |
| **Total** | **CHF 4,500** | **100%** | | |

**New BOT Setup:**
- You see AAPL breaking out (USD) ← Technical setup is great
- You also see ASML breaking out (EUR) ← Technical setup is also great

**Decision:**
- **Choose ASML (EUR)** even though AAPL might be slightly better setup
- Reason: EUR under-allocated (26% vs 30% target)
- This brings portfolio back into balance

**IF both setups are truly equal quality:**
- EUR wins due to allocation
- Currency risk management > marginal setup quality difference

**IF AAPL is CLEARLY better (50 delta, clean Fib break vs ASML 25 delta, marginal break):**
- Can override and take AAPL
- But immediately look for next EUR trade to rebalance

---

### Weekly Portfolio Review

**Every Friday:**

1. **Currency Exposure Check:**

```
Calculate:
- Total USD exposure (sum of all USD positions)
- Total EUR exposure (sum of all EUR positions)
- Total CHF exposure (sum of all CHF positions)

Convert to %:
- USD: X% (target 40-50%)
- EUR: Y% (target 30-40%)
- CHF: Z% (target 10-20%)
```

2. **Rebalancing Actions:**

```
IF USD > 55%:
  - Close lowest-conviction USD trade
  - Next 2-3 trades must be EUR/CHF

IF EUR < 25%:
  - Actively scan for EUR setups
  - Lower bar for EUR entry (accept 6/7 checklist vs 7/7)

IF CHF < 5%:
  - Add Swiss defensive trade (Novartis, Nestlé)
```

3. **Currency Macro View:**

```
Check USD/CHF trend:
- Trending up (USD strengthening)? → Increase USD allocation to 50-60%
- Trending down (USD weakening)? → Decrease USD to 30-40%
- Sideways/unclear? → Maintain 40% balanced

Check EUR/CHF trend:
- EUR strengthening vs CHF? → Can increase EUR to 45%
- EUR weakening vs CHF? → Decrease EUR to 30%
```

---

## CURRENCY RISK MONITORING

### Track These Metrics

**In your trading journal, add:**

| Trade # | Security | Currency | Entry (Local FX) | Exit (Local FX) | P&L (USD/EUR) | FX Rate at Entry | FX Rate at Exit | P&L (CHF) | FX Impact |
|---------|----------|----------|------------------|-----------------|---------------|------------------|-----------------|-----------|-----------|
| 569 | GLD | USD | $500 | $1,200 | +$700 | 0.88 | 0.86 | +CHF 602 | -CHF 18 |
| ... | ASML | EUR | €400 | €900 | +€500 | 0.96 | 0.97 | +CHF 485 | +CHF 5 |

**Monthly Summary:**

```
Total P&L (USD trades): +$2,500
FX impact on USD trades: -CHF 120 (lost 4.8% to FX)

Total P&L (EUR trades): +€1,200
FX impact on EUR trades: +CHF 35 (gained 2.9% from FX)

Total P&L (CHF trades): +CHF 450
FX impact: CHF 0 (no FX risk)

NET FX IMPACT: -CHF 85 (negative this month - USD weakened)
```

**Action:** If consistently losing to FX, adjust allocation!

---

### FX Hedging Decision Tree

```
START: Analyze total portfolio FX exposure

├─ Portfolio is currency-balanced (40% USD, 35% EUR, 25% CHF)
│  └─ NO ACTION NEEDED ✓
│
├─ Portfolio is USD-heavy (60%+ USD)
│  ├─ Do you expect USD to strengthen vs CHF?
│  │  ├─ YES → Keep USD exposure (benefit from FX tailwind)
│  │  └─ NO → REDUCE USD exposure or add EUR/CHF trades
│  │
│  └─ Uncertain on USD direction?
│      └─ REBALANCE to 40% USD (reduce FX risk)
│
└─ Portfolio is EUR-heavy (50%+ EUR)
   ├─ Do you expect EUR to strengthen vs CHF?
   │  ├─ YES → Keep EUR exposure
   │  └─ NO → REDUCE EUR exposure or add USD/CHF trades
   │
   └─ Uncertain?
       └─ REBALANCE to 35% EUR
```

---

## RECOMMENDED CURRENCY-BALANCED UNIVERSE

### TIER 1 - Core Securities by Currency

**USD Securities (Target: 40-50% of portfolio)**

| Security | Market | Why Trade | Notes |
|----------|--------|-----------|-------|
| **AAPL** | Tech | 75% WR, +$2,481 | Your best USD trade |
| **GLD** | Precious Metals | 60% WR, +$2,112 | Macro hedge |
| **NFLX** | Tech | 100% WR, +$791 | Perfect record |
| **WMT** | Consumer | 100% WR, +$829 | Defensive |
| **JNJ** | Healthcare | 100% WR, +$1,040 | Quality |
| **XOM** | Energy | 100% WR, +$1,243 | Only oil stock |

**~6-8 core USD securities**

---

**EUR Securities (Target: 30-40% of portfolio)**

| Security | Market | Why Trade | Notes |
|----------|--------|-----------|-------|
| **ASML** | Tech | Chip equipment monopoly | Like your tech winners |
| **SAP** | Tech | Enterprise software | Stable, like AAPL |
| **LVMH** | Luxury | Luxury leader | Strong trends, like WMT quality |
| **TotalEnergies** | Energy | Integrated oil | Like XOM (your winner) |
| **Novo Nordisk** (EUR listing) | Healthcare | Obesity drugs | Massive momentum |
| **Rheinmetall** | Defense | German defense | Geopolitical catalyst |
| **Hermès** | Luxury | Ultra-luxury | Quality |

**~6-8 core EUR securities**

---

**CHF Securities (Target: 10-20% of portfolio)**

| Security | Market | Why Trade | Notes |
|----------|--------|-----------|-------|
| **Novartis** | Healthcare/Pharma | Pharma leader | Like ABBV |
| **Roche** | Healthcare/Pharma | Pharma + diagnostics | Diversified |
| **Nestlé** | Consumer | Food/beverage | Like WMT stability |
| **UBS** | Financials | Swiss banking | Post-Credit Suisse |
| **Richemont** | Luxury | Luxury (Cartier) | Thematic |

**~4-5 core CHF securities**

**Total Universe: 16-21 securities across 3 currencies**

---

## PRACTICAL IMPLEMENTATION

### Week 1: Setup

1. **Verify broker access:**
   - ✓ Can I trade Eurex options (SAP, Novartis, Siemens)?
   - ✓ Can I trade Euronext options (LVMH, TotalEnergies, ASML)?
   - ✓ Can I trade SIX Swiss Exchange options (Roche, UBS)?

2. **Add EUR/CHF securities to watchlist:**
   - ASML, SAP, LVMH, Novo Nordisk, TotalEnergies, Rheinmetall
   - Novartis, Roche, Nestlé, UBS, Richemont

3. **Create currency exposure tracker:**
   - Spreadsheet with columns: Security, Currency, Size, CHF Equivalent, % of Portfolio
   - Update daily

---

### Week 2-4: Test EUR/CHF Trades

**Goal:** Execute 2-3 EUR trades and 1-2 CHF trades to:
- Test options liquidity (bid-ask spreads acceptable?)
- Validate BOT strategy works in EUR/CHF markets
- Build familiarity with European options

**Start with:**
- **ASML** (EUR) - Most liquid European tech options
- **Novartis** (CHF) - Liquid Swiss pharma options

**Track:**
- Execution quality (spreads, fills)
- Technical behavior (do Fib zones work same as US?)
- Currency impact on P&L

---

### Month 2+: Full Currency Balance

**Target portfolio allocation:**

```
10 open BOT positions:
- 4-5 USD positions (40-50%)
- 3-4 EUR positions (30-40%)
- 1-2 CHF positions (10-20%)
```

**Daily workflow:**
1. Scan all 3 currency universes for breakouts
2. Check current currency allocation
3. Prioritize entry in under-allocated currency
4. Execute trade

**Weekly review:**
- Measure FX impact on P&L
- Adjust allocation if needed
- Track if currency hedge is working

---

## ADVANCED: CURRENCY OVERLAY STRATEGIES

### Strategy A: Static Hedge (Conservative)

**Allocation:** Always maintain 40% USD / 40% EUR / 20% CHF

**Pros:**
- Simplest to manage
- Consistent hedge
- No macro FX forecasting needed

**Cons:**
- Miss opportunities when USD clearly trending
- Locked into rigid structure

**Best for:** Conservative, don't want to think about FX

---

### Strategy B: Dynamic Hedge (Moderate)

**Allocation:** Adjust based on USD/CHF and EUR/CHF trends

**Rules:**

```
IF USD/CHF trending UP (USD strengthening):
  → Increase USD to 50-60%
  → Reduce EUR to 25-30%
  → Keep CHF at 15-20%

IF USD/CHF trending DOWN (USD weakening):
  → Decrease USD to 30-40%
  → Increase EUR to 40-50%
  → Keep CHF at 15-20%

IF USD/CHF sideways:
  → Maintain 40% USD / 40% EUR / 20% CHF
```

**Pros:**
- Benefit from FX tailwinds
- Reduce FX headwinds
- Still maintain diversification

**Cons:**
- Requires FX trend monitoring
- Can be whipsawed if wrong on FX

**Best for:** Active trader, comfortable with macro

---

### Strategy C: Opportunistic (Aggressive)

**Allocation:** Go where best BOT setups are, ignore currency

**Only hedge when:**
- USD exposure exceeds 70%+ (too concentrated)
- Add offsetting EUR/CHF position

**Pros:**
- Maximum flexibility
- Always take best technical setups
- Can concentrate in best opportunities

**Cons:**
- Highest FX risk
- Can have 80-90% USD exposure temporarily
- Requires discipline to hedge when needed

**Best for:** Experienced, strong technical trader, can tolerate FX volatility

---

## RECOMMENDED APPROACH FOR YOU

**Start with Strategy B (Dynamic Hedge)**

**Why:**
1. You're trading 8-14 day BOT (short-term)
2. FX can move 2-3% in 2 weeks (material impact)
3. You have expenses in EUR (natural EUR exposure)
4. Living in Geneva (CHF anchor makes sense)

**Implementation:**

**Target Allocation (Baseline):**
- 40% USD
- 40% EUR
- 20% CHF

**Adjust based on macro:**
- If USD trending strong vs CHF → 50% USD / 30% EUR / 20% CHF
- If USD trending weak vs CHF → 30% USD / 50% EUR / 20% CHF
- If uncertain → 40% USD / 40% EUR / 20% CHF

**Maximum limits:**
- Never exceed 65% in any single currency
- Never go below 20% USD (need US market liquidity)
- Never go below 10% CHF (your base currency)

**Weekly rebalancing:**
- If any currency >10% off target, prioritize rebalancing
- Close lowest-conviction trade in over-allocated currency
- Next entry must be in under-allocated currency

---

## SUMMARY: ACTION STEPS

### Immediate (This Week):

1. ✓ **Verify broker capabilities** for EUR/CHF options
2. ✓ **Add to watchlist:** ASML, SAP, LVMH, Novartis, Roche
3. ✓ **Create currency tracker** spreadsheet
4. ✓ **Calculate current currency exposure** on existing positions

### Month 1:

1. ✓ **Execute first EUR trade** (recommend: ASML)
2. ✓ **Execute first CHF trade** (recommend: Novartis)
3. ✓ **Track FX impact** on all trades
4. ✓ **Test options liquidity** in EUR/CHF markets

### Month 2+:

1. ✓ **Maintain 40/40/20 allocation** (USD/EUR/CHF)
2. ✓ **Weekly currency review** and rebalancing
3. ✓ **Build EUR/CHF universe** to 15-20 securities
4. ✓ **Measure FX hedge effectiveness** monthly

---

**The goal: Never again lose 50% of a winning trade to currency risk.**
