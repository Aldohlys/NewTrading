"""
5-year breakout backtest comparing strict S6 (vol_decline < 0.90) vs relaxed (< 0.95)
Uses existing Yahoo data cache from breakout_backtest_5y.py
"""
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

euro_tickers = ['CA.PA','BNP','SAF','SIE','KNIN','SGO','ABBN','AMRZ','AI','OR','NVO','BN',
                'NOVN','TTE','GTT','DSY','ERA','MT','FXC','RO','SLHN','CRST']
tickers_df = tickers_df[~tickers_df.Symbol.isin(euro_tickers)]
etf_list = ['XLE','MOO','ITA','XLB','XLI','XLK','XLF','XLV','XLP','XLC','XLY','XLRE',
            'XLU','XOP','GLD','GDX','SLV','SMH','QQQ','VXX','EWJ','EWY','IWM','IBB',
            'NLR','NUCL','KRE','ITB','URA','DBA']
stocks_df = tickers_df[~tickers_df.Symbol.isin(etf_list)]
symbols = stocks_df.Symbol.tolist()
sector_map = dict(zip(stocks_df.Symbol, stocks_df.Sector))

print(f"Downloading 5y daily data for {len(symbols)} stocks...")
all_data = {}
batch_size = 50
for i in range(0, len(symbols), batch_size):
    batch = symbols[i:i+batch_size]
    print(f"  Batch {i//batch_size + 1}...")
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

def find_breakouts(all_data, sector_map, vol_decline_thresh):
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
            h20 = highs[i-20:i]; l20 = lows[i-20:i]
            h40 = highs[i-40:i]; l40 = lows[i-40:i]
            v20 = volumes[i-20:i]; v50 = volumes[i-50:i]

            range_20 = h20.max() - l20.min()
            range_40 = h40.max() - l40.min()
            if range_40 == 0: continue
            squeeze = range_20 / range_40

            vol_20_avg = v20.mean()
            vol_50_avg = v50.mean()
            if vol_50_avg == 0: continue
            vol_ratio = vol_20_avg / vol_50_avg

            hi20 = h20.max(); lo20 = l20.min()
            if hi20 == lo20: continue
            rng_pct = (closes[i] - lo20) / (hi20 - lo20)

            daily_ret = (closes[i] - closes[i-1]) / closes[i-1] if closes[i-1] > 0 else 0
            near_high = closes[i] >= hi20 * 0.995
            vol_surge = volumes[i] >= vol_20_avg * 1.2

            if (squeeze < 0.65 and vol_ratio < vol_decline_thresh and
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
                    'squeeze': round(squeeze, 3),
                    'vol_dec': round(vol_ratio, 3),
                    'vol_surge_x': round(float(volumes[i]/vol_20_avg), 2),
                    'ret_5d': round(r5,2) if r5 is not None else None,
                    'ret_10d': round(r10,2) if r10 is not None else None,
                    'ret_15d': round(r15,2) if r15 is not None else None,
                    'ret_20d': round(r20,2) if r20 is not None else None,
                    'max_ret': round(mx,2) if mx is not None else None,
                    'max_dd': round(dd,2) if dd is not None else None,
                })

    df_res = pd.DataFrame(results)
    if len(df_res) == 0: return df_res
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

# Run both
print("\n" + "="*70)
print("COMPARISON: S6 < 0.90 (strict) vs S6 < 0.95 (relaxed)")
print("="*70)

for label, thresh in [("STRICT (S6 < 0.90)", 0.90), ("RELAXED (S6 < 0.95)", 0.95)]:
    res = find_breakouts(all_data, sector_map, thresh)
    v20 = res.ret_20d.dropna()
    vm = res.max_ret.dropna()
    vd = res.max_dd.dropna()
    rr = abs(vm.mean()/vd.mean()) if vd.mean() != 0 else 0

    print(f"\n{'='*50}")
    print(f"{label}")
    print(f"{'='*50}")
    print(f"  Signals: {len(res)} | Unique tickers: {res.ticker.nunique()}")

    # By period
    for p, c in [('5d','ret_5d'),('10d','ret_10d'),('20d','ret_20d')]:
        v = res[c].dropna()
        if len(v) > 0:
            print(f"  {p}: mean={v.mean():.2f}%, median={v.median():.2f}%, WR={((v>0).mean()*100):.1f}%, WR>3%={((v>3).mean()*100):.1f}%")

    print(f"  Max gain (20d): {vm.mean():.2f}% | Max DD: {vd.mean():.2f}% | R/R: {rr:.2f}")

    # By year
    res['year'] = res.date.str[:4]
    print(f"\n  By year:")
    for yr in sorted(res.year.unique()):
        yr_df = res[res.year == yr]
        yv = yr_df.ret_20d.dropna()
        if len(yv) > 0:
            print(f"    {yr}: N={len(yr_df)}, 20d mean={yv.mean():.2f}%, WR={((yv>0).mean()*100):.1f}%")

    # By sector
    print(f"\n  By sector (20d):")
    for sect in res.groupby('sector').size().sort_values(ascending=False).index:
        s = res[res.sector == sect]
        sv = s.ret_20d.dropna()
        smx = s.max_ret.dropna(); sdd = s.max_dd.dropna()
        if len(sv) >= 3:
            srr = abs(smx.mean()/sdd.mean()) if sdd.mean() != 0 else 0
            print(f"    {sect:25s}: N={len(s):3d}, mean={sv.mean():+6.2f}%, WR={((sv>0).mean()*100):5.1f}%, R/R={srr:.2f}")

    if label == "RELAXED (S6 < 0.95)":
        res.to_csv(r"C:\Users\aldoh\Documents\NewTrading\breakout_5y_results_relaxed_s6.csv", index=False)

# Show what RELAXED adds vs STRICT
print(f"\n{'='*70}")
print("ADDITIONAL SIGNALS from relaxed S6")
print(f"{'='*70}")

strict = find_breakouts(all_data, sector_map, 0.90)
relaxed = find_breakouts(all_data, sector_map, 0.95)

# Find signals in relaxed but not in strict
strict_keys = set(strict.ticker + '_' + strict.date)
new_signals = relaxed[~(relaxed.ticker + '_' + relaxed.date).isin(strict_keys)]
nv = new_signals.ret_20d.dropna()

print(f"\nNew signals added: {len(new_signals)}")
if len(nv) > 0:
    print(f"  20d mean: {nv.mean():.2f}%, WR: {((nv>0).mean()*100):.1f}%")
    print(f"  Avg winner: {nv[nv>0].mean():.2f}%" if (nv>0).any() else "")
    print(f"  Avg loser: {nv[nv<=0].mean():.2f}%" if (nv<=0).any() else "")

    print(f"\n  Top 10 new signals:")
    for _, r in new_signals.dropna(subset=['ret_20d']).nlargest(10, 'ret_20d').iterrows():
        print(f"    {r.ticker:6s} {r.date} ${r.close:>8.2f} vd={r.vol_dec:.3f} | 20d={r.ret_20d:+.2f}% | max={r.max_ret:+.2f}%")

    print(f"\n  Bottom 5 new signals:")
    for _, r in new_signals.dropna(subset=['ret_20d']).nsmallest(5, 'ret_20d').iterrows():
        print(f"    {r.ticker:6s} {r.date} ${r.close:>8.2f} vd={r.vol_dec:.3f} | 20d={r.ret_20d:+.2f}% | max={r.max_ret:+.2f}%")
