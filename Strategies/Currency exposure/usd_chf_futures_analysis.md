# USD/CHF Futures Analysis - Risk Assessment

## Project Context
Analysis of CME Micro Swiss Franc/U.S. Dollar futures position using historical USD/CHF volatility data from SQLite database.

## Position Details
- **Contract**: CME Micro Swiss Franc/USD Futures (CHF/USD)
- **Contract Size**: 12,500 CHF per contract
- **Tick Size**: 0.0001 USD per CHF
- **Tick Value**: $1.25 per tick per contract
- **Position**: 3 contracts
- **Total Exposure**: 37,500 CHF

## USD/CHF Average True Range Analysis

### Overall ATR Statistics
- **Average True Range**: 0.0034 (0.34%)
- **Data Period**: January 4, 2021 to September 14, 2025 (1,200 trading days)
- **Range**: 0.0000 to 0.0346

### ATR Percentile Distribution

| Percentile | ATR Value | Percentage | Ticks | Value per Contract | 3-Contract Position |
|------------|-----------|------------|-------|-------------------|---------------------|
| 10th       | 0.0005    | 0.05%      | 5     | $6.25            | ±$18.75            |
| 20th       | 0.0009    | 0.09%      | 9     | $11.25           | ±$33.75            |
| 30th       | 0.0014    | 0.14%      | 14    | $17.50           | ±$52.50            |
| 40th       | 0.0019    | 0.19%      | 19    | $23.75           | ±$71.25            |
| 50th (Median) | 0.0027 | 0.27%      | 27    | $33.75           | ±$101.25           |
| 60th       | 0.0033    | 0.33%      | 33    | $41.25           | ±$123.75           |
| 70th       | 0.0042    | 0.42%      | 42    | $52.50           | ±$157.50           |
| 80th       | 0.0053    | 0.53%      | 53    | $66.25           | ±$198.75           |
| 90th       | 0.0071    | 0.71%      | 71    | $88.75           | ±$266.25           |
| 100th      | 0.0346    | 3.46%      | 346   | $432.50          | ±$1,297.50         |

## Current Position Valuation

### Contract Value Calculation
If current USD/CHF rate is 0.9000:
- **Current value per contract**: 0.9000 × 12,500 = $11,250
- **Total position value**: $11,250 × 3 = **$33,750**

### Tick Value Impact
- **Dollar value per tick per contract**: 0.0001 × 12,500 = **$1.25**
- **Dollar value per tick for 3 contracts**: $1.25 × 3 = **$3.75**

## Today's Performance Analysis

### Actual Trading Result
- **Tick Move**: -62 ticks
- **Loss per Contract**: 62 ticks × $1.25 = **-$77.50**
- **Total Position Loss**: -$77.50 × 3 contracts = **-$232.50**

### Volatility Context
Today's 62-tick move represents:
- **Volatility Rank**: ~85th percentile (between 80th and 90th percentiles)
- **Comparison to Typical**: 2.3x the typical daily movement (27 ticks)
- **Assessment**: High volatility day but not extreme
- **Frequency**: Such moves occur roughly 15-20% of trading days

## Risk Management Analysis

### $600 Daily Loss Limit Assessment
**Risk Calculation:**
- **Loss Threshold**: $600 ÷ $3.75 per tick = **160 ticks**
- **Historical Probability**: **0.83%** (10 days out of 1,200 trading days)
- **Frequency**: Roughly **1 in every 120 trading days**
- **Annual Expectation**: ~2 days per year (assuming 250 trading days)

### Historical $600+ Loss Days
The 10 occurrences of 160+ tick moves:
- 2022-06-16, 2022-11-07, 2022-11-11, 2022-11-14
- 2023-03-16
- 2024-08-04
- 2025-01-17, 2025-04-03, 2025-04-10, 2025-04-22

**Pattern Observed**: Clustering during market stress periods (Nov 2022, Apr 2025)

### Risk Summary
- **Very Low Probability**: Less than 1% chance daily of exceeding $600 loss
- **Today's Context**: At 62 ticks (-$232.50), position was at 39% of $600 threshold
- **Typical Daily Risk**: ±$127.50 (based on average ATR of 34 ticks)

## Key Insights

### Volatility Characteristics
- **Median daily volatility**: 0.27% (typical daily move)
- **High volatility threshold**: Above 0.71% (90th percentile)
- **Extreme volatility**: 3.46% maximum daily move observed
- **Low volatility**: Below 0.19% (40th percentile and below)

### Position Management Considerations
1. **Liquidity Concern**: Contract volume may be limited for position adjustments
2. **Risk Tolerance**: $600 daily loss limit provides good buffer (0.83% probability)
3. **Typical Exposure**: Daily P&L swings of ±$128 are normal
4. **Extreme Risk**: Maximum observed loss potential of $1,298 in crisis conditions

## Data Source
Analysis based on ConvertToCHF table from trading database:
- **Database**: `C:\Users\aldoh\Documents\RApplication\data\mydb.db`
- **Table**: ConvertToCHF (USD currency records)
- **Period**: January 2021 - September 2025
- **Records**: 1,200 daily observations

---
*Analysis generated using Claude Code on 2025-09-24*
*Contract specifications sourced from CME Group Rulebook Chapter 295*