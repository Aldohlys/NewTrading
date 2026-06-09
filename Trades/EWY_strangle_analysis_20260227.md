# EWY 120/150 Short Strangle Analysis — 2026-02-27

## Trade Setup
- **Position**: Short 120P / Short 150C, March 20 expiry
- **Opened**: Feb 19, 2026
- **Net credit**: $5.85/share ($585 per lot), 1 lot
- **Max loss budget**: 600 CHF

## Market Data (from IBKR via getVolMetrics)
- Spot: 150.40 (150C ATM)
- IV30: 62.68%, RV30: 40.04%
- IVP: 99.9, HVP: 100.0
- IV/HV ratio: 1.57 (Edge grade A), VRP: 36.1%

## Position Sizer Results

### Regime: DANGEREUX
HVP at 100 means underlying is moving as much as IV implies. Despite grade A edge (IV >> HV), the regime overrides — the premium is rich because the risk is real.

### Scenario Matrix (21 DTE, $600 max loss)

| Scenario | ES99 | VaR99 | Mean P&L | Win% | Lots |
|---|---|---|---|---|---|
| HV Base | $1,048 | $834 | −$358 | 0.5% | 0 |
| HV Adjusted | $1,512 | $1,139 | −$372 | 2.3% | 0 |
| IV Conservative | $1,578 | $1,182 | −$374 | 2.6% | 0 |

**Recommendation: 0 lots** — ES99/lot of $1,512 far exceeds $600 CHF budget.

## Roll Analysis

### Call Roll Up (150C → 155C / 160C)
- Reduces ES99 but kills credit and win rate
- 150→155: −$2.20 debit, net credit drops to $3.65
- 150→160: −$3.98 debit, net credit drops to $1.87

### Put Roll Up (120P → higher strikes)
- Put barely moved: $1.75 entry → $1.64 current ($0.11 profit)
- Not worth the friction + commission

### Combined Roll Matrix (8 configurations tested)

| Config | Put Roll | Call Roll | Net Credit | ES99 | Lots |
|--------|----------|----------|-----------|------|------|
| 120/150 (current) | — | — | $5.85 | $1,512 | 0 |
| 130/150 | +$1.23 | — | $7.08 | $1,420 | 0 |
| 135/150 | +$2.31 | — | $8.16 | $1,347 | 0 |
| 140/150 | +$3.78 | — | $9.63 | $1,256 | 0 |
| 130/155 | +$1.23 | −$2.20 | $4.88 | $1,284 | 0 |
| 135/155 | +$2.31 | −$2.20 | $5.96 | $1,213 | 0 |
| 140/155 | +$3.78 | −$2.20 | $7.44 | $1,131 | 0 |
| 135/160 | +$2.31 | −$3.98 | $4.18 | $1,083 | 0 |
| 140/160 | +$3.78 | −$3.98 | $5.65 | $1,018 | 0 |

No configuration achieved a positive lot recommendation.

## Protection Analysis (exit by March 6)

| Config | Net Credit | ES99 | Max Sim Loss | Win% |
|---|---|---|---|---|
| Naked hold | $5.85 | $3,513 | $31,913 | 45% |
| +160C Mar6 @$2.60 | $3.25 | $730 | $3,996 | 0% |
| +155C Mar6 @$4.20 | $1.65 | $536 | $4,156 | 0% |

160C protection: 80% ES99 reduction for $2.60/share. 155C offers diminishing returns at $4.20.

## Opening Price Decision Matrix

| EWY Opens | Unrealized CHF | Budget Left | Action |
|-----------|---------------|-------------|--------|
| 140 | −31 | +569 | Hold — thesis working |
| 145 | −162 | +438 | Hold — set stop at −500 CHF |
| 149 | −309 | +291 | Close or buy 160C protection |
| 151.53 | −420 | +180 | Close or buy 160C *(last close)* |
| 153 | −489 | +111 | Close — almost no room |
| 155 | −591 | +9 | Close — budget gone |
| 158+ | −757+ | negative | Close immediately |

**Key levels:**
- Budget blown: EWY ~155.20 (only $3.67 above last close)
- Breakeven: ~$138.00
- Daily 1σ move: ~$5.95

## Thesis & Catalyst Assessment

**Original thesis**: Parabolic KOSPI move will reverse hard (similar to SLV), Samsung + SK Hynix (~50% of EWY) vulnerable to NVDA weakness.

**Catalyst assessment (morning of Feb 27):**
- NVDA −5.46% → KOSPI only −1% (weak pass-through)
- NVDA pre-market +0.8% (bouncing — catalyst fading)
- KOSPI showed resilience, not fragility

## Decision: Close Position
- Unrealized loss: −439 CHF (73% of 600 CHF budget)
- Only 161 CHF headroom — cannot survive another adverse session
- Sell order placed: adaptive limit at −$10.00 debit
- Expected realized loss: ~−374 CHF (~$415 USD)

## Important Context: Sizer Approved the Trade on Feb 19

When the position sizer was run at trade entry (Feb 19), it **cleared the trade** — the regime and sizing were acceptable. By Feb 27, the same sizer on the same strangle returned 0 lots and DANGEREUX.

**What changed in 8 days:**
- EWY rallied from ~144 to 150.40 (150C went from OTM to ATM)
- HVP likely spiked to 100 as the rally itself increased realized vol
- IVP rose to 99.9 — vol regime shifted from tradeable to extreme
- The 150C moved from a comfortable OTM short to an ATM position with maximum gamma exposure

**This raises questions about the sizer:**
- The vol regime can shift rapidly — the sizer gives a point-in-time snapshot that may not reflect how quickly conditions can deteriorate
- HV/HVP are backward-looking and may lag actual regime shifts — by the time HVP hits 100, you're already in the storm
- The sizer doesn't account for directional path risk post-entry (i.e., what happens if spot moves toward a short strike)
- Potential improvement: stress-test the sizer output at entry by re-running at spot ±1σ to see how fragile the recommendation is

## Key Lessons

1. **Sizer can approve a trade that quickly becomes untenable** — the Feb 19 approval vs Feb 27 rejection shows how fast vol regimes shift
2. **Grade A edge ≠ safe trade** — IV/HV ratio of 1.57 looks great, but when HVP is 100, the premium is rich *because the risk is real*
3. **Path risk dominates** in high-vol regimes — even if the thesis is correct at expiry, surviving the interim drawdown requires budget headroom
4. **EWY-specific**: overnight KOSPI gap (9.5hr unhedgeable window) makes standard options management insufficient
5. **Mixed currency awareness**: TWS shows P&L in CHF (base), option prices in USD
6. **Catalyst assessment matters**: a −5.46% NVDA move producing only −1% KOSPI was a signal the pass-through thesis was weak
7. **Potential sizer enhancement**: run the sizer at entry not just at current spot, but also at spot ±1σ and ±2σ to stress-test the recommendation's robustness
