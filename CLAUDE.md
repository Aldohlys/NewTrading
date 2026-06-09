# Trading Strategy Advisory & Data Analysis

## Project Overview
This workspace is used for **trading strategy discussion, elaboration, and advisory** — not codebase development. Claude acts as a **trading advisor specialized in options, stocks, and futures markets**. Conversations cover market structure, strategy design, Greeks analysis, volatility dynamics, risk management, and opportunity detection.

Additionally, trading data stored in a SQLite database can be queried for empirical analysis to support strategy discussions.

## Objectives
- Discuss, elaborate, and refine trading strategies (options, stocks, futures)
- Provide advisory-level analysis on market mechanics, pricing, and mispricings
- Analyze trading patterns and metrics from SQLite database
- Generate insights and reports from trading data

## Markdown formatting rules (apply to ALL reports and chat output)

**Always escape `$` as `\$` when referring to dollar prices/amounts.**

The Claude Code / FleetView markdown renderer treats two `$` on the same line as a LaTeX math block, which garbles the text between them. Example failure (line from `Trades/CL_Jul26_breakout_analysis_20260509.md`):

> `The $25 front-end drop is a prompt-month spike (geopolitical/supply); long-dated $53`

renders as `The 25 front-end drop is a prompt-month spike (geopolitical/supply); long-dated 53` in italic math font — unreadable.

**Rule:** When writing prices, P&L, risk numbers, etc., always use `\$25`, `\$100`, `\$1,640`. This applies to:
- New trade plans, analysis reports, journal entries in `Trades/`, `Reports/`, `Discussions/`
- Section bodies, table cells, headers, bullet lists — everywhere
- Chat responses with multi-line prose

**Exception:** Single `$` per line with no closing `$` on the same line will not trigger math mode, but escape anyway for consistency — a later edit may add another `$` and silently break the line.

**Sweep before saving:** before writing a trade-plan or report file, mentally scan for any line with two or more `$` and escape them. After saving, the user has been bitten by this often enough that it's a recurring issue — bake the escape in from the start.

## Conversation History

### Initial Setup (2025-09-22)
- User inquired about Claude Code's capabilities for data analysis beyond codebases
- Confirmed Claude Code can work with various data types including:
  - Structured data (databases, JSON, CSV)
  - Unstructured data (notes, journals, logs)
  - Mixed content types
- Identified focus: Trading data analysis from SQLite database

### Completed Analysis
- ✅ Database structure examination (29 tables identified)
- ✅ Strategy performance analysis (29 unique strategies)
- ✅ Performance metrics calculation (P&L, win rates, risk assessment)
- ✅ Comprehensive strategy report generated

### Analysis Results Summary
**Performance Analysis by Strategy (2025-09-22)**
- **Total Strategies**: 29 unique strategies across 2,039 trades
- **Top Performer**: BOT ($5,958.73 total P&L, 223 trades)
- **Highest Win Rate**: IWM (50%), CS SPY (45.5%)
- **Largest Volume**: OFI (706 trades, 34.6% of total)
- **Biggest Loser**: LTO (-$7,752.25, 6.5% win rate)

**Key Insights**:
- TBILL shows excellent risk-adjusted returns (40% win rate, no losses)
- OFI strategy has high volume but minimal profitability
- Several strategies (LTO, BPT, A14) show consistent underperformance
- Detailed report: `strategy_performance_report.md`

### BOT Strategy Deep Dive (2025-09-22)
**Analysis of 223 BOT trades revealing key success/failure patterns:**

**🎯 Critical Success Factors:**
- **Asymmetry Recognition**: Best trades ($1,692, $1,633) closed when "no asymmetry left"
- **Progressive Exits**: Winners used staged profit-taking vs all-or-nothing
- **Position Sizing**: Short 1-5 contracts avg +$79.56, larger sizes avg -$160+
- **Technical Discipline**: Respected Fibonacci zones and support/resistance levels

**⚠️ Major Failure Patterns:**
- **Discipline Breakdown**: "Should have closed earlier, I was lazy" (-$324 loss)
- **IV Crush Vulnerability**: SPY trade lost $997 from 17% → 13% IV drop
- **Repositioning Errors**: "Not worth repositioning strike without duration"
- **Oversizing**: Positions >5 contracts consistently underperformed

**📊 Performance by Asset Class:**
- **Metals** (GLD/GOLD/SLV): +$1,147 avg - best trending behavior
- **Tech** (AAPL): +$305 avg - clear technical patterns
- **Commodities** (MCL): Problematic due to sizing and stops
- **Detailed analysis**: `bot_analysis.md`

### Technical Notes
- **TWS mixed currencies**: P&L displayed in base currency (CHF), option prices in USD
- **EWY/KOSPI gap risk**: KOSPI trades 12am-6am CET, US options open 3:30pm CET — 9.5hr unhedgeable window
- **Position sizer**: `RApplication/Tdata/inst/python/tdata_py/position_sizer.py`
  - Import directly via `importlib.util.spec_from_file_location`, not through package `__init__.py` (avoids dependency chain)
  - Vol metrics from DB: `SELECT * FROM Prices WHERE sym = ? AND iv30 IS NOT NULL ORDER BY ROWID DESC LIMIT 1`
  - Algorithm summary: `position_sizer_summary.md`

### Generated Reports
- `strategy_performance_report.md` — strategy performance analysis
- `bot_analysis.md` — BOT strategy deep dive
- `position_sizer_summary.md` — position sizer algorithm documentation
- `EWY_strangle_analysis_20260227.md` — EWY 120/150 strangle trade analysis

### Next Steps
- Apply BOT insights to other strategies (LTO, BPT analysis)
- Risk management analysis (drawdown, risk/reward ratios)
- Account-specific performance comparison
- Journal sentiment correlation with performance

## Database Information
- Format: SQLite database
- Content: Trading data
- Location: `C:\Users\aldoh\Documents\RApplication\data\mydb.db`

### Database Structure
**Main Tables:**
- **Trades** (2,039 records): Core trading data with fields:
  - TradeNr, Account, TradeDate, Strategy, Instrument
  - Position details: Pos, Prix, Comm., Total
  - Risk management: Exp.Date, Risk, Reward, PnL
  - Status and notes: Statut, Currency, Remarques

- **Journal** (1,405 entries): Trading journal with fields:
  - entryId, theme, date, sym (symbol)
  - Market data: close, change, mkt_price, mkt_change
  - text (journal notes/observations)

**Other Tables:**
- Account, AccountWithConversionRate, Prices, Strategies
- Currency conversion: ConvertToCHF, ConvertToUSD, Currencies
- Account-specific: DU5221795, U1804173, Gonet
- Testing: TestPortf, TestTrades
- Reference: Tickers, Param

## Analysis Tools
- SQLite for database queries
- Claude Code for analysis and automation
- Export capabilities for various formats (CSV, JSON)