import yfinance as yf
import pandas as pd
import numpy as np
import sqlite3
import warnings
warnings.filterwarnings('ignore')

# Get tickers
conn = sqlite3.connect(r"C:\Users\aldoh\Documents\RApplication\data\mydb.db")
tickers_df = pd.read_sql("SELECT Symbol, Sector FROM ScannerUniverse WHERE IsActive = 1 AND Sector NOT IN ('Forex', 'Macro')", conn)
conn.close()

# Remove non-US tickers (European stocks with different Yahoo symbols)
euro_tickers = ['CA.PA','BNP','SAF','SIE','KNIN','SGO','ABBN','AMRZ','AI','OR','NVO','BN',
                'NOVN','TTE','GTT','DSY','ERA','MT','FXC','RO','SLHN','CRST']
tickers_df = tickers_df[~tickers_df.Symbol.isin(euro_tickers)]

# Skip ETFs for pure stock analysis
etf_list = ['XLE','MOO','ITA','XLB','XLI','XLK','XLF','XLV','XLP','XLC','XLY','XLRE',
            'XLU','XOP','GLD','GDX','SLV','SMH','QQQ','VXX','EWJ','EWY','IWM','IBB',
            'NLR','NUCL','KRE','ITB','URA','DBA']
stocks_df = tickers_df[~tickers_df.Symbol.isin(etf_list)]

symbols = stocks_df.Symbol.tolist()
sector_map = dict(zip(stocks_df.Symbol, stocks_df.Sector))

print(f"Downloading 5y daily data for {len(symbols)} stocks...")

# Download in batches
all_data = {}
batch_size = 50
for i in range(0, len(symbols), batch_size):
    batch = symbols[i:i+batch_size]
    print(f"  Batch {i//batch_size + 1}: {batch[:5]}...")
    try:
        data = yf.download(batch, period="5y", interval="1d", group_by='ticker', progress=False, threads=True)
        for sym in batch:
            try:
                if len(batch) == 1:
                    df = data.copy()
                else:
                    df = data[sym].copy()
                df = df.dropna(subset=['Close'])
                if len(df) > 100:
                    df = df.reset_index()
                    if isinstance(df.columns, pd.MultiIndex):
                        df.columns = [c[0] if isinstance(c, tuple) else c for c in df.columns]
                    all_data[sym] = df
            except Exception:
                pass
    except Exception as e:
        print(f"  Error: {e}")

print(f"Got data for {len(all_data)} stocks")

# Breakout detection
def find_breakouts(all_data, sector_map, squeeze_thresh=0.65, vol_decline_thresh=0.90):
    results = []
    for sym, df in all_data.items():
        df = df.sort_values('Date').reset_index(drop=True)
        if len(df) < 55:
            continue

        highs = df['High'].values.astype(float)
        lows = df['Low'].values.astype(float)
        closes = df['Close'].values.astype(float)
        volumes = df['Volume'].values.astype(float)
        dates = df['Date'].values

        for i in range(50, len(df)):
            h20 = highs[i-20:i]
            l20 = lows[i-20:i]
            h40 = highs[i-40:i]
            l40 = lows[i-40:i]
            v20 = volumes[i-20:i]
            v50 = volumes[i-50:i]

            range_20 = h20.max() - l20.min()
            range_40 = h40.max() - l40.min()
            if range_40 == 0:
                continue
            squeeze = range_20 / range_40

            vol_20_avg = v20.mean()
            vol_50_avg = v50.mean()
            if vol_50_avg == 0:
                continue
            vol_ratio = vol_20_avg / vol_50_avg

            hi20 = h20.max()
            lo20 = l20.min()
            if hi20 == lo20:
                continue
            rng_pct = (closes[i] - lo20) / (hi20 - lo20)

            daily_ret = (closes[i] - closes[i-1]) / closes[i-1] if closes[i-1] > 0 else 0
            near_high = closes[i] >= hi20 * 0.995
            vol_surge = volumes[i] >= vol_20_avg * 1.2

            if (squeeze < squeeze_thresh and vol_ratio < vol_decline_thresh and
                rng_pct >= 0.65 and daily_ret >= 0.015 and near_high and vol_surge):

                r5 = r10 = r15 = r20 = mx = dd = None
                if i+5 < len(df): r5 = (closes[i+5] - closes[i]) / closes[i] * 100
                if i+10 < len(df): r10 = (closes[i+10] - closes[i]) / closes[i] * 100
                if i+15 < len(df): r15 = (closes[i+15] - closes[i]) / closes[i] * 100
                if i+20 < len(df):
                    r20 = (closes[i+20] - closes[i]) / closes[i] * 100
                    mx = (highs[i+1:i+21].max() - closes[i]) / closes[i] * 100
                    dd = (lows[i+1:i+21].min() - closes[i]) / closes[i] * 100

                results.append({
                    'ticker': sym, 'sector': sector_map.get(sym, '?'),
                    'date': str(dates[i])[:10], 'close': round(float(closes[i]), 2),
                    'daily_ret': round(daily_ret*100, 2),
                    'squeeze': round(squeeze, 3), 'vol_dec': round(vol_ratio, 3),
                    'vol_surge_x': round(float(volumes[i]/vol_20_avg), 2),
                    'ret_5d': round(r5,2) if r5 is not None else None,
                    'ret_10d': round(r10,2) if r10 is not None else None,
                    'ret_15d': round(r15,2) if r15 is not None else None,
                    'ret_20d': round(r20,2) if r20 is not None else None,
                    'max_ret': round(mx,2) if mx is not None else None,
                    'max_dd': round(dd,2) if dd is not None else None,
                })

    df_res = pd.DataFrame(results)
    if len(df_res) == 0:
        return df_res
    # Deduplicate within 10 days same ticker
    df_res = df_res.sort_values(['ticker','date'])
    filt = []
    for t in df_res.ticker.unique():
        td = df_res[df_res.ticker == t]
        last_date = pd.Timestamp('1900-01-01')
        for _, r in td.iterrows():
            if (pd.Timestamp(r.date) - last_date).days >= 10:
                filt.append(r)
                last_date = pd.Timestamp(r.date)
    return pd.DataFrame(filt)

print("\n" + "="*60)
print("STRICT CRITERIA - 5 YEAR BACKTEST")
print("="*60)

strict = find_breakouts(all_data, sector_map, 0.65, 0.90)

if len(strict) > 0:
    print(f"\nTotal breakout signals: {len(strict)}")
    print(f"Unique tickers: {strict.ticker.nunique()}")
    print(f"Date range: {strict.date.min()} to {strict.date.max()}")

    print(f"\n=== BY SECTOR ===")
    print(strict.groupby('sector').size().sort_values(ascending=False).to_string())

    print(f"\n=== BY YEAR ===")
    strict['year'] = strict.date.str[:4]
    for yr in sorted(strict.year.unique()):
        yr_df = strict[strict.year == yr]
        v20 = yr_df.ret_20d.dropna()
        if len(v20) > 0:
            print(f"  {yr}: N={len(yr_df)}, 20d mean={v20.mean():.2f}%, median={v20.median():.2f}%, WR={((v20>0).mean()*100):.1f}%")

    print(f"\n=== FORWARD RETURNS SUMMARY ===")
    for p, c in [('5d','ret_5d'),('10d','ret_10d'),('15d','ret_15d'),('20d','ret_20d')]:
        v = strict[c].dropna()
        if len(v) > 0:
            print(f"\n--- {p} ---")
            print(f"  N={len(v)}, Mean={v.mean():.2f}%, Median={v.median():.2f}%")
            print(f"  WR(>0%)={((v>0).mean()*100):.1f}%, WR(>3%)={((v>3).mean()*100):.1f}%")
            if (v>0).any(): print(f"  Avg winner: {v[v>0].mean():.2f}%")
            if (v<=0).any(): print(f"  Avg loser: {v[v<=0].mean():.2f}%")
            print(f"  Worst: {v.min():.2f}%, Best: {v.max():.2f}%")

    vm = strict.max_ret.dropna(); vd = strict.max_dd.dropna()
    if len(vm) > 0:
        print(f"\n--- Best Exit / Worst DD (20d window) ---")
        print(f"  Mean max gain: {vm.mean():.2f}%, Median: {vm.median():.2f}%")
        print(f"  Mean max DD: {vd.mean():.2f}%, Median: {vd.median():.2f}%")
        print(f"  Reward/Risk: {abs(vm.mean()/vd.mean()):.2f}")

    # By sector detailed
    print(f"\n=== BY SECTOR DETAILED (20d returns) ===")
    for sect in strict.groupby('sector').size().sort_values(ascending=False).index:
        s = strict[strict.sector == sect]
        v20 = s.ret_20d.dropna()
        vmx = s.max_ret.dropna()
        vdd = s.max_dd.dropna()
        if len(v20) > 0:
            rr = abs(vmx.mean()/vdd.mean()) if vdd.mean() != 0 else 0
            print(f"\n  {sect} (N={len(s)}, {s.ticker.nunique()} tickers)")
            print(f"    20d: mean={v20.mean():.2f}%, median={v20.median():.2f}%, WR={((v20>0).mean()*100):.1f}%")
            print(f"    Max gain={vmx.mean():.2f}%, Max DD={vdd.mean():.2f}%, R/R={rr:.2f}")
            print(f"    Tickers: {', '.join(sorted(s.ticker.unique()))}")

    # Top 20 and bottom 10
    print(f"\n=== TOP 20 BREAKOUTS (by 20d return) ===")
    top = strict.dropna(subset=['ret_20d']).nlargest(20, 'ret_20d')
    for _, r in top.iterrows():
        print(f"  {r.ticker:6s} {r.date} ${r.close:>8.2f} | day +{r.daily_ret}% | 10d={r.ret_10d}% | 20d={r.ret_20d}% | max={r.max_ret}% | dd={r.max_dd}%")

    print(f"\n=== BOTTOM 10 BREAKOUTS (by 20d return) ===")
    bot = strict.dropna(subset=['ret_20d']).nsmallest(10, 'ret_20d')
    for _, r in bot.iterrows():
        print(f"  {r.ticker:6s} {r.date} ${r.close:>8.2f} | day +{r.daily_ret}% | 10d={r.ret_10d}% | 20d={r.ret_20d}% | max={r.max_ret}% | dd={r.max_dd}%")

    # Expectancy
    print(f"\n=== EXPECTANCY (assuming $1000 per trade, 20d hold, stock) ===")
    v20 = strict.ret_20d.dropna()
    avg_pnl = v20.mean() / 100 * 1000
    trades_per_yr = len(strict) / 5
    print(f"  Avg P&L per trade: ${avg_pnl:.0f}")
    print(f"  Trades per year (avg): {trades_per_yr:.0f}")
    print(f"  Expected annual P&L: ${avg_pnl * trades_per_yr:.0f}")

    # Save results
    strict.to_csv(r"C:\Users\aldoh\Documents\NewTrading\breakout_5y_results.csv", index=False)
    print(f"\nResults saved to breakout_5y_results.csv")
else:
    print("NO SIGNALS FOUND")
