# BOT STRATEGY - PRACTICAL TRADING PLAYBOOK
**Quick-Decision Framework for Weekly Breakout Trades**

---

## EXECUTIVE SUMMARY

**Your Edge:** 2.71x win/loss ratio | $8,742 total profit | 40% win rate
**Key Success Factor:** Strong directional skill + proper option structure selection
**Time Requirement:** 5-minute pre-trade checklist + daily 2-minute monitoring

---

## CORRECTED FINDINGS

### 1. Premium Analysis - IMPORTANT CORRECTION

**Original finding was FLAWED:** Absolute premium ($0-1 vs $3-5) doesn't account for spot price differences.

**Correct Analysis Needed:**
- **HAL at $29:** $0.50 option = 1.7% of spot (reasonable)
- **AAPL at $190:** $0.50 option = 0.26% of spot (likely far OTM, low delta)
- **SLV at $28:** $0.22 option = 0.79% of spot (won $1,633!)

**What Actually Matters:**
1. **Delta:** 30-50 delta range (not premium dollars)
2. **IV Percentile:** <50% historically (room for expansion)
3. **Time:** 15-28 DTE at entry

**Your winning SLV trade proves this:**
- Trade #568: SLV 17APR25 28 P at $0.22 → +$1,633
- Low absolute premium BUT proper structure for low-priced underlying

---

## PART 1: PRE-TRADE CHECKLIST (5 MINUTES)

### Quick Decision Framework

**STEP 1: TECHNICAL VALIDATION (90 seconds)**

□ **Breakout confirmed?**
  - Price broke above/below key resistance/support
  - Fibonacci consolidation zone clearly breached
  - Above 25 & 50 DMA (for calls) / Below (for puts)

□ **Target defined?**
  - Clear Fibonacci extension level for exit
  - Measured move or prior swing high/low

□ **Timing right?**
  - Continuation breakout (better) vs first attempt (riskier)
  - Volume confirmation present

**If any box unchecked → PASS on trade**

---

**STEP 2: SECTOR/MACRO FILTER (30 seconds)**

□ **Sector alignment?**
  - ✅ PREFER: Precious Metals, Technology, Healthcare, Consumer
  - ⚠️ CAUTION: Energy/Commodities (whipsaw risk)
  - ❌ AVOID: Index ETFs (SPY, QQQ, IWM) unless VIX rising sharply

□ **Narrative check?**
  - Not an overcrowded consensus trade (check financial media, options OI)
  - Has clear catalyst or technical driver

---

**STEP 3: OPTION STRUCTURE SELECTION (2 minutes)**

### A. Strike Selection: Delta-Based Rule

**Use Delta, not premium dollars:**

| Conviction Level | Call Delta | Put Delta | Profile |
|-----------------|------------|-----------|---------|
| **High conviction** | 45-55 (ATM) | 45-55 (ATM) | Faster P&L, higher cost |
| **Medium conviction** | 30-40 (OTM) | 30-40 (OTM) | Balanced risk/reward |
| **Low conviction / Testing** | 20-30 (farther OTM) | 20-30 (farther OTM) | Cheaper, needs big move |

**Rule of thumb:** Use 40-50 delta for most BOT trades (best balance)

---

### B. Outright vs Spread Decision Tree

```
START: Is IV Percentile > 60%? (Check IV rank on your platform)
│
├─ YES (High IV) ──> Use SPREAD
│   │
│   └─ For Calls: Buy Call Spread (Buy ATM, Sell OTM at Fib target)
│   └─ For Puts: Buy Put Spread (Buy ATM, Sell OTM at Fib target)
│
│   Example: GLD Dec 2025 - High IV environment
│   Action: Buy 266/275 Call Spread instead of outright 266 Call
│   Benefit: IV crush affects both legs, reducing risk
│
└─ NO (Low/Normal IV < 60%) ──> Use OUTRIGHT OPTION
    │
    └─ Rationale: You WANT volatility expansion
       Spread caps your upside from vega gains
```

**Why this matters:**
- **High IV:** Spread protects from IV crush (your GLD example)
- **Low IV:** Outright captures full vega expansion benefit

**Additional Spread Considerations:**
- Use spreads when premium cost feels "too expensive" for position sizing
- Width of spread = Fib target distance (sell strike at technical target)
- Spreads reduce max profit but define risk precisely

---

### C. IV Environment Check

□ **IV Percentile < 50%?** (Ideal - room for expansion)
  - ✅ BEST: IV 20-40%ile (low, expansion likely)
  - ⚠️ ACCEPTABLE: IV 40-60%ile (neutral, use spreads if >50%)
  - ❌ RISKY: IV >70%ile (high, use spreads or pass)

**CRITICAL DISTINCTION:**

| Scenario | VIX/IV Status | Action | Reasoning |
|----------|---------------|--------|-----------|
| **Entry** | VIX LOW (12-15) | ✅ ENTER CALLS | IV expansion likely on breakout |
| **Entry** | VIX HIGH (25+) | ❌ AVOID CALLS | IV crush risk when fear subsides |
| **Entry** | VIX RISING | ⚠️ CONTEXT-DEPENDENT | See below |
| **During Trade** | VIX SPIKING | 🔔 MONITOR | May help puts, hurt calls |

**Addressing Question 3: VIX Rising - What to Do?**

**For CALL options:**
- VIX rising usually means market stress/selling
- Your call may suffer even if IV increases (spot price falling)
- **Action:** Tighten stops, consider exit if broad market weakening
- **Exception:** Sector-specific strength (e.g., Gold rising while SPY falls)

**For PUT options:**
- VIX rising helps put values (fear premium)
- BUT timing is critical - markets fall fast and bounce fast
- **Action:** Take profits faster on puts (70% of time markets rise)
- **Rule:** Puts require tighter profit targets than calls

**Best Practice:** Enter when VIX is LOW, ride the IV expansion during breakout

---

### D. Time Selection

□ **Duration check:**
  - ✅ OPTIMAL: 15-28 DTE (days to expiration)
  - Target exit in 8-14 days (sweet spot: 64.3% WR)
  - Avoid entering with <10 DTE or >40 DTE

---

**STEP 4: POSITION SIZING & RISK (1 minute)**

□ **Max risk defined:**
  - Dollar amount you're willing to lose (e.g., $200-300)
  - For outright: Premium paid × contracts
  - For spread: (Spread width - premium paid) × contracts × 100

□ **Exit targets set BEFORE entry:**
  - Profit target: Fibonacci extension or 2R (twice your risk)
  - Stop loss: Below breakout level or max 50% of premium

**Addressing Question 7: What is "2R"?**

**R = Initial Risk**

Example:
- You buy a call for $3.00 (your risk = $300 per contract)
- 1R = $300 profit (breakeven + $300)
- 2R = $600 profit (breakeven + $600)
- 3R = $900 profit (breakeven + $900)

**Rule 44 clarification:** "If trade is up >2R, take partial profits"
- Means: If you're up 2× your initial risk, scale out at least 1/3 of position
- This locks in a win and lets rest run with house money

---

**STEP 5: PRE-ENTRY PLANNING (1 minute)**

**Define NOW (before entry):**

□ **Technical exit level:** Where does asymmetry disappear?
  - Fibonacci extension target
  - Next resistance/support zone
  - "No asymmetry left" = when easy money is made

□ **Time-based exit:** If not profitable by Day 21, close or roll

□ **Scaling plan:** (Should be in "Before Entry", not "During Trade")
  - First exit: At 2R or interim resistance
  - Second exit: At Fib target or when asymmetry exhausted
  - Final piece: Trail with technical stop

□ **Automatic orders:** (Should be set before entry)
  - Set limit sell orders at technical targets
  - Example: Your JNJ trade used BS pricing to set sell limits
  - Removes emotion from exit decision

---

## SIMPLIFIED PRE-TRADE CHECKLIST SUMMARY

**7 QUICK CHECKS (Can be done in 5 minutes):**

1. ✅ **Technical:** Breakout confirmed, target defined, above/below DMAs
2. ✅ **Sector:** Not in index ETF, sector shows leadership
3. ✅ **Delta:** 30-50 delta range (not too far OTM)
4. ✅ **IV Check:** IV%ile <50% for outright, or use spread if >60%
5. ✅ **Structure:** Outright (low IV) vs Spread (high IV)
6. ✅ **Time:** 15-28 DTE entry
7. ✅ **Exits Planned:** Technical target, time stop (day 21), scaling levels defined

**If all 7 are YES → ENTER TRADE**
**If any critical box is NO → PASS**

---

## PART 2: MONITORING SYSTEM (2 MINUTES DAILY)

### Daily Quick Check (End of Day)

**Run this at market close or before next morning:**

| Check | Green Flag ✅ | Yellow Flag ⚠️ | Red Flag 🔴 Action Required |
|-------|--------------|---------------|----------------------------|
| **Days Held** | 0-14 days | 15-21 days | >21 days → Close or roll with +21 DTE |
| **Price vs Breakout** | Above (calls) / Below (puts) | Testing breakout level | Broke back through → CLOSE |
| **Fib Structure** | In extension zone | At target zone | Broke above/below Fib zone → CLOSE |
| **IV Movement** | Expanding or stable | Contracting slowly | Crushed >20% → Reassess |
| **P&L** | Profitable or small loss | Flat | Down >50% of premium → Review stop loss |
| **Asymmetry** | Still present (room to run) | Nearing exhaustion | Gone (target hit) → CLOSE |

**Action Matrix:**

- **All Green:** Hold, let it run
- **1-2 Yellow:** Monitor closely, prepare for exit
- **Any Red:** Execute the red flag action immediately

---

### Weekly Review (Fridays, 5 minutes)

For each open BOT position, answer:

1. **Would I enter this trade today at current levels?**
   - YES → Hold
   - NO → Close Monday morning

2. **Has the thesis changed?**
   - Sector rotation occurred
   - Macro narrative shifted
   - Technical structure broken

3. **Days held:**
   - <21 days → OK to hold if technical structure intact
   - ≥21 days → Close or roll (22-28 day window is graveyard)

---

## PART 3: EXIT RULES (CLEAR-CUT)

### Automatic Exits (Set these at entry)

1. **Profit Targets:**
   - First piece: 2R or halfway to Fib target
   - Second piece: Fib extension target or 3R
   - Final piece: Trail with 2 ATR stop or close when asymmetry exhausted

2. **Stop Losses:**
   - Hard stop: Breakout level violated (price closes back through)
   - Time stop: Day 21 if not profitable
   - Dollar stop: -50% of premium OR max risk defined pre-trade

### Manual Exits (Discretionary Signals)

**CLOSE IMMEDIATELY when:**

- [ ] "No asymmetry left" - target zone reached, move exhausted
- [ ] Fib structure violated (price broke back into consolidation zone)
- [ ] IV crushed >20% while spot flat/adverse
- [ ] Sector rotation evident (leadership changed)
- [ ] You feel "lazy" about managing trade (discipline breakdown signal)
- [ ] Considering repositioning strike without extending duration (just close instead)

**Your own words from winning trades:**
- "Break out is over, no asymmetry any more" (GLD +$1,692)
- "Not be too greedy" (EQT +$721)
- "Made the max profit I was expecting" (XOM +$886)

**Your own words from losing trades (learn from these):**
- "Should have closed earlier, I was lazy" (C -$324)
- "Not worth repositioning strike without duration" (USO -$507)

---

## PART 4: ADVANCED RULES

### IV Percentile Analysis (Addressing Question 5)

**Question 5: "Do you mean future realized vol should be greater than implied vol?"**

**Clarification:**

**Rule 13 Original:** "What realized volatility is required for this trade to profit?"

**What this means:**
- Calculate the breakeven spot price at expiration
- Estimate what daily volatility is needed to reach that price
- Compare to current IV

**Example:**
- Stock at $100, buy $105 call for $2, 20 DTE
- Need stock to reach $107 to breakeven
- That's 7% move in 20 days ≈ 1.5% daily realized vol
- If IV implies 1% daily vol, you need MORE volatility than priced in
- If IV implies 2% daily vol, you're buying expensive volatility

**BUT - Exception (your point about earnings):**
- Before earnings, IV spikes (implied vol increases)
- You can profit from IV expansion EVEN IF realized vol stays low
- **Key:** Sell BEFORE earnings when IV peaks, don't hold through event

**Corrected Rule 13:**
"Will this trade profit from directional move alone, or am I relying on IV expansion?"
- ✅ BEST: Both direction AND IV expansion expected (low IV breakout)
- ⚠️ RISKY: Need IV expansion to profit (selling before event works)
- ❌ AVOID: High IV, relying on direction alone (IV crush kills you)

---

### Index Options - Special Case (Addressing Question 2)

**Question 2: "What do you mean 'Index options are volatility trades more than directional trades'?"**

**Explanation:**

**Index options (SPY, QQQ, IWM) behave differently than single stocks:**

1. **Lower Realized Volatility:**
   - Indices diversify away single-stock risk
   - SPY realized vol ≈ 15-20% annual
   - Individual stocks ≈ 25-40% annual
   - Lower vol = less option movement per spot move

2. **IV Mean Reversion:**
   - Index IV spikes during fear (VIX >25)
   - Then compresses quickly back to 12-15
   - **Your SPY loss:** IV 17% → 13% = -$320 from vega alone
   - Single stocks: IV trends persist longer

3. **Hedging Demand:**
   - Institutions constantly buy index puts (portfolio protection)
   - This creates persistent put skew and IV compression on calls
   - When fear subsides, puts get sold → IV crush

4. **Tight Ranges:**
   - SPY moves 0.5-1% daily (normal)
   - Individual breakout stocks move 3-5% daily
   - Options need movement to overcome theta

**Your Data Confirms This:**
- **Index/ETF trades:** 8 total, -$1,249 P&L, 25% WR (WORST sector)
- **Single-stock trades:** Much better win rates

**When Index BOT Works:**
- VIX rising sharply (10 → 20+) - volatility expansion regime
- Major market breakout with expanding breadth
- Short-term tactical trades (0-7 DTE) with defined events

**When Index BOT Fails:**
- VIX already elevated (>20) - IV crush incoming
- Low-vol grind environments (VIX 12-15)
- Your directional call is right, but IV compresses faster than spot moves

**Recommendation:** Stick to single-name equities for BOT unless clear volatility regime shift.

---

### Spread vs Outright - Decision Matrix (Addressing Question 8)

**Question 8: "High IV can still work for breakout trades if using spreads (GLD Dec 2025 example)"**

**Absolutely correct. Here's the decision framework:**

| Scenario | IV Environment | Underlying Type | Choice | Reasoning |
|----------|----------------|-----------------|--------|-----------|
| **GLD Dec 2025** | High (>60%ile) | Single stock | SPREAD | Sell expensive premium at Fib target, cap IV crush risk |
| **Tech breakout** | Low (<40%ile) | Single stock | OUTRIGHT | Capture full vega expansion |
| **Index breakout** | Any | Index ETF | SPREAD or PASS | Indices compress IV quickly |
| **Earnings play** | High (pre-event) | Single stock | SPREAD | Sell at event, reduce IV crush |
| **Low-priced stock** | Normal | HAL, F, etc. | OUTRIGHT | Spreads too narrow for low $ stocks |

**Spread Advantages When IV is High:**
- Both legs experience IV crush equally (net impact reduced)
- Define max profit AND max loss precisely
- Lower capital requirement vs outright
- Can still profit from directional move

**Spread Disadvantages:**
- Cap upside gains (can't capture "home run" trades)
- Wider bid-ask spread (execution cost)
- Less sensitivity to volatility expansion (lower vega)

**Your GLD Example (Dec 2025):**
- IV was elevated (gold volatility spike)
- Used spread to reduce IV exposure
- Directional thesis intact
- Smart adjustment for environment

**Rule:** High IV doesn't prohibit BOT - it changes structure from outright to spread.

---

## PART 5: SIMPLIFIED RULES SUMMARY

### Entry Rules (VALIDATED)

1. **Delta:** 30-50 delta range (focus on this, not premium dollars)
2. **IV Check:** <50%ile for outright, 50-70%ile use spreads, >70%ile avoid or tight spreads
3. **Duration:** 15-28 DTE entry, target 8-14 day hold
4. **Sector:** Prefer single names in Metals, Tech, Healthcare; avoid index ETFs
5. **Technical:** Clear breakout with Fib target defined
6. **VIX Context:** Enter when VIX low (<18), not when elevated

### Exit Rules (VALIDATED)

7. **Asymmetry:** Close when target reached or "no asymmetry left"
8. **Progressive:** Scale out at 2R, Fib target, and trail remainder
9. **Time:** Close by Day 21 if not profitable (avoid Day 22-28 graveyard)
10. **Technical:** Close if breaks back below breakout level or Fib zone
11. **Discipline:** Close immediately when you "know" you should (no lazy holding)
12. **Automatic:** Set limit orders at entry based on technical levels

### Forbidden Actions (VALIDATED)

13. **Never:** Reposition strike without extending duration (+21 DTE minimum)
14. **Never:** Hold from laziness when exit signal clear
15. **Never:** Enter far OTM options just because they're cheap (low delta <20)
16. **Never:** Enter index BOT when VIX already elevated (IV crush trap)

---

## PART 6: QUICK REFERENCE CARD

**Print this and keep at your desk:**

```
═══════════════════════════════════════════════════════════════
              BOT TRADE QUICK DECISION CARD
═══════════════════════════════════════════════════════════════

ENTRY CHECKLIST (5 min):
□ Breakout confirmed, above/below DMAs, target defined
□ Sector: Single-name stock (not index ETF)
□ Delta: 30-50 range
□ IV: <50%ile (outright) or 50-70%ile (spread)
□ Time: 15-28 DTE
□ Exit plan: Technical target + Day 21 time stop
□ Position size: Max risk acceptable

STRUCTURE DECISION:
• IV < 50%ile → OUTRIGHT option
• IV 50-70%ile → CALL/PUT SPREAD
• IV > 70%ile → TIGHT SPREAD or PASS

DAILY MONITOR (2 min):
✓ Days held <21? (If ≥21 → Close or roll)
✓ Price above/below breakout? (If broke back → Close)
✓ Fib structure intact? (If violated → Close)
✓ Would I enter today? (If NO → Close)

EXIT TRIGGERS:
→ Hit Fib target / No asymmetry left
→ Up 2R: Take 1/3 off, trail rest
→ Day 21: Close if not profitable
→ Break back through entry level: Close immediately
→ "I should close this": DO IT NOW

FORBIDDEN:
✗ Reposition strikes without adding duration
✗ Hold from laziness
✗ Enter far OTM (<20 delta)
✗ Index options when VIX >20
═══════════════════════════════════════════════════════════════
```

---

## PART 7: REAL EXAMPLES FROM YOUR TRADES

### Perfect Execution Example

**GLD 16MAY25 266 C (Trade #569): +$1,692**

✅ What went right:
- Clear gold breakout, macro tailwind
- Likely 40-50 delta strike (ATM)
- 35 DTE entry (Apr 11 → May 16)
- Closed when: "No asymmetry left, in target zone"
- Held 5 days only (didn't overstay)

**Lesson:** Recognized completion, took profit, moved on.

---

**AAPL 26JAN24 190 C (Trade #376): +$1,346**

✅ What went right:
- "Progressively sold and adjusted sell levels as needed"
- Scaled out in pieces
- High-conviction tech name
- Clear technical management

**Lesson:** Progressive exits capture most of big moves without picking top.

---

### Avoidable Loss Example

**C 30MAY25 60 P (Trade #574): -$324**

❌ What went wrong:
- "Should have been closed earlier. I was lazy"
- Discipline breakdown
- Knew exit signal was there but procrastinated

**Lesson:** When you know, act immediately. Laziness costs money.

---

**SPY 30JUN23 410 P (Trade #224): -$997**

❌ What went wrong:
- Index option (SPY) in low-vol environment
- IV crushed from 17% to 13%
- Held 43 days (way past Day 21 rule)
- Vega loss: -$320, Theta + directional: -$670

**Lesson:** Avoid index BOT unless VIX rising. Obey Day 21 rule.

---

## PART 8: NEXT STEPS

### Implementation Plan

**Week 1: Setup**
- Print Quick Reference Card
- Set up IV percentile indicator on your platform
- Create entry template with all 7 checklist items

**Week 2-4: Practice**
- Run every potential BOT trade through the 7-point checklist
- Log results: Did checklist prevent bad trades? Capture good ones?
- Refine based on your specific trading style

**Ongoing:**
- Friday review: Check all open positions against "Would I enter today?"
- Monthly review: Track win rate by sector, IV environment, structure type
- Adjust rules based on new data

### Questions for Further Analysis

1. **Does sector rotation follow predictable patterns?** (Seasonal, macro-driven?)
2. **Win rate by day of week for entry?** (Monday vs Friday entries)
3. **Performance by VIX regime?** (<15, 15-20, >20)
4. **Spread vs Outright empirical comparison** (need more spread data)

---

## CONCLUSION

**Your edge is real.** The key is disciplined execution around:

1. **Proper structure selection** (delta, IV, outright vs spread)
2. **Time management** (exit by Day 21 if not working)
3. **Asymmetry recognition** (close when easy money is made)
4. **Sector focus** (single names, avoid indices)

**Time investment:**
- **Entry:** 5 minutes per trade (7-point checklist)
- **Daily monitoring:** 2 minutes per open position
- **Weekly review:** 5 minutes total

**This is sustainable for weekly trading.**

Trade well. Trust your rules. Act when you "know."
