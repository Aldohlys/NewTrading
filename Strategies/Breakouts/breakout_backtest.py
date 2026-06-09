import sqlite3
import pandas as pd
import numpy as np

conn = sqlite3.connect(r"C:\Users\aldoh\Documents\RApplication\data\mydb.db")

# Get all sectors
sectors = pd.read_sql("SELECT DISTINCT Sector as sector FROM ScannerUniverse WHERE IsActive = 1 ORDER BY Sector", conn)
print("All sectors:")
for s in sectors.sector.tolist():
    print(f"  {s}")

# Get tickers for Tech and Healthcare-like sectors
tickers_df = pd.read_sql("SELECT Symbol as ticker, Sector as sector FROM ScannerUniverse WHERE IsActive = 1", conn)
relevant = tickers_df[tickers_df.sector.str.contains('Tech|Health|Pharma|Bio|Med|Comm|Software|Semi|Comput', case=False, na=False)]
if len(relevant) == 0:
    # Try broader match
    print("No match, showing all sectors with counts:")
    print(tickers_df.sector.value_counts())
    relevant = tickers_df  # fallback: show all to find right names

print(f"\nRelevant tickers ({len(relevant)}):")
print(relevant.groupby('sector').apply(lambda x: x.ticker.tolist()))

# Get OHLCV
tickers_list = relevant.ticker.tolist()
placeholders = ','.join(['?'] * len(tickers_list))
ohlcv = pd.read_sql(f"SELECT date, ticker, Open, High, Low, Close, Volume FROM mrbreakouts_cache WHERE ticker IN ({placeholders}) ORDER BY ticker, date", conn, params=tickers_list)
print(f"\nOHLCV rows: {len(ohlcv)}, tickers with data: {ohlcv.ticker.nunique()}")

# Breakout detection
def find_breakouts(ohlcv_data, ticker_sector_map, squeeze_thresh=0.65, vol_decline_thresh=0.90):
    results = []
    for tkr in ohlcv_data.ticker.unique():
        df = ohlcv_data[ohlcv_data.ticker == tkr].sort_values('date').reset_index(drop=True)
        if len(df) < 55:
            continue
        for i in range(50, len(df)):
            w20 = df.iloc[i-20:i]
            w40 = df.iloc[i-40:i]
            w50 = df.iloc[i-50:i]
            today = df.iloc[i]
            yest = df.iloc[i-1]

            r20 = w20.High.max() - w20.Low.min()
            r40 = w40.High.max() - w40.Low.min()
            if r40 == 0: continue
            squeeze = r20 / r40

            v20 = w20.Volume.mean()
            v50 = w50.Volume.mean()
            if v50 == 0: continue
            vr = v20 / v50

            lo20 = w20.Low.min()
            hi20 = w20.High.max()
            if hi20 == lo20: continue
            rng = (today.Close - lo20) / (hi20 - lo20)

            dret = (today.Close - yest.Close) / yest.Close
            near_hi = today.Close >= hi20 * 0.995
            vsurge = today.Volume >= v20 * 1.2

            if (squeeze < squeeze_thresh and vr < vol_decline_thresh and rng >= 0.65
                and dret >= 0.015 and near_hi and vsurge):

                r5 = r10 = r15 = r20d = mx = dd = None
                if i+5 < len(df): r5 = (df.iloc[i+5].Close - today.Close)/today.Close*100
                if i+10 < len(df): r10 = (df.iloc[i+10].Close - today.Close)/today.Close*100
                if i+15 < len(df): r15 = (df.iloc[i+15].Close - today.Close)/today.Close*100
                if i+20 < len(df):
                    r20d = (df.iloc[i+20].Close - today.Close)/today.Close*100
                    mx = (df.iloc[i+1:i+21].High.max() - today.Close)/today.Close*100
                    dd = (df.iloc[i+1:i+21].Low.min() - today.Close)/today.Close*100
                elif i+1 < len(df):
                    mx = (df.iloc[i+1:].High.max() - today.Close)/today.Close*100
                    dd = (df.iloc[i+1:].Low.min() - today.Close)/today.Close*100

                sect = ticker_sector_map.get(tkr, 'Unknown')
                results.append({
                    'ticker': tkr, 'sector': sect, 'date': int(today.date),
                    'close': round(today.Close,2), 'daily_ret': round(dret*100,2),
                    'squeeze': round(squeeze,3), 'vol_dec': round(vr,3),
                    'vol_surge_x': round(today.Volume/v20,2),
                    'ret_5d': round(r5,2) if r5 is not None else None,
                    'ret_10d': round(r10,2) if r10 is not None else None,
                    'ret_15d': round(r15,2) if r15 is not None else None,
                    'ret_20d': round(r20d,2) if r20d is not None else None,
                    'max_ret': round(mx,2) if mx is not None else None,
                    'max_dd': round(dd,2) if dd is not None else None,
                })

    df_res = pd.DataFrame(results)
    if len(df_res) == 0:
        return df_res
    # Deduplicate within 5 days
    df_res = df_res.sort_values(['ticker','date'])
    filt = []
    for t in df_res.ticker.unique():
        td = df_res[df_res.ticker==t]
        ld = 0
        for _,r in td.iterrows():
            if r.date - ld >= 5:
                filt.append(r)
                ld = r.date
    return pd.DataFrame(filt)

tsmap = dict(zip(relevant.ticker, relevant.sector))

# STRICT
print("\n" + "="*60)
print("STRICT CRITERIA (squeeze<0.65, vol_decline<0.90)")
print("="*60)
strict = find_breakouts(ohlcv, tsmap, 0.65, 0.90)
if len(strict) > 0:
    print(f"\nSignals found: {len(strict)}")
    print(strict.to_string(index=False))
    print(f"\nBy sector:\n{strict.groupby('sector').size()}")
    for p,c in [('5d','ret_5d'),('10d','ret_10d'),('15d','ret_15d'),('20d','ret_20d')]:
        v = strict[c].dropna()
        if len(v)>0:
            print(f"\n--- {p} ---")
            print(f"  N={len(v)}, Mean={v.mean():.2f}%, Median={v.median():.2f}%")
            print(f"  WR(>0%)={((v>0).mean()*100):.1f}%, WR(>3%)={((v>3).mean()*100):.1f}%")
            if (v>0).any(): print(f"  Avg winner: {v[v>0].mean():.2f}%")
            if (v<=0).any(): print(f"  Avg loser: {v[v<=0].mean():.2f}%")
    vm = strict.max_ret.dropna(); vd = strict.max_dd.dropna()
    if len(vm)>0:
        print(f"\n--- Max Gain/DD (20d) ---")
        print(f"  Mean max gain: {vm.mean():.2f}%, Mean max DD: {vd.mean():.2f}%")
        print(f"  Reward/Risk: {abs(vm.mean()/vd.mean()):.2f}")
    print(f"\n--- Per ticker ---")
    for t in strict.ticker.unique():
        td = strict[strict.ticker==t]
        print(f"\n{t} ({td.sector.iloc[0]}): {len(td)} breakouts")
        for _,r in td.iterrows():
            print(f"  {r.date}: ${r.close} | +{r.daily_ret}% | sq={r.squeeze} | vol={r.vol_surge_x}x | 5d={r.ret_5d}% | 10d={r.ret_10d}% | 20d={r.ret_20d}% | max={r.max_ret}% | dd={r.max_dd}%")
else:
    print("NO signals found with strict criteria")

# RELAXED
print("\n" + "="*60)
print("RELAXED CRITERIA (squeeze<0.70, vol_decline<0.95)")
print("="*60)
relaxed = find_breakouts(ohlcv, tsmap, 0.70, 0.95)
if len(relaxed) > 0:
    print(f"\nSignals found: {len(relaxed)}")
    print(relaxed.to_string(index=False))
    print(f"\nBy sector:\n{relaxed.groupby('sector').size()}")
    for p,c in [('5d','ret_5d'),('10d','ret_10d'),('15d','ret_15d'),('20d','ret_20d')]:
        v = relaxed[c].dropna()
        if len(v)>0:
            print(f"\n--- {p} (RELAXED) ---")
            print(f"  N={len(v)}, Mean={v.mean():.2f}%, Median={v.median():.2f}%")
            print(f"  WR(>0%)={((v>0).mean()*100):.1f}%, WR(>3%)={((v>3).mean()*100):.1f}%")
            if (v>0).any(): print(f"  Avg winner: {v[v>0].mean():.2f}%")
            if (v<=0).any(): print(f"  Avg loser: {v[v<=0].mean():.2f}%")
    vm = relaxed.max_ret.dropna(); vd = relaxed.max_dd.dropna()
    if len(vm)>0:
        print(f"\n--- Max Gain/DD (20d, RELAXED) ---")
        print(f"  Mean max gain: {vm.mean():.2f}%, Mean max DD: {vd.mean():.2f}%")
        print(f"  Reward/Risk: {abs(vm.mean()/vd.mean()):.2f}")
    print(f"\n--- Per ticker (RELAXED) ---")
    for t in relaxed.ticker.unique():
        td = relaxed[relaxed.ticker==t]
        print(f"\n{t} ({td.sector.iloc[0]}): {len(td)} breakouts")
        for _,r in td.iterrows():
            print(f"  {r.date}: ${r.close} | +{r.daily_ret}% | sq={r.squeeze} | vol={r.vol_surge_x}x | 5d={r.ret_5d}% | 10d={r.ret_10d}% | 20d={r.ret_20d}% | max={r.max_ret}% | dd={r.max_dd}%")
else:
    print("NO signals found with relaxed criteria")

conn.close()
