# Regime Backtest — Sigmoid Calibration Results

Date: 2026-03-19
Strategy: BOT | Trades: 98 (W:39 L:59) | Period: 2022-07-21 to 2026-03-02
Overall win rate: 39.8%

## Signal Calibration

| Signal | Current Center | Cal. Center | Current Scale | Cal. Scale | Tercile Win Rates | N | Note |
|--------|---------------|-------------|---------------|------------|-------------------|---|------|
| vix_stress | 25.00 | 16.38 | 4.00 | 0.96 | low=39% mid=44% high=36% | 98 | OK |
| vix_calm | 20.00 | 16.38 | 3.00 | 0.96 | low=39% mid=44% high=36% | 98 | OK |
| backwardation | 0.10 | 0.10 | 0.05 | 0.02 | low=36% mid=41% high=42% | 98 | OK |
| rates_press | 4.50 | 4.14 | 0.30 | 0.07 | low=36% mid=38% high=45% | 98 | OK |
| dxy_strength | 2.00 | -0.53 | 1.50 | 0.57 | low=39% mid=41% high=39% | 98 | OK |
| tlt_bid | 1.00 | -0.43 | 1.50 | 1.01 | low=39% mid=38% high=42% | 98 | OK |
| credit_stress | 1.00 | -1.00 | 1.00 | 0.32 | low=36% mid=44% high=39% | 98 | OK |
| copper_gold | 0.00 | 1.47 | 2.00 | 1.55 | low=30% mid=41% high=48% | 98 | OK |

## Regime Performance

| Regime | N | Wins | Win% | Avg P&L | Total P&L | Avg Hold |
|--------|---|------|------|---------|-----------|----------|
| liquidity_stress | 2 | 1 | 50.0% | $684.12 | $1368.23 | 11.5 days |
| neutral | 96 | 38 | 39.6% | $83.89 | $8053.13 | 17.1 days |

## Directional Flow Probability Bands

| Band | N | Win% | Avg P&L |
|------|---|------|---------|
| <30% | 18 | 33.3% | $152.81 |
| 30-40% | 80 | 41.2% | $83.38 |

## Liquidity Stress Probability Bands

| Band | N | Win% | Avg P&L |
|------|---|------|---------|
| 25-35% | 96 | 39.6% | $83.89 |
| 35-50% | 2 | 50.0% | $684.12 |

## Signal Quintile Analysis

### vix_stress

| Quintile | N | Win% | Avg P&L |
|----------|---|------|---------|
| Q1 | 20 | 40.0% | $161.39 |
| Q2 | 19 | 42.1% | $82.59 |
| Q3 | 21 | 47.6% | $112.34 |
| Q4 | 18 | 38.9% | $4.12 |
| Q5 | 20 | 30.0% | $109.56 |

### vix_calm

| Quintile | N | Win% | Avg P&L |
|----------|---|------|---------|
| Q1 | 20 | 30.0% | $109.56 |
| Q2 | 21 | 42.9% | $53.49 |
| Q3 | 18 | 44.4% | $72.78 |
| Q4 | 19 | 42.1% | $82.59 |
| Q5 | 20 | 40.0% | $161.39 |

### backwardation

| Quintile | N | Win% | Avg P&L |
|----------|---|------|---------|
| Q1 | 20 | 35.0% | $85.04 |
| Q2 | 19 | 42.1% | $170.39 |
| Q3 | 20 | 40.0% | $23.60 |
| Q4 | 19 | 31.6% | $83.73 |
| Q5 | 20 | 50.0% | $121.01 |

### rates_press

| Quintile | N | Win% | Avg P&L |
|----------|---|------|---------|
| Q1 | 20 | 35.0% | $0.41 |
| Q2 | 19 | 47.4% | $274.45 |
| Q3 | 20 | 35.0% | $12.15 |
| Q4 | 19 | 42.1% | $147.60 |
| Q5 | 20 | 40.0% | $57.56 |

### dxy_strength

| Quintile | N | Win% | Avg P&L |
|----------|---|------|---------|
| Q1 | 20 | 30.0% | $-18.80 |
| Q2 | 19 | 57.9% | $239.69 |
| Q3 | 20 | 40.0% | $62.66 |
| Q4 | 19 | 42.1% | $217.56 |
| Q5 | 20 | 30.0% | $-7.18 |

### reflation

| Quintile | N | Win% | Avg P&L |
|----------|---|------|---------|
| Q1 | 20 | 40.0% | $108.72 |
| Q2 | 19 | 57.9% | $332.50 |
| Q3 | 20 | 50.0% | $90.94 |
| Q4 | 19 | 31.6% | $27.00 |
| Q5 | 20 | 20.0% | $-70.12 |

### tlt_bid

| Quintile | N | Win% | Avg P&L |
|----------|---|------|---------|
| Q1 | 20 | 45.0% | $117.43 |
| Q2 | 19 | 42.1% | $165.51 |
| Q3 | 20 | 35.0% | $54.56 |
| Q4 | 19 | 36.8% | $113.92 |
| Q5 | 20 | 40.0% | $33.61 |

### credit_stress

| Quintile | N | Win% | Avg P&L |
|----------|---|------|---------|
| Q1 | 20 | 40.0% | $118.36 |
| Q2 | 19 | 42.1% | $45.73 |
| Q3 | 20 | 30.0% | $-31.13 |
| Q4 | 19 | 42.1% | $105.42 |
| Q5 | 20 | 45.0% | $240.25 |

### copper_gold

| Quintile | N | Win% | Avg P&L |
|----------|---|------|---------|
| Q1 | 20 | 35.0% | $104.05 |
| Q2 | 19 | 36.8% | $73.26 |
| Q3 | 20 | 30.0% | $-0.78 |
| Q4 | 19 | 42.1% | $96.72 |
| Q5 | 20 | 55.0% | $206.31 |

### sentiment

| Quintile | N | Win% | Avg P&L |
|----------|---|------|---------|
| Q1 | 20 | 35.0% | $119.33 |
| Q2 | 19 | 42.1% | $78.77 |
| Q3 | 21 | 47.6% | $163.53 |
| Q4 | 18 | 44.4% | $72.16 |
| Q5 | 20 | 30.0% | $40.27 |

## Signal Predictive Power

| Signal | Corr with Win | Avg (Win) | Avg (Loss) | Diff |
|--------|--------------|-----------|------------|------|
| vix_stress | -0.020 | 0.160 | 0.167 | -0.007 |
| vix_calm | +0.043 | 0.692 | 0.672 | +0.020 |
| backwardation | +0.059 | 0.548 | 0.521 | +0.027 |
| rates_press | -0.018 | 0.274 | 0.279 | -0.005 |
| dxy_strength | -0.000 | 0.218 | 0.218 | -0.000 |
| reflation | -0.145 | 0.463 | 0.503 | -0.041 |
| tlt_bid | -0.058 | 0.403 | 0.441 | -0.038 |
| credit_stress | +0.014 | 0.251 | 0.245 | +0.005 |
| copper_gold | +0.161 | 0.459 | 0.351 | +0.109 |
| sentiment | +0.031 | 0.625 | 0.615 | +0.010 |

## Limitations

- **No S5FI (breadth) data**: breadth_bull and breadth_bear signals could not be calibrated.
  The breadth calculation requires live scraping of 500+ tickers and is not available historically.
  Proxy: consider using RSP/SPY relative performance or MMFI index if available.
- **No COT/positioning data**: positioning stress modifier not backtested.
- **No catalyst/event data**: catalyst boost not backtested.
- **Regime inertia**: not applied in backtest (no sequential regime state).
- **Sample size**: 98 trades is small for 10 parameter calibrations. Treat results as directional, not definitive.
- **Survivorship**: only closed trades included; open trades excluded.
