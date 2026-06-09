# BALANCED WEEKLY TRADING PLAN
**Max Risk Per Trade: CHF 600**
**Strangle: Learning Mode (1 per week max)**

---

## RISK PARAMETERS

| Parameter | Rule |
|-----------|------|
| **Max risk per trade** | CHF 600 |
| **BOT trades** | Premium ≤ CHF 600 |
| **Short puts** | Always with protective put (spread) |
| **Spread max risk** | Width - credit ≤ CHF 600 |
| **Strangles** | Max 1 per week (learning) |

---

## STRATEGY 1: BOT (BREAKOUT TRADES)

### Position Sizing

**Max premium:** CHF 600 per trade

| Stock Price | Typical Premium | Contracts |
|-------------|-----------------|-----------|
| €50-100 | €2-4 | 2-3 contracts |
| €100-200 | €4-6 | 1-2 contracts |
| €200-400 | €5-8 | 1 contract |
| €700-900 (ASML) | €15-25 | 1 contract (careful sizing) |
| CHF 25-50 | CHF 2-4 | 2-3 contracts |
| CHF 80-100 | CHF 4-6 | 1-2 contracts |

**Example BOT Trades (CHF 600 max):**

| Stock | Price | Strike | Premium | Contracts | Total Cost | Max Risk |
|-------|-------|--------|---------|-----------|------------|----------|
| SAP | €230 | €235 C | €5.50 | 1 | €550 | **CHF 528** ✓ |
| TotalEnergies | €62 | €64 C | €1.80 | 3 | €540 | **CHF 518** ✓ |
| ASML | €900 | €920 C | €22 | **skip** | €2,200 | Too expensive |
| Novartis | CHF 92 | CHF 95 C | CHF 3.50 | 2 | CHF 700 | **CHF 700** ⚠ over |
| Novartis | CHF 92 | CHF 95 C | CHF 3.50 | 1 | CHF 350 | **CHF 350** ✓ |
| UBS | CHF 28 | CHF 29 C | CHF 0.80 | 6 | CHF 480 | **CHF 480** ✓ |

**Note:** ASML options often too expensive for CHF 600 limit. Use smaller contracts or skip.

---

## STRATEGY 2: SHORT PUT SPREADS (MEAN REVERSION)

### Structure

**Always defined risk:**
- Sell: 20 delta put (45 DTE)
- Buy: OTM put (insurance)
- Max risk = Spread width - Net credit ≤ CHF 600

### Spread Sizing for CHF 600 Max Risk

**Formula:**
```
Max Risk = (Strike Sold - Strike Bought) × 100 - Net Credit
Target: Max Risk ≤ CHF 600
```

**Example EUR Spreads:**

| Stock | Current | Sell Put | Buy Put | Width | Credit | Max Risk | CHF Risk |
|-------|---------|----------|---------|-------|--------|----------|----------|
| SAP | €230 | €215 | €207.5 | €7.5 | €2.00 | €550 | **CHF 528** ✓ |
| SAP | €230 | €210 | €200 | €10 | €3.50 | €650 | **CHF 624** ⚠ |
| TotalEnergies | €62 | €58 | €54 | €4 | €0.80 | €320 | **CHF 307** ✓ |
| TotalEnergies | €62 | €56 | €50 | €6 | €1.20 | €480 | **CHF 461** ✓ |
| Siemens | €190 | €175 | €167.5 | €7.5 | €2.20 | €530 | **CHF 509** ✓ |
| Airbus | €165 | €150 | €142.5 | €7.5 | €1.80 | €570 | **CHF 547** ✓ |

**Example CHF Spreads:**

| Stock | Current | Sell Put | Buy Put | Width | Credit | Max Risk |
|-------|---------|----------|---------|-------|--------|----------|
| Novartis | CHF 92 | CHF 85 | CHF 80 | CHF 5 | CHF 1.50 | **CHF 350** ✓ |
| Novartis | CHF 92 | CHF 85 | CHF 77.5 | CHF 7.5 | CHF 2.00 | **CHF 550** ✓ |
| UBS | CHF 28 | CHF 25 | CHF 22.5 | CHF 2.5 | CHF 0.50 | **CHF 200** ✓ |
| ABB | CHF 52 | CHF 48 | CHF 44 | CHF 4 | CHF 1.00 | **CHF 300** ✓ |

**Rules:**
1. Width ≤ €7.5 or CHF 7.5 for most trades
2. Use €10 width only if credit ≥ €4.00
3. 1 spread per underlying (don't stack)

---

## STRATEGY 3: STRANGLES (LEARNING MODE)

### Constraints
- **Maximum:** 1 strangle per week
- **Goal:** Learn the strategy, not maximize profit

### Risk Management for Undefined Risk

**Option A: Use Iron Condor Instead (Defined Risk)**

An iron condor = strangle + wings (protective options)

```
Sell call spread (bear call spread):
- Sell: 20 delta call
- Buy: 10 delta call (insurance)

Sell put spread (bull put spread):
- Sell: 20 delta put
- Buy: 10 delta put (insurance)
```

**Example Iron Condor (SAP at €230):**
- Sell €250 call / Buy €260 call (bear call spread)
- Sell €210 put / Buy €200 put (bull put spread)
- Width: €10 each side
- Total credit: €7.00 (€3.50 + €3.50)
- Max risk per side: €10 - €3.50 = €6.50 = €650 per side
- **Max total risk: €650** ✓

**Option B: Naked Strangle with Stop Loss**

If you want to learn real strangles:
- Set stop loss at 2× credit received
- Example: Collect €5.00 credit, stop at €10.00 loss
- Close if either side breaches 50 delta

**Max risk with stop:** ~€500-700 if disciplined

### Recommended Approach: Start with Iron Condors

| Stock | Current | Call Spread | Put Spread | Width | Credit | Max Risk |
|-------|---------|-------------|------------|-------|--------|----------|
| SAP | €230 | €250/€257.5 | €210/€202.5 | €7.5 | €5.00 | **€250** ✓ |
| Siemens | €190 | €205/€212.5 | €175/€167.5 | €7.5 | €4.00 | **€350** ✓ |
| TTE | €62 | €68/€72 | €56/€52 | €4 | €2.50 | **€150** ✓ |

**Iron condors give you strangle-like exposure with defined max risk!**

---

## WEEKLY TRADING TEMPLATE

### Target: 3-5 New Positions Per Week

| Strategy | Positions/Week | CHF Risk Each | Total CHF Risk |
|----------|----------------|---------------|----------------|
| **BOT** | 2-3 | ≤ CHF 600 | CHF 1,200-1,800 |
| **Short Put Spreads** | 1-2 | ≤ CHF 600 | CHF 600-1,200 |
| **Strangle/Iron Condor** | 0-1 | ≤ CHF 600 | CHF 0-600 |
| **Total** | 3-5 | | **CHF 1,800-3,600** |

### Currency Distribution

| Currency | Positions/Week | Rationale |
|----------|----------------|-----------|
| **USD** | 1-2 | Best liquidity, your proven winners |
| **EUR** | 1-2 | Currency hedge, 30% of expenses |
| **CHF** | 0-1 | Base currency exposure |

---

## EXAMPLE: BALANCED WEEK

### Monday: Scan & Plan

**Check for setups in:**
- BOT: What's breaking out? (technical scan)
- Short puts: What's at support? (mean reversion scan)
- Iron condor: What's range-bound with high IV? (volatility scan)

### Tuesday-Wednesday: Execute

**Example Week (5 positions, CHF 2,650 total risk):**

| # | Strategy | Security | Currency | Trade | Max Risk |
|---|----------|----------|----------|-------|----------|
| 1 | **BOT** | GLD | USD | Buy $265 call, 20 DTE | $550 (CHF 484) |
| 2 | **BOT** | SAP | EUR | Buy €235 call, 18 DTE | €500 (CHF 480) |
| 3 | **Short Put** | TotalEnergies | EUR | Sell €58/€54 put spread, 45 DTE | €320 (CHF 307) |
| 4 | **Short Put** | Novartis | CHF | Sell CHF 85/80 put spread, 45 DTE | CHF 350 |
| 5 | **Iron Condor** | Siemens | EUR | Sell €205/212.5 C, €175/167.5 P | €350 (CHF 336) |

**Total weekly risk:** CHF 1,957
**Currency mix:** USD 25% / EUR 57% / CHF 18%

---

## EUR STOCK SUMMARY (CHF 600 Max Risk)

### For BOT (Buy Calls/Puts)

| Stock | Price | Typical Premium | Max Contracts | Max Risk |
|-------|-------|-----------------|---------------|----------|
| **TotalEnergies** | €62 | €1.50-2.50 | 3-4 | ~CHF 500 ✓ |
| **Deutsche Telekom** | €26 | €0.50-1.00 | 5-6 | ~CHF 500 ✓ |
| **Infineon** | €32 | €0.80-1.50 | 4-5 | ~CHF 500 ✓ |
| **SAP** | €230 | €4.00-6.00 | 1 | ~CHF 500 ✓ |
| **Siemens** | €190 | €4.00-5.50 | 1 | ~CHF 500 ✓ |
| **Airbus** | €165 | €3.50-5.00 | 1 | ~CHF 500 ✓ |
| **ASML** | €900 | €18-30 | ⚠ | ~CHF 1,700+ ✗ |

**ASML note:** Too expensive for CHF 600 limit. Either:
- Skip ASML for BOT
- Use mini options if available
- Accept higher risk (CHF 1,500-2,000) as exception

### For Short Put Spreads

| Stock | Spread Width | Expected Credit | Max Risk |
|-------|--------------|-----------------|----------|
| **TotalEnergies** | €4-6 | €0.80-1.50 | CHF 300-450 ✓ |
| **SAP** | €7.5 | €2.00-2.50 | CHF 480-530 ✓ |
| **Siemens** | €7.5 | €2.00-2.50 | CHF 480-530 ✓ |
| **Airbus** | €7.5 | €1.80-2.20 | CHF 500-550 ✓ |

### For Iron Condors

| Stock | Wing Width | Expected Credit | Max Risk |
|-------|------------|-----------------|----------|
| **SAP** | €7.5 | €4.00-5.50 | CHF 200-350 ✓ |
| **Siemens** | €7.5 | €3.50-4.50 | CHF 300-400 ✓ |
| **TotalEnergies** | €4 | €2.00-3.00 | CHF 100-200 ✓ |

---

## CHF STOCK SUMMARY (CHF 600 Max Risk)

### For BOT

| Stock | Price | Typical Premium | Max Contracts | Max Risk |
|-------|-------|-----------------|---------------|----------|
| **UBS** | CHF 28 | CHF 0.60-1.20 | 5-8 | ~CHF 500 ✓ |
| **ABB** | CHF 52 | CHF 1.50-2.50 | 2-3 | ~CHF 500 ✓ |
| **Novartis** | CHF 92 | CHF 3.00-4.50 | 1-2 | ~CHF 500 ✓ |

### For Short Put Spreads

| Stock | Spread Width | Expected Credit | Max Risk |
|-------|--------------|-----------------|----------|
| **Novartis** | CHF 5-7.5 | CHF 1.50-2.50 | CHF 250-500 ✓ |
| **UBS** | CHF 2.5-3 | CHF 0.40-0.70 | CHF 180-260 ✓ |
| **ABB** | CHF 4-5 | CHF 0.80-1.30 | CHF 270-420 ✓ |

---

## POSITION TRACKING TEMPLATE

### Weekly Trades Log

| Date | Strategy | Security | Currency | Entry | Exit | Risk | P&L | Notes |
|------|----------|----------|----------|-------|------|------|-----|-------|
| Mon | BOT | GLD | USD | $4.50 | | $450 | | Gold breakout |
| Tue | Put Spread | SAP | EUR | €2.20 cr | | €530 | | 45 DTE |
| Wed | Iron Condor | Siemens | EUR | €4.00 cr | | €350 | | 21 DTE |

### Currency Exposure Tracking

| Week | USD Risk | EUR Risk | CHF Risk | Total Risk |
|------|----------|----------|----------|------------|
| Week 1 | CHF 900 | CHF 1,200 | CHF 350 | CHF 2,450 |
| Week 2 | | | | |

---

## CHECKLIST: BEFORE EACH TRADE

### Pre-Trade Validation

**All Strategies:**
- [ ] Max risk ≤ CHF 600? (strict)
- [ ] Currency allocation balanced? (check tracker)
- [ ] Not exceeding total weekly risk? (target CHF 2,500-3,500)

**BOT Specific:**
- [ ] Breakout confirmed (Fib, DMA, volume)?
- [ ] Delta 30-50?
- [ ] DTE 15-28?
- [ ] Premium fits CHF 600 limit?

**Short Put Spread Specific:**
- [ ] At support level?
- [ ] DTE ~45?
- [ ] Spread width gives max risk ≤ CHF 600?
- [ ] Willing to own stock at strike price?
- [ ] Protective put (insurance) included?

**Iron Condor Specific:**
- [ ] Range-bound stock?
- [ ] IV elevated (>30%)?
- [ ] DTE 10-30?
- [ ] Both wings defined (insurance on both sides)?
- [ ] Max risk per side ≤ CHF 600?
- [ ] Only 1 per week? (learning mode)

---

## SUMMARY: YOUR BALANCED APPROACH

### Weekly Rhythm

**Monday:** Scan for setups (all 3 strategies)
**Tuesday-Wednesday:** Execute 3-5 trades
**Thursday-Friday:** Monitor, adjust stops
**Weekend:** Review, plan next week

### Risk Budget

| Metric | Target |
|--------|--------|
| Max risk per trade | **CHF 600** |
| Weekly new risk | CHF 2,000-3,500 |
| Total open risk | CHF 8,000-12,000 |
| Reserve cash | 60%+ of portfolio |

### Strategy Mix

| Strategy | Frequency | Risk per | Weekly Risk |
|----------|-----------|----------|-------------|
| BOT | 2-3/week | CHF 400-600 | CHF 1,200-1,800 |
| Put Spreads | 1-2/week | CHF 300-600 | CHF 300-1,200 |
| Iron Condor | 0-1/week | CHF 200-600 | CHF 0-600 |

### Currency Mix

| Currency | Target | Why |
|----------|--------|-----|
| USD | 30-40% | Best liquidity, proven winners |
| EUR | 40-50% | Currency hedge, 30% expenses |
| CHF | 10-20% | Base currency anchor |

---

## RECOMMENDED STARTING POSITIONS

### This Week: 4 Positions (CHF 1,850 total risk)

1. **BOT (USD):** GLD $265 call if breaking out
   - Premium: $5.00 × 1 = $500 (CHF 440)

2. **BOT (EUR):** SAP €235 call OR TotalEnergies €64 call
   - SAP: €5.00 × 1 = €500 (CHF 480)
   - TTE: €1.60 × 3 = €480 (CHF 460)

3. **Put Spread (EUR):** TotalEnergies €58/€54
   - Credit: €1.00, Max risk: €300 (CHF 290)

4. **Put Spread (CHF):** Novartis CHF 85/80
   - Credit: CHF 1.50, Max risk: CHF 350

**Total first week:** ~CHF 1,560-1,620

### Next Week: Add Iron Condor

5. **Iron Condor (EUR):** SAP or Siemens
   - Max risk: ~CHF 350
   - Start learning strangle/IC dynamics

---

**Your constraints make sense:**
- CHF 600 max = Proper risk management
- Put spreads = Defined risk (no naked exposure)
- 1 strangle/week = Smart learning approach

**You're ready to start!**
