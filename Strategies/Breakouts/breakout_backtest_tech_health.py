import sqlite3
import pandas as pd
import numpy as np

conn = sqlite3.connect(r"C:\Users\aldoh\Documents\RApplication\data\mydb.db")

# Get all sectors and find Tech/Healthcare tickers
tickers_df = pd.read_sql("SELECT Symbol as ticker, Sector as sector FROM ScannerUniverse WHERE IsActive = 1", conn)

# Filter to Tech and Healthcare
relevant = tickers_df[tickers_df.sector.isin(['Technology', 'Healthcare'])]
print("Sectors found:", relevant.sector.unique())
print("Relevant tickers:", len(relevant))
print(relevant.groupby('sector').ticker.apply(list))

# Get OHLCV data
tickers_list = relevant.ticker.tolist()
placeholders = ','.join(['?'] * len(tickers_list))
ohlcv = pd.read_sql(
    "SELECT date, ticker, Open, High, Low, Close, Volume FROM mrbreakouts_cache WHERE ticker IN ({}) ORDER BY ticker, date".format(placeholders),
    conn, params=tickers_list
)

print("Total rows: {}, tickers: {}".format(len(ohlcv), ohlcv.ticker.nunique()))

# Breakout detection - STRICT criteria
results = []
for tkr in ohlcv.ticker.unique():
    df = ohlcv[ohlcv.ticker == tkr].sort_values('date').reset_index(drop=True)
    if len(df) < 55:
        continue

    for i in range(50, len(df)):
        window_20 = df.iloc[i-20:i]
        window_40 = df.iloc[i-40:i]
        window_50 = df.iloc[i-50:i]
        today = df.iloc[i]
        yesterday = df.iloc[i-1]

        range_20 = window_20.High.max() - window_20.Low.min()
        range_40 = window_40.High.max() - window_40.Low.min()
        if range_40 == 0:
            continue
        squeeze_ratio = range_20 / range_40

        vol_20 = window_20.Volume.mean()
        vol_50 = window_50.Volume.mean()
        if vol_50 == 0:
            continue
        vol_ratio = vol_20 / vol_50

        low_20 = window_20.Low.min()
        high_20 = window_20.High.max()
        if high_20 == low_20:
            continue
        rng_pct = (today.Close - low_20) / (high_20 - low_20)

        daily_return = (today.Close - yesterday.Close) / yesterday.Close
        near_high = today.Close >= high_20 * 0.995

        vol_surge = today.Volume >= vol_20 * 1.2

        is_breakout = (squeeze_ratio < 0.65 and
                       vol_ratio < 0.90 and
                       rng_pct >= 0.65 and
                       daily_return >= 0.015 and
                       near_high and
                       vol_surge)

        if is_breakout:
            ret_5d = ret_10d = ret_15d = ret_20d = max_ret_20d = max_dd_20d = None

            if i + 5 < len(df):
                ret_5d = (df.iloc[i+5].Close - today.Close) / today.Close * 100
            if i + 10 < len(df):
                ret_10d = (df.iloc[i+10].Close - today.Close) / today.Close * 100
            if i + 15 < len(df):
                ret_15d = (df.iloc[i+15].Close - today.Close) / today.Close * 100
            if i + 20 < len(df):
                ret_20d = (df.iloc[i+20].Close - today.Close) / today.Close * 100
            if i + 20 < len(df):
                future_highs = df.iloc[i+1:i+21].High.max()
                max_ret_20d = (future_highs - today.Close) / today.Close * 100
                future_lows = df.iloc[i+1:i+21].Low.min()
                max_dd_20d = (future_lows - today.Close) / today.Close * 100
            elif i + 1 < len(df):
                future_highs = df.iloc[i+1:].High.max()
                max_ret_20d = (future_highs - today.Close) / today.Close * 100
                future_lows = df.iloc[i+1:].Low.min()
                max_dd_20d = (future_lows - today.Close) / today.Close * 100

            results.append({
                'ticker': tkr,
                'sector': relevant[relevant.ticker == tkr].sector.values[0],
                'date': int(today.date),
                'close': round(today.Close, 2),
                'daily_ret': round(daily_return * 100, 2),
                'squeeze_ratio': round(squeeze_ratio, 3),
                'vol_decline': round(vol_ratio, 3),
                'rng_pct': round(rng_pct, 3),
                'vol_surge_x': round(today.Volume / vol_20, 2),
                'ret_5d': round(ret_5d, 2) if ret_5d is not None else None,
                'ret_10d': round(ret_10d, 2) if ret_10d is not None else None,
                'ret_15d': round(ret_15d, 2) if ret_15d is not None else None,
                'ret_20d': round(ret_20d, 2) if ret_20d is not None else None,
                'max_ret_20d': round(max_ret_20d, 2) if max_ret_20d is not None else None,
                'max_dd_20d': round(max_dd_20d, 2) if max_dd_20d is not None else None,
            })

results_df = pd.DataFrame(results)

if len(results_df) > 0:
    # Deduplicate: remove signals within 5 days on same ticker
    results_df = results_df.sort_values(['ticker', 'date'])
    filtered = []
    for tkr in results_df.ticker.unique():
        tkr_df = results_df[results_df.ticker == tkr]
        last_date = 0
        for _, row in tkr_df.iterrows():
            if row.date - last_date >= 5:
                filtered.append(row)
                last_date = row.date
    results_df = pd.DataFrame(filtered)

    print("\n=== BREAKOUT SIGNALS FOUND: {} ===\n".format(len(results_df)))
    print("=== ALL BREAKOUT SIGNALS ===")
    print(results_df.to_string(index=False))

    print("\n=== BY SECTOR ===")
    print(results_df.groupby('sector').size())

    for period, col in [('5d', 'ret_5d'), ('10d', 'ret_10d'), ('15d', 'ret_15d'), ('20d', 'ret_20d')]:
        valid = results_df[col].dropna()
        if len(valid) > 0:
            print("\n--- {} Forward Returns ---".format(period))
            print("  N = {}".format(len(valid)))
            print("  Mean: {:.2f}%".format(valid.mean()))
            print("  Median: {:.2f}%".format(valid.median()))
            print("  Win rate (>0%): {:.1f}%".format((valid > 0).mean()*100))
            print("  Win rate (>3%): {:.1f}%".format((valid > 3).mean()*100))
            if (valid > 0).any():
                print("  Avg winner: {:.2f}%".format(valid[valid > 0].mean()))
            else:
                print("  No winners")
            if (valid <= 0).any():
                print("  Avg loser: {:.2f}%".format(valid[valid <= 0].mean()))
            else:
                print("  No losers")

    valid_max = results_df['max_ret_20d'].dropna()
    valid_dd = results_df['max_dd_20d'].dropna()
    if len(valid_max) > 0:
        print("\n--- Best Possible Exit (20d window) ---")
        print("  Mean max gain: {:.2f}%".format(valid_max.mean()))
        print("  Median max gain: {:.2f}%".format(valid_max.median()))
        print("  Mean max drawdown: {:.2f}%".format(valid_dd.mean()))
        print("  Median max drawdown: {:.2f}%".format(valid_dd.median()))
        print("  Reward/Risk: {:.2f}".format(abs(valid_max.mean() / valid_dd.mean())))

    # Per-ticker breakdown
    print("\n=== PER-TICKER BREAKDOWN ===")
    for tkr in results_df.ticker.unique():
        tkr_df = results_df[results_df.ticker == tkr]
        print("\n{} ({}): {} breakouts".format(tkr, tkr_df.sector.iloc[0], len(tkr_df)))
        for _, row in tkr_df.iterrows():
            print("  Date {}: ${} | day +{}% | squeeze={} | vol_surge={}x | 5d={}% | 10d={}% | 20d={}% | max={}% | dd={}%".format(
                row.date, row.close, row.daily_ret, row.squeeze_ratio, row.vol_surge_x,
                row.ret_5d, row.ret_10d, row.ret_20d, row.max_ret_20d, row.max_dd_20d))
else:
    print("NO BREAKOUT SIGNALS FOUND with strict criteria")
    print("Trying relaxed criteria...")

# Also run RELAXED criteria for comparison
results_relaxed = []
for tkr in ohlcv.ticker.unique():
    df = ohlcv[ohlcv.ticker == tkr].sort_values('date').reset_index(drop=True)
    if len(df) < 55:
        continue

    for i in range(50, len(df)):
        window_20 = df.iloc[i-20:i]
        window_40 = df.iloc[i-40:i]
        window_50 = df.iloc[i-50:i]
        today = df.iloc[i]
        yesterday = df.iloc[i-1]

        range_20 = window_20.High.max() - window_20.Low.min()
        range_40 = window_40.High.max() - window_40.Low.min()
        if range_40 == 0:
            continue
        squeeze_ratio = range_20 / range_40

        vol_20 = window_20.Volume.mean()
        vol_50 = window_50.Volume.mean()
        if vol_50 == 0:
            continue
        vol_ratio = vol_20 / vol_50

        low_20 = window_20.Low.min()
        high_20 = window_20.High.max()
        if high_20 == low_20:
            continue
        rng_pct = (today.Close - low_20) / (high_20 - low_20)

        daily_return = (today.Close - yesterday.Close) / yesterday.Close
        near_high = today.Close >= high_20 * 0.995

        vol_surge = today.Volume >= vol_20 * 1.2

        is_breakout = (squeeze_ratio < 0.70 and
                       vol_ratio < 0.95 and
                       rng_pct >= 0.65 and
                       daily_return >= 0.015 and
                       near_high and
                       vol_surge)

        if is_breakout:
            ret_5d = ret_10d = ret_15d = ret_20d = max_ret_20d = max_dd_20d = None
            if i + 5 < len(df):
                ret_5d = (df.iloc[i+5].Close - today.Close) / today.Close * 100
            if i + 10 < len(df):
                ret_10d = (df.iloc[i+10].Close - today.Close) / today.Close * 100
            if i + 15 < len(df):
                ret_15d = (df.iloc[i+15].Close - today.Close) / today.Close * 100
            if i + 20 < len(df):
                ret_20d = (df.iloc[i+20].Close - today.Close) / today.Close * 100
            if i + 20 < len(df):
                future_highs = df.iloc[i+1:i+21].High.max()
                max_ret_20d = (future_highs - today.Close) / today.Close * 100
                future_lows = df.iloc[i+1:i+21].Low.min()
                max_dd_20d = (future_lows - today.Close) / today.Close * 100
            elif i + 1 < len(df):
                future_highs = df.iloc[i+1:].High.max()
                max_ret_20d = (future_highs - today.Close) / today.Close * 100
                future_lows = df.iloc[i+1:].Low.min()
                max_dd_20d = (future_lows - today.Close) / today.Close * 100

            results_relaxed.append({
                'ticker': tkr,
                'sector': relevant[relevant.ticker == tkr].sector.values[0],
                'date': int(today.date),
                'close': round(today.Close, 2),
                'daily_ret': round(daily_return * 100, 2),
                'squeeze_ratio': round(squeeze_ratio, 3),
                'vol_decline': round(vol_ratio, 3),
                'vol_surge_x': round(today.Volume / vol_20, 2),
                'ret_5d': round(ret_5d, 2) if ret_5d is not None else None,
                'ret_10d': round(ret_10d, 2) if ret_10d is not None else None,
                'ret_20d': round(ret_20d, 2) if ret_20d is not None else None,
                'max_ret_20d': round(max_ret_20d, 2) if max_ret_20d is not None else None,
                'max_dd_20d': round(max_dd_20d, 2) if max_dd_20d is not None else None,
            })

results_relaxed_df = pd.DataFrame(results_relaxed)
if len(results_relaxed_df) > 0:
    results_relaxed_df = results_relaxed_df.sort_values(['ticker', 'date'])
    filtered_r = []
    for tkr in results_relaxed_df.ticker.unique():
        tkr_df = results_relaxed_df[results_relaxed_df.ticker == tkr]
        last_date = 0
        for _, row in tkr_df.iterrows():
            if row.date - last_date >= 5:
                filtered_r.append(row)
                last_date = row.date
    results_relaxed_df = pd.DataFrame(filtered_r)

    print("\n\n=== RELAXED CRITERIA: {} signals ===".format(len(results_relaxed_df)))
    print(results_relaxed_df.to_string(index=False))

    print("\n=== BY SECTOR (relaxed) ===")
    print(results_relaxed_df.groupby('sector').size())

    for period, col in [('5d', 'ret_5d'), ('10d', 'ret_10d'), ('20d', 'ret_20d')]:
        valid = results_relaxed_df[col].dropna()
        if len(valid) > 0:
            print("\n--- {} Forward Returns (RELAXED) ---".format(period))
            print("  N = {}".format(len(valid)))
            print("  Mean: {:.2f}%".format(valid.mean()))
            print("  Median: {:.2f}%".format(valid.median()))
            print("  Win rate (>0%): {:.1f}%".format((valid > 0).mean()*100))
            print("  Win rate (>3%): {:.1f}%".format((valid > 3).mean()*100))

    valid_max = results_relaxed_df['max_ret_20d'].dropna()
    valid_dd = results_relaxed_df['max_dd_20d'].dropna()
    if len(valid_max) > 0:
        print("\n--- Best Possible Exit (20d, RELAXED) ---")
        print("  Mean max gain: {:.2f}%".format(valid_max.mean()))
        print("  Mean max DD: {:.2f}%".format(valid_dd.mean()))
        print("  Reward/Risk: {:.2f}".format(abs(valid_max.mean() / valid_dd.mean())))

conn.close()
