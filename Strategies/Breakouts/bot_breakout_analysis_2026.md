# BOT (Breakout) Strategy — Deep Analysis

*Analysis date: 2026-03-17 | 96 closed trades (excl. zero-P&L) | Jul 2022 – Mar 2026*
*Updated: 2026-03-17 — Added open trade assessment, DOW-pattern screener, TGT trade plan*

---

## 1. HEADLINE NUMBERS

| Metric | Value |
|--------|-------|
| **Total P&L** | **+$9,373** |
| **Win rate** | **40.6%** (39 wins / 57 losses) |
| **Avg win** | +$548 |
| **Avg loss** | -$210 |
| **Profit factor** | 2.60x (avg win / avg loss) |
| **Avg days in trade** | 17.2 |
| **Expectancy per trade** | +$97.63 |

The strategy is profitable despite a sub-50% win rate because **winners are 2.6x larger than losers**. This is a classic momentum/breakout profile — the key is keeping losers small and letting winners run.

---

## 2. THE SINGLE MOST POWERFUL FACTOR: PARTIAL PROFIT-TAKING & RISK-FREE TRADES

| Exit Discipline | Trades | Win % | Avg P&L |
|----------------|--------|-------|---------|
| **Partial profit / risk-free trade** | 13 | **92.3%** | **+$637** |
| No partial profit | 83 | 33.7% | +$13 |

This is the **#1 finding** of the entire analysis. When you scale out (sell enough to cover cost, then ride the rest risk-free), your win rate jumps from 34% to **92%** and avg P&L multiplies by 49x.

Trades where this was done: AAPL #376 (+$1,346), GOLD #351 (+$1,116), XOM #391 (+$886), AMGN #353 (+$868), HAL #657 (+$672), URA #628 (+$400), TGT #678 (+$729), DOW #692 (+$1,058).

**Your own words confirm it**: *"If I had opened 3 contracts and not 4, I would have needed to wait until the price tripled. So this makes it an easier trade."* (HAL #657)

---

## 3. TRADE COMPLEXITY: LEGS MATTER

| Legs | Trades | Win % | Avg P&L |
|------|--------|-------|---------|
| 2 legs (open+close) | 44 | **15.9%** | **-$117** |
| 3-4 legs (adjustments) | 38 | **57.9%** | **+$283** |
| 5+ legs (active mgmt) | 14 | **71.4%** | **+$269** |

**2-leg trades are net losers.** These are "fire and forget" trades with no management — you buy, then sell at a loss or small gain. The moment you actively manage a position (add, scale out, adjust), profitability flips dramatically.

This strongly correlates with the partial profit-taking finding: active management = partial exits = larger winners.

---

## 4. DURATION SWEET SPOT

| Duration | Trades | Win % | Avg P&L |
|----------|--------|-------|---------|
| 0-5 days | 16 | 25.0% | +$56 |
| **6-14 days** | **25** | **52.0%** | **+$146** |
| 15-25 days | 32 | 40.6% | +$120 |
| 26+ days | 23 | 39.1% | +$43 |

The **6-14 day window** is the sweet spot: highest win rate (52%) and best avg P&L (+$146). Trades held for less than a week often fail (25% win rate) — breakouts need a few days to confirm. Trades held beyond 25 days see diminishing returns; theta erosion eats into the gains.

This suggests your optimal holding period is **~2 weeks**, with exits when momentum fades, not when options expire.

---

## 5. ENTRY DAY OF WEEK

| Day | Trades | Win % | Avg P&L |
|-----|--------|-------|---------|
| Monday | 8 | 25.0% | -$28 |
| **Tuesday** | **47** | **44.7%** | **+$177** |
| Wednesday | 20 | 45.0% | +$53 |
| Thursday | 14 | 28.6% | +$39 |
| Friday | 7 | 42.9% | -$44 |

**Tuesday is overwhelmingly your best entry day** — both in volume (49% of all trades) and in avg P&L (+$177). This makes sense: WITT sessions generate ideas early in the week, and Tuesday gives you a confirmed Monday close to validate the breakout before entering.

Monday and Thursday entries perform poorly. Monday may be "jumping the gun" before confirmation; Thursday may be too late in the weekly cycle.

---

## 6. SECTOR PERFORMANCE

| Sector | Trades | Win % | Avg P&L | Total P&L |
|--------|--------|-------|---------|-----------|
| **Precious Metals** (GLD, SLV) | 6 | **66.7%** | **+$395** | +$2,372 |
| **US Bonds** (TLT) | 3 | **66.7%** | +$129 | +$385 |
| **Consumer non-cyclical** | 5 | **60.0%** | +$264 | +$1,319 |
| Technology | 9 | 44.4% | +$214 | +$1,930 |
| Basic Materials | 11 | 36.4% | +$134 | +$1,470 |
| Financial | 5 | 40.0% | +$29 | +$143 |
| Healthcare | 6 | 33.3% | +$29 | +$173 |
| **Energy** | **10** | **30.0%** | **-$66** | **-$659** |
| **US Stocks (SPY/SPX)** | **6** | **33.3%** | **-$102** | **-$610** |

**Precious Metals is your highest-conviction sector** for BOT trades — trending behavior with strong momentum follow-through. Energy is a net loser despite high trade count (MCL futures especially hurt). SPY/SPX breakout attempts consistently underperform.

---

## 7. BETA ANALYSIS

| Beta | Trades | Win % | Avg P&L |
|------|--------|-------|---------|
| **Low beta (<0.5)** | 23 | **56.5%** | **+$231** |
| Medium beta (0.5-1.0) | 19 | 31.6% | -$7 |
| High beta (>1.0) | 27 | 40.7% | +$119 |

**Low-beta stocks outperform dramatically** in BOT trades. This is counter-intuitive but makes sense: low-beta names (GLD, JNJ, ABBV, ABT, AMGN) tend to have cleaner breakout patterns with less noise. High-beta names (AMD, TSLA, PLTR) are noisier and harder to time.

---

## 8. SENTIMENT ANALYSIS FROM REMARKS

| Signal | Trades | Win % | Avg P&L |
|--------|--------|-------|---------|
| **Asymmetry explicitly noted** | 11 | **54.5%** | **+$349** |
| FOMO-driven | 5 | 60.0% | +$198 |
| Patrick-sourced ideas | 30 | 36.7% | +$1 |
| WITT-sourced | 53 | 39.6% | +$111 |
| Non-WITT | 43 | 41.9% | +$81 |

Key takeaways:

- **Asymmetry recognition is a strong predictor**: When you explicitly note "asymmetry" in your remarks, you outperform significantly. This suggests you're better at picking winners when you consciously evaluate risk/reward asymmetry upfront.

- **FOMO trades are surprisingly OK** (5 trades, 60% win): The sample is small, but your FOMO tends to hit in sectors you know well (precious metals, URA). The risk is position sizing, not direction.

- **Patrick's ideas have near-zero edge** on average (+$0.71 avg P&L). However, this is misleading — his best ideas are excellent (V #300, RRC #328, GOLD #351) but some don't translate well into your execution (CSCO trades, TLT #314). The issue isn't idea quality but **execution gap**: you sometimes enter late, choose wrong duration, or don't manage the trade.

---

## 9. OPTION STRUCTURE

| Structure | Trades | Win % | Avg P&L |
|-----------|--------|-------|---------|
| Puts only | 8 | 50.0% | +$210 |
| Mixed C+P | 29 | 44.8% | +$173 |
| Calls only | 54 | 40.7% | +$85 |
| Spreads | 4 | 0.0% | -$372 |
| Futures | 1 | 0.0% | -$438 |

- **Pure spreads (verticals) have 0% win rate** in BOT — they cap your upside which kills the breakout thesis. Your own note on SMH #398: *"as a BOT I let it go till the end as there was no evident breakdown from fib zone either"* — spreads remove the ability to ride momentum.
- **Puts work well** when you're playing a bearish breakout (QCOM, AAPL, NFLX, TLT).
- **Futures (MCL) are destructive** — 2 trades, both losers totaling -$740.

---

## 10. QUARTERLY EVOLUTION — ARE YOU GETTING BETTER?

| Period | Trades | Win % | Avg P&L |
|--------|--------|-------|---------|
| 2023 Q2 | 5 | 0% | -$319 |
| 2023 Q3 | 5 | 60% | +$158 |
| 2023 Q4 | 5 | 40% | +$260 |
| 2024 Q1 | 10 | 50% | +$307 |
| 2024 Q2 | 9 | 22% | -$159 |
| 2024 Q3 | 11 | 36% | +$10 |
| 2024 Q4 | 3 | 33% | +$66 |
| 2025 Q1 | 7 | 57% | +$74 |
| 2025 Q2 | 9 | 33% | +$123 |
| 2025 Q3 | 8 | 38% | +$62 |
| 2025 Q4 | 13 | 54% | +$230 |
| 2026 Q1 | 10 | 40% | +$155 |

**Clear improvement** from 2023 (learning phase) to late 2025/2026. Q4 2025 was your best quarter: 54% win rate, +$230 avg, driven by disciplined trades (JNJ, WMT, HAL, URA, GLD). The blowup quarters (2023Q2, 2024Q2) coincide with SPY/energy overexposure.

---

## 11. TOP 10 WINNERS — WHAT THEY HAVE IN COMMON

| # | Trade | Symbol | P&L | Key Pattern |
|---|-------|--------|-----|-------------|
| 1 | #569 | GLD | +$1,692 | Precious metals + mixed C/P + 3 days |
| 2 | #376 | AAPL | +$1,346 | Progressive sells + 16 days |
| 3 | #393 | AAPL | +$1,278 | Asymmetry noted + 7 days exit |
| 4 | #351 | GOLD | +$1,116 | Partial profit + 20 days |
| 5 | #692 | DOW | +$1,058 | A+ setup + Moontower + fib targets |
| 6 | #644 | JNJ | +$1,040 | BS-based sell targets + 8 days |
| 7 | #391 | XOM | +$886 | Progressive sells + planned exits |
| 8 | #353 | AMGN | +$868 | Partial profit + patience |
| 9 | #653 | WMT | +$829 | Risk-free trade + 6 days |
| 10 | #649 | NFLX | +$791 | Automated target + 17 days |

**Common success traits:**
1. **Active position management** (scaling out progressively)
2. **Pre-defined targets** (BS-model based or fib extension based)
3. **Risk removed early** (cost covered by first partial sale)
4. **Duration 6-20 days** (not held to expiration)
5. **Clear thesis** documented at entry

---

## 12. TOP 10 LOSERS — WHAT WENT WRONG

| # | Trade | Symbol | P&L | Root Cause |
|---|-------|--------|-----|------------|
| 1 | #224 | SPY | -$997 | IV crush 17%→13%, repositioning errors |
| 2 | #404 | USO | -$507 | Repositioned strike without duration |
| 3 | #447 | MCL | -$438 | Futures — wrong instrument for BOT |
| 4 | #636 | ITB | -$333 | Single unfamiliar name, no management |
| 5 | #574 | C | -$324 | Bearish financial — wrong read |
| 6 | #550 | GM | -$309 | Bearish auto sector |
| 7 | #398 | SMH | -$306 | Spread capped upside, held to expiry |
| 8 | #425 | MCL | -$303 | Futures — stopped out in 3 days |
| 9 | #363 | GOOG | -$295 | Entered despite bad R/R, GOOG had already popped |
| 10 | #422 | EBAY | -$292 | "Hail Mary" 14-delta, couldn't exit in time |

**Common failure patterns:**
1. **No active management** — 2-leg trades left to die
2. **Wrong instrument** — Futures (MCL) and pure spreads
3. **Chasing** — Entering after the move (GOOG, EBAY)
4. **Ignoring own rules** — Entering despite bad R/R or missing confirmation
5. **Repositioning strike without duration** — Your own lesson from USO #404

---

## 13. ACTIONABLE RULES (Ranked by Impact)

### RULE 1: Always plan for partial exits (Impact: +$600/trade)
Open enough contracts to sell some at 2x cost, making the remainder a risk-free trade. Minimum 3 contracts (sell 1 at 2x) or 4 contracts (sell 2 at 2x). Your own note on HAL #657 confirms: *"If I had opened 3 contracts and not 4, I would have needed to wait until the price tripled."*

### RULE 2: Never hold a 2-leg trade (Impact: flips -$117 to +$283)
If a BOT has no management plan (adjustment levels, profit targets), don't take it. Every trade should have at minimum 3 legs: entry, partial profit, final exit.

### RULE 3: Enter on Tuesdays, exit within 6-14 days (Impact: +$146 vs +$56)
Tuesday entries after Monday confirmation. Target exit around day 7-12. If not in profit by day 14, reassess. Don't hold beyond 25 days.

### RULE 4: Favor low-beta, trending names (Impact: +$231 vs -$7)
GLD, JNJ, ABBV, ABT-type names produce cleaner breakouts than AMD, TSLA, SMH. Precious metals and consumer non-cyclicals are your best sectors.

### RULE 5: Note asymmetry explicitly at entry (Impact: +$349 vs +$51)
Force yourself to write the R/R asymmetry in your remarks. If you can't articulate it, don't take the trade. Trades where you noted "asymmetry" outperform by 7x.

### RULE 6: Avoid futures and pure vertical spreads for BOT
Futures (MCL): 0% win rate, -$740 total. Spreads: 0% win rate, -$1,490 total. Breakouts need uncapped upside — use outright calls/puts, or bull call spreads where you can buy back the short leg.

### RULE 7: Pre-compute option targets using BS model
Your JNJ #644 and DOW #692 trades used BS-model projected option prices for specific spot/vol/date scenarios. This gave you concrete sell levels. Apply this systematically.

### RULE 8: Don't reposition strike without repositioning duration
Your USO #404 lesson: *"Not worth repositioning in strike if not in duration as well — as it is then a new trade."*

---

## 14. PROPOSED BOT TRADE TEMPLATE

```
ENTRY CHECKLIST:
☐ Clear breakout above/below fib zone (confirmed by Monday close)
☐ Enter on Tuesday (or Wednesday at latest)
☐ Asymmetry noted: R/R ratio > 2:1
☐ Low-to-medium beta preferred (< 1.0)
☐ Outright option (no spread, no futures)
☐ Minimum 3 contracts for partial exit plan
☐ Pre-compute BS-based sell targets for T+5, T+10, T+15

MANAGEMENT:
☐ At ~2x cost: sell enough to cover cost → risk-free
☐ Set automated partial profit orders at each fib extension
☐ If not in profit by day 10-12: tighten stop to entry cost
☐ Close before last week of expiration (your rule)
☐ Never reposition strike without also extending duration

EXIT SIGNALS:
☐ All pre-computed targets hit
☐ Price falls back inside fib zone for 2+ days
☐ Delta drops below 10-15
☐ "No more asymmetry" → close immediately
```

---

## 15. OPEN BOT TRADES ASSESSMENT (Mar 17, 2026)

| Trade | Symbol | Direction | Days In | Delta | Unrealized | Health |
|-------|--------|-----------|---------|-------|------------|--------|
| #699 | AIG | Long 3 puts 73P Apr24 | 1 | -0.30 | +$91 | Best positioned — but BPT says shorts losing conviction |
| #698 | OXY | Long 3 calls 63C Apr24 | 1 | 0.26 | -$25 | Needs active management, energy is weakest sector |
| #696 | PLTR | Long 1 put 130P Apr17 | 12 | -0.12 | -$158 | Single contract, high beta, delta fading — cut at delta 10 |
| #690 | PFE | Long 6 calls 29C Apr17 | 20 | 0.13 | -$138 | BPT confirms healthcare bullish, but delta very low |
| #691 | SAF | Bull spread 350/360 Mar20 | 29 | 0.00 | -€232 | Dead — expires worthless |
| #641 | GLD | Bull spread Oct25 | 153 | — | — | Bookkeeping — update to Fermé |
| #643 | MSF | FX hedge Apr26 | 180 | — | — | Not a BOT trade — reclassify |

### Risk-Free Targets (BS-computed)

**OXY 63C × 3 @ $1.25 → sell 1 @ $3.75 (3x)**
- T+5: OXY $63 + IV 48% → $3.79 ✅ | OXY $64 + IV 42% → $3.89 ✅
- T+10: OXY $64 + IV 45% → $3.84 ✅ | OXY $65 + any IV → ✅
- Needs breakout + IV expansion combo (JNJ/DOW pattern)

**AIG 73P × 3 @ $1.37 → sell 1 @ $4.11 (3x)**
- T+5: AIG $71 + IV 39% → $4.34 ✅ | AIG $70 + IV 33% → $4.43 ✅
- T+10: AIG $71 + IV 39% → $4.11 ✅ | AIG $70 + any IV → ✅
- BPT caution: Patrick says AIG shorts losing conviction

---

## 16. DOW-PATTERN SCREENER

### What Made DOW #692 an A+ Setup
1. **Negative VRP** (-4.1 pts): IV < RV — options cheap vs. realized movement
2. **Low IVP** (48.9%): Room for IV expansion on breakout
3. **High RVP** (75.3%): Stock already moving — momentum confirmed
4. **IVP << RVP gap** (-26.4 pts): Market hasn't priced in the movement — mispricing
5. **Technical breakout**: Bear bottom with tested rebound + macro support

### 4-Dimension IV Assessment Framework
1. **IVP** — Is IV elevated vs. own history?
2. **Peer comparison** — Is IV elevated vs. similar stocks?
3. **Term structure** — Is near-term IV elevated vs. longer tenors?
4. **Skew** — Is the skew percentile high or not?

### Screening Results (Mar 17, 2026)

| Symbol | VRP | IVP | RVP | Gap | Dim 2 (Peer VRP) | Dim 3 (Term) | Dim 4 (Skew) | Patrick |
|--------|-----|-----|-----|-----|-------------------|--------------|---------------|---------|
| **TGT** | **-2.9** | **30.2** | **62.9** | **-32.7** | Cheapest vs peers (-3.3) | Apr cheap vs May ✅ | Flat (3.6 pts) ✅ | Buy-the-dip ✅ |
| **WMT** | **-2.7** | 51.1 | 78.1 | **-26.9** | Cheap vs peers (-1.3) | Flat ⚠️ | Moderate (6 pts) | Bull continuation ✅ |
| ADM | -5.5 | 81.6 | 93.6 | -12.1 | N/A | N/A | N/A | Not mentioned |
| PG | +0.9 | 79.7 | 77.3 | +2.4 | Expensive (+2.0) | Apr cheap ✅ | Steep (8 pts) ❌ | BOT of day ✅ |

**TGT is the strongest DOW-like candidate** — wins on all 4 IV dimensions + Patrick backing + prior $729 win.

---

## 17. TGT TRADE PLAN

### Setup
- **Symbol**: TGT (Target Corp)
- **Sector**: Retail | **Beta**: 1.01
- **Price**: $116.79 (Mar 17, 2026)
- **52w range**: $83.66 – $122.33 (85.7% position)
- **Catalyst**: BPT "consolidating after profit-taking, buy-the-dip setup"
- **Prior BOT**: #678 → +$729 (Feb 2026)

### Vol Profile (4 Dimensions)
| Dimension | Value | Assessment |
|-----------|-------|------------|
| IV30 / RV30 | 31.8% / 34.7% | VRP = -2.9 → **options cheap** |
| IVP / RVP | 30.2% / 62.9% | -32.7 gap → **massive expansion room** |
| Term structure | Apr 30.8% < May 31.8% | **Near-term cheapest** |
| Skew | 3.6 pts (ITM-OTM) | **Flat — OTM calls not penalized** |

### Trade Structure (Preferred: 4 contracts)
| | Detail |
|---|---|
| **Instrument** | TGT Apr17 125 Call |
| **Entry price** | ~$1.51 (mid, Mar 17 close) |
| **Contracts** | 4 |
| **Total cost** | ~$604 |
| **Delta at entry** | 0.27 |
| **IV at entry** | 30.8% |
| **Days to expiry** | 31 (at entry) |

### Execution Plan
| Step | Action | Trigger |
|------|--------|---------|
| **Entry** | Buy 4 × TGT Apr17 125C | Tuesday, on dip confirmation holding support |
| **Target 1** | Sell 2 @ $3.02 (2x) → **risk-free** | TGT ~$121-123 (+3.6-5.3%), IV ~34-37% |
| **Target 2** | Sell 1 @ $5.10 | TGT ~$125 (strike), IV ~37% |
| **Target 3** | Sell last @ $7.00+ | TGT ~$127+, momentum peak |
| **Stop** | Cut all if TGT < $113 or delta < 10 after day 12 | |
| **Time stop** | Close before Apr 10 (last week rule) | |

### BS Target Grid (Key Scenarios)

**Risk-free bar: $3.02 per contract (sell 2 to cover $604 total cost)**

| Time | TGT Spot | IV | Call Price | x Entry | Risk-Free? |
|------|----------|-----|-----------|---------|:---:|
| T+5 | $121 | 37% | $3.23 | 2.1x | ✅ |
| T+5 | $123 | 31% | $3.32 | 2.2x | ✅ |
| T+5 | $125 | 34% | $4.70 | 3.1x | ✅ |
| T+10 | $121 | 40% | $3.08 | 2.0x | ✅ |
| T+10 | $123 | 34% | $3.23 | 2.1x | ✅ |
| T+10 | $125 | 31% | $3.85 | 2.5x | ✅ |
| T+15 | $125 | 31% | $3.34 | 2.2x | ✅ |
| T+15 | $127 | 34% | $4.79 | 3.2x | ✅ |

### Alternative: 3 contracts ($453)
- Risk-free: sell 1 @ $4.53 (3x) — needs TGT at $125 + IV 34%
- Harder bar but within budget

### Variance Strip Analysis (CBOE VIX methodology applied to TGT)

Computed via VIX Skew & Advanced Vol Metrics tool, using IBKR option chain data.

**VIX Decomposition (30-day target)**

| Metric | 2σ range | 3σ range |
|--------|:---:|:---:|
| **VIX (Combined)** | **34.1%** | **34.9%** |
| Call Component | 25.4 | 25.7 |
| Put Component | 22.8 | 23.6 |
| **Put/Call Skew Ratio** | **0.90** | **0.92** |
| Target Days | 30 | 30 |

**Term Structure**

| Term | Expiry | DTE | Variance (2σ) | Variance (3σ) | Strikes (2σ/3σ) |
|------|--------|-----|:---:|:---:|:---:|
| Near | 20260410 | 23.9 | 0.1130 | 0.1220 | 35 / 39 |
| Next | 20260417 | 30.9 | 0.1160 | 0.1220 | 8 / 12 |
| Weight | | | Near 1% / Next 99% | Near 1% / Next 99% | |

**Advanced Volatility Metrics**

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Spot/Vol Correlation | 0.128 | Near zero — vol independent of price direction |
| Vol-of-Vol (annualized) | 2.244 | Very high — extreme vol instability |
| Recent Vol-of-Vol (30d) | 2.240 | Consistent with annualized — not a spike |
| Current RV | 38.8% | Stock moving significantly |
| RV Percentile | 82% | 82nd percentile of realized movement |

**Key Findings:**

1. **Call skew (Put/Call ratio 0.90-0.92)**: Unusual — normally >1.0. Call variance exceeds put variance, indicating aggressive upside positioning. Consistent with the buy-the-dip thesis. At 3σ the ratio moves toward 0.92 as deep OTM puts (tail protection) add to the put side, but the core signal remains: smart money is buying calls.

2. **Term structure**: Contango at 2σ (near 0.1130 < next 0.1160), flattening to dead-flat at 3σ (both 0.1220). Near-term tails are priced slightly richer (short-dated OTM protection demand), but the body of the distribution confirms near-term options are cheapest.

3. **Spot/Vol correlation near zero (0.128)**: Unlike typical equities (negative correlation: price down → vol up), TGT vol can expand on a rally. This is favorable for a bullish breakout — you get the vega tailwind even on upside moves.

4. **Vol-of-Vol 2.24**: TGT's implied vol itself is highly unstable. Combined with low IVP (30%), this is the DOW pattern signature: vol is jumpy but at the bottom of its range. When it moves, it moves big.

5. **RV 38.8% at 82nd percentile vs IV 31.8% at 30th percentile**: Confirms the mispricing — the stock is moving far more than options are pricing in.

### Why This Trade
1. **DOW pattern**: Negative VRP + low IVP + high RVP = vol mispricing
2. **Patrick validation**: Explicit "buy-the-dip" call on TGT
3. **Track record**: You won +$729 on TGT BOT 6 weeks ago
4. **4-contract structure**: Enables 2x risk-free exit on modest +3.6% move
5. **All 4 IV dimensions favorable**: Cheap vs history, peers, tenors, and skew
6. **Variance strip confirms**: Call skew (0.90), near-zero spot/vol correlation, high vol-of-vol at low IVP — all point to underpriced upside
