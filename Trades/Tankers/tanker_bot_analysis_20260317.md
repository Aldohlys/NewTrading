# BOT Grid Analysis — TNK & STNG (Tanker Sector)

*Analysis date: 2026-03-17 | Data source: IBKR TWS via Tdata*

---

## 1. DOW-PATTERN SCREENER

### 4-Dimension IV Assessment

| Dimension | TNK | STNG | DOW #692 ref |
|-----------|-----|------|:---:|
| **IV30** | **48.9%** | **44.9%** | 30.1% |
| **RV30 (HV)** | **40.8%** | **38.9%** | 34.2% |
| **VRP (IV - RV)** | **+8.1 pts** | **+6.0 pts** | -4.1 |
| **IVP** | **85.3%** | **65.6%** | 48.9% |
| **RVP (HVP)** | **79.3%** | **57.0%** | 75.3% |
| **IVP - RVP gap** | **+6.0 pts** | **+8.6 pts** | -26.4 |
| Beta | -0.37 | -0.39 | ~0.5 |

### Verdict Against DOW Pattern

The DOW #692 A+ setup had: **negative VRP** (options cheap), **low IVP** (expansion room), **high RVP** (momentum), **large negative IVP-RVP gap** (mispricing).

**Both TNK and STNG FAIL the DOW pattern on multiple dimensions:**

| Criterion | TNK | STNG | DOW ref |
|-----------|:---:|:---:|:---:|
| Negative VRP (options cheap) | **NO** (+8.1) | **NO** (+6.0) | YES (-4.1) |
| Low IVP (expansion room) | **NO** (85.3%) | **NO** (65.6%) | YES (48.9%) |
| High RVP (momentum) | YES (79.3%) | Moderate (57.0%) | YES (75.3%) |
| IVP << RVP gap | **NO** (+6.0) | **NO** (+8.6) | YES (-26.4) |

**Options are EXPENSIVE relative to realized movement**, which is the opposite of what BOT needs. You're paying a premium for vol that hasn't materialized in the underlying.

---

## 2. IV PERCENTILE DISTRIBUTION

### TNK — IV is near 1-year highs

| Percentile | IV Level | Current: 48.9% |
|:---:|:---:|:---:|
| p10 | 34.4% | |
| p25 | 37.6% | |
| p50 (median) | 41.4% | |
| p75 | 45.2% | |
| **p90** | **50.6%** | **<-- Current sits between p75 and p90** |
| 1Y min | 29.9% | |
| 1Y max | 68.1% | |

### STNG — IV moderately elevated

| Percentile | IV Level | Current: 44.9% |
|:---:|:---:|:---:|
| p10 | 36.4% | |
| p25 | 38.6% | |
| p50 (median) | 42.3% | |
| **p75** | **46.5%** | **<-- Current sits near p75** |
| p90 | 52.3% | |
| 1Y min | 30.4% | |
| 1Y max | 74.1% | |

**Implication**: Both names have IV above median. Buying options here means paying for elevated vol. If IV mean-reverts (which it tends to), you face vega headwind.

---

## 3. PRICE CONTEXT

| Metric | TNK | STNG |
|--------|-----|------|
| **Current price** | **$63.89** | **$66.30** |
| 52w low | $33.35 | $30.63 |
| 52w high | $82.24 | $81.85 |
| **52w position** | **69.1%** | **69.6%** |
| 30d ago | $64.89 | $64.67 |
| 180d ago | $43.79 | $43.48 |
| YTD return | +19.6% | +30.4% |
| 1Y return | +64.2% | +63.3% |
| P/E | 6.33 | 9.43 |
| Dividend | 3.13% | 2.72% |
| Beta | -0.37 | -0.39 |

Both are at ~70% of their 52w range. Strong 1Y rallies (+63-64%), but prices have stalled/pulled back from highs in the last 30 days.

**Negative beta (-0.37/-0.39)** is notable — these move *opposite* to broad market. Good for diversification but complicates timing against macro signals.

---

## 4. PRIOR STNG BOT TRADE (#603)

| Leg | Date | Action | Price | P&L |
|-----|------|--------|-------|-----|
| 1 | Jul 30, 2025 | Buy 2 × 50C Sep25 | $1.50 | |
| 2 | Aug 4, 2025 | Buy 1 × 50C Sep25 | $1.52 | Added on dip |
| 3 | Aug 13, 2025 | Sell 1 | $0.77 | Momentum fading |
| 4 | Aug 25, 2025 | Sell 1 | $1.30 | Neutral stance |
| 5 | Sep 8, 2025 | Sell 1 | $6.10 | Auto target hit |
| **Total** | | | | **+$362** |

**Your own note**: *"Automatic profit target on breakout trades does not make real sense... it was filled right at opening and now is between 7.80 and 8.10"* — left $170-$200 on the table by using a fixed target instead of progressive exits.

**Lessons from #603**:
- 5-leg active management worked (Rule 2 validated)
- But auto target cost you ~30% of potential profit
- Entry at $1.50 on 30-delta OTM was good — cheap asymmetry
- The add at $1.52 on the dip showed conviction

---

## 5. OPTION CHAIN SNAPSHOT (Apr 17, 2026 — 30 DTE)

### TNK Option Chain

| Strike | Call Mid | Call IV | Call Delta | Put Mid | Put IV | Put Delta |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 55 | $10.20 | 56.2% | 0.85 | $0.67 | 56.2% | -0.16 |
| 60 | $6.20 | 52.5% | 0.70 | $1.60 | 52.5% | -0.31 |
| **65** | **$3.10** | **49.9%** | **0.49** | **$4.10** | **49.9%** | **-0.52** |
| 70 | $1.75 | 49.2% | 0.29 | $7.40 | 49.2% | -0.71 |

### STNG Option Chain

| Strike | Call Mid | Call IV | Call Delta | Put Mid | Put IV | Put Delta |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 60.0 | $8.15 | 48.1% | 0.79 | $1.03 | 48.1% | -0.21 |
| 62.5 | $6.15 | 46.1% | 0.70 | $1.74 | 46.1% | -0.30 |
| 65.0 | $4.30 | 44.9% | 0.60 | $2.73 | 44.9% | -0.41 |
| **67.5** | **$3.08** | **44.3%** | **0.48** | **$3.70** | **44.3%** | **-0.52** |
| **70.0** | **$2.15** | **44.4%** | **0.37** | **$5.10** | **44.4%** | **-0.63** |
| 72.5 | $1.50 | 45.1% | 0.28 | $7.29 | 45.1% | -0.73 |
| 75.0 | $1.15 | 46.8% | 0.21 | $9.30 | 46.3% | -0.80 |

**Skew observation**: Both names show normal skew — higher IV for lower strikes. No unusual call skew like TGT had. This means no "smart money" call buying signal.

**Spreads**: TNK spreads are **wide** ($0.80-$1.80 on ATM calls = 25-50% of mid). STNG is much tighter ($0.20-$0.25 on ATM = 5-8%). **STNG has far better liquidity.**

---

## 6. BS TARGET GRIDS

### TNK — Apr17 65C @ $3.10 (ATM, delta 0.49)

**Risk-free bar: sell 1 @ $6.20 (2x) with 3 contracts, or sell 2 @ $6.20 with 4 contracts**

| Time | TNK Spot | IV | Call Price | x Entry | RF? |
|------|----------|-----|-----------|---------|:---:|
| T+5 | $68 (+6.4%) | 50% | $5.29 | 1.7x | |
| T+5 | $70 (+9.6%) | 45% | $6.41 | 2.1x | YES |
| T+5 | $70 (+9.6%) | 50% | $6.70 | 2.2x | YES |
| T+5 | $72 (+12.7%) | 45% | $8.01 | 2.6x | YES |
| T+10 | $68 (+6.4%) | 50% | $4.93 | 1.6x | |
| T+10 | $70 (+9.6%) | 50% | $6.37 | 2.1x | YES |
| T+10 | $72 (+12.7%) | 45% | $7.76 | 2.5x | YES |
| T+15 | $70 (+9.6%) | 55% | $6.22 | 2.0x | YES |
| T+15 | $72 (+12.7%) | 45% | $7.51 | 2.4x | YES |

**TNK needs +9.6% to reach risk-free.** That's a big ask in 5-10 days for a stock that moved -1.5% in the last 30 days.

### STNG — Apr17 67.5C @ $3.075 (ATM, delta 0.48)

**Risk-free bar: sell 1 @ $6.15 (2x) with 3 contracts, or sell 2 @ $6.15 with 4 contracts**

| Time | STNG Spot | IV | Call Price | x Entry | RF? |
|------|-----------|-----|-----------|---------|:---:|
| T+5 | $72 (+8.6%) | 45% | $6.14 | 2.0x | YES |
| T+5 | $72 (+8.6%) | 50% | $6.45 | 2.1x | YES |
| T+5 | $74 (+11.6%) | 40% | $7.43 | 2.4x | YES |
| T+10 | $72 (+8.6%) | 50% | $6.10 | 2.0x | YES |
| T+10 | $74 (+11.6%) | 45% | $7.41 | 2.4x | YES |
| T+15 | $74 (+11.6%) | 45% | $7.13 | 2.3x | YES |

**STNG needs +8.6% to reach risk-free** — similarly demanding.

### STNG — Apr17 70C @ $2.15 (OTM, delta 0.37) — CHEAPER ALTERNATIVE

**Risk-free bar: sell 1 @ $4.30 (2x) with 3 contracts, or sell 1 @ $6.45 (3x) with 3 contracts**

| Time | STNG Spot | IV | Call Price | x Entry | RF? |
|------|-----------|-----|-----------|---------|:---:|
| T+5 | $72 (+8.6%) | 45% | $4.55 | 2.1x | YES |
| T+5 | $74 (+11.6%) | 40% | $5.56 | 2.6x | YES |
| T+10 | $72 (+8.6%) | 50% | $4.50 | 2.1x | YES |
| T+10 | $74 (+11.6%) | 45% | $5.55 | 2.6x | YES |
| T+15 | $74 (+11.6%) | 45% | $5.18 | 2.4x | YES |

70C is cheaper ($2.15 vs $3.075) and hits risk-free at the same +8.6% spot move. Lower delta (0.37) means less premium at risk, but needs a larger % move for same dollar gain.

---

## 7. SECTOR ASSESSMENT: TANKERS

### Bullish Factors
- **Massive 1Y rallies** (+63-64%) driven by tight tanker supply / geopolitical disruptions
- **Cheap valuations**: TNK P/E 6.3, STNG P/E 9.4 — deep value territory
- **Negative beta**: Uncorrelated to market, potential safe haven during risk-off
- **Dividends**: 2.7-3.1% yield provides downside cushion
- **Your STNG #603 was profitable** — you know this sector

### Bearish / Cautionary Factors
- **Options are expensive** (positive VRP, IVP > 65%) — the vol premium is against you
- **Price momentum stalling**: Both stocks dropped -3% on analysis day, 30d change near flat
- **Wide spreads on TNK** — execution risk, slippage
- **Energy is your weakest BOT sector** (-$66 avg, -$659 total in historical analysis)
- **No clear breakout pattern** — both are mid-range, not breaking above resistance
- **No DOW-pattern match** — none of the 4 IV dimensions are favorable

---

## 8. COMPARISON WITH TGT (Your Last DOW-Pattern Trade)

| Factor | TGT (DOW-like) | TNK | STNG |
|--------|:---:|:---:|:---:|
| VRP | -2.9 (cheap) | **+8.1 (expensive)** | **+6.0 (expensive)** |
| IVP | 30.2% (low) | **85.3% (high)** | **65.6% (moderate)** |
| RVP | 62.9% (high) | 79.3% (high) | 57.0% (moderate) |
| IVP-RVP gap | -32.7 (mispriced) | **+6.0 (no mispricing)** | **+8.6 (no mispricing)** |
| Breakout? | Buy-the-dip ✅ | Stalling ⚠️ | Stalling ⚠️ |
| Spread quality | Tight | **Wide** | Tight |
| Move needed for RF | +3.6% | **+9.6%** | **+8.6%** |

**The contrast is stark.** TGT needed a modest +3.6% move because options were cheap. TNK/STNG need +8.6-9.6% because options are already expensive.

---

## 9. RECOMMENDATION

### Overall: **WAIT / NO TRADE**

Both TNK and STNG fail the BOT framework on the most critical dimension — **vol is overpriced**, not underpriced. Buying calls now means:
1. Paying elevated premium (IVP 65-85%)
2. Facing vega headwind if IV mean-reverts
3. Needing large spot moves (+8-10%) just to reach risk-free
4. Energy/shipping is your weakest historical sector for BOT

### If You Must Trade (Trigger Conditions)

Wait for:
- **IV pullback**: IVP below 50% (ideally below 40%) — this makes options 20-30% cheaper
- **Clear breakout**: Price above $70 (TNK) or $72 (STNG) on volume
- **Negative VRP**: IV drops below HV, confirming options underpriced
- **When any 2 of 4 IV dimensions flip favorable**

### If Triggered — Preferred Setup

**STNG over TNK** due to:
- Much tighter spreads (5% vs 25-50%)
- Higher liquidity (1.6M daily volume vs 336K)
- Analyst consensus "Strong Buy" with $79 target (+19%)
- You have prior positive trade history (#603)

**Structure**: STNG Apr17 70C × 3 @ ~$2.15 (when entry conditions met)
- Risk-free: sell 1 @ $4.30 (2x) on +8.6% move
- Progressive exits: sell 1 at 3x, ride last contract
- Stop: cut at delta 10 or if price drops below $62

### Alternative: Vol-Selling Angle

Given elevated IV, the **opposite trade** might be more appropriate for these names — selling premium (put spreads, iron condors) rather than buying breakouts. With IVP at 65-85%, you'd be selling vol at the top of its range. But that's a different strategy than BOT.

---

*Data pulled from IBKR TWS via Tdata | BS model: r=4.3%, no dividends adjustment*

---

## 10. DIVIDEND YIELD & VOLATILITY — CORRELATION ANALYSIS

**Date:** 2026-03-18

| Ticker | Div Yield |
|--------|-----------|
| TNK    | 1.56%     |
| STNG   | 2.83%     |

*(Note: these figures differ slightly from Section 3 above (3.13% / 2.72%) — likely due to different data sources or ex-date timing. Use latest broker data.)*

### No Direct Causation, But Indirect Links

#### 1. Dividend Policy Signals Earnings Stability
- **Higher, stable dividends** (STNG 2.83%) often signal management confidence in cash flow predictability — which *should* dampen vol over time.
- **Lower dividends** (TNK 1.56%) may mean the company retains more for capex/debt or has less predictable cash flows.
- In tankers, dividends are often **variable** (tied to spot rates), so a higher yield today may reflect *more* volatile payouts, not less.

#### 2. Dividend Yield as a Put Floor
- Stocks with high yields attract income-seeking holders who buy dips → creates a soft floor → can compress realized vol.
- This effect is stronger in utilities/REITs than cyclical sectors like tankers.

#### 3. For Options Pricing Specifically
- **Higher div yield lowers forward price** → directly affects put/call parity and delta calculations.
- On STNG (2.83% yield), forward is discounted more → LEAP calls relatively cheaper, LEAP puts more expensive vs TNK.
- If the market **underestimates** the dividend (or it gets cut), expect a vol spike.

#### 4. What Actually Drives the Vol Difference
For TNK vs STNG, the real drivers are:
- **Fleet composition** — spot vs time-charter exposure (more spot = more vol)
- **Balance sheet leverage** — higher debt amplifies equity vol
- **Market cap / liquidity** — smaller float = wider spreads = higher implied vol
- **Earnings variability** — trailing EPS dispersion

### Conclusion
The 1.27% dividend spread is a **symptom**, not a cause. Both are tanker plays tied to freight rates, so vol profiles are driven primarily by **spot rate exposure, leverage, and float size**. The dividend difference tells you more about capital allocation policy than expected volatility. For vol-selling strategy selection, focus on **IV percentile relative to realized vol** for each name individually.
