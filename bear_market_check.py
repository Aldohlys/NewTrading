import yfinance as yf
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Get SPX data
spy = yf.download('SPY', period='5y', interval='1d', progress=False)
spy = spy.reset_index()
if isinstance(spy.columns, pd.MultiIndex):
    spy.columns = [c[0] if isinstance(c, tuple) else c for c in spy.columns]

spy['MA50'] = spy['Close'].rolling(50).mean()
spy['MA200'] = spy['Close'].rolling(200).mean()
spy['ATH'] = spy['Close'].expanding().max()
spy['Drawdown'] = (spy['Close'] - spy['ATH']) / spy['ATH'] * 100

# Get VIX
vix = yf.download('^VIX', period='5y', interval='1d', progress=False)
vix = vix.reset_index()
if isinstance(vix.columns, pd.MultiIndex):
    vix.columns = [c[0] if isinstance(c, tuple) else c for c in vix.columns]
vix = vix.rename(columns={'Close': 'VIX'})

spy = spy.merge(vix[['Date','VIX']], on='Date', how='left')

print("=" * 70)
print("1. SPX BELOW MA50 - BEAR MARKET OR CONSOLIDATION?")
print("=" * 70)

spy['below_ma50'] = spy['Close'] < spy['MA50']
spy['group'] = (spy['below_ma50'] != spy['below_ma50'].shift()).cumsum()
below_periods = spy[spy['below_ma50']].groupby('group').agg(
    start=('Date', 'first'),
    end=('Date', 'last'),
    days=('Date', 'count'),
    min_close=('Close', 'min'),
    max_close=('Close', 'max'),
    entry_close=('Close', 'first'),
    exit_close=('Close', 'last'),
    min_drawdown=('Drawdown', 'min'),
    avg_vix=('VIX', 'mean'),
    max_vix=('VIX', 'max'),
).reset_index(drop=True)

below_periods = below_periods[below_periods.days > 5]
below_periods['price_range_pct'] = ((below_periods.max_close - below_periods.min_close) / below_periods.min_close * 100).round(1)

print("\nPeriods where SPX was below MA50 for >5 days:\n")
for _, p in below_periods.iterrows():
    end_idx = spy[spy.Date >= p.end].index
    if len(end_idx) > 0 and end_idx[0] + 20 < len(spy):
        ret_20d = (spy.iloc[end_idx[0]+20].Close - spy.iloc[end_idx[0]].Close) / spy.iloc[end_idx[0]].Close * 100
        outcome = f"20d after: {ret_20d:+.1f}%"
    else:
        outcome = "N/A"
    bear = "BEAR" if p.min_drawdown < -10 else "CONSOLIDATION"
    print(f"  {str(p.start)[:10]} to {str(p.end)[:10]} | {int(p.days):3d} days | DD={p.min_drawdown:.1f}% | VIX avg={p.avg_vix:.1f} max={p.max_vix:.1f} | {bear} | {outcome}")

print(f"\n{'=' * 70}")
print("2. VIX > 25 - DOES IT ALWAYS MEAN BEAR?")
print("=" * 70)

high_vix = spy[spy.VIX > 25].copy()
high_vix['ret_next_20d'] = None
for idx in high_vix.index:
    if idx + 20 < len(spy):
        high_vix.loc[idx, 'ret_next_20d'] = (spy.iloc[idx+20].Close - spy.iloc[idx].Close) / spy.iloc[idx].Close * 100

valid = high_vix.dropna(subset=['ret_next_20d'])
print(f"\nDays with VIX > 25: {len(high_vix)}")
print(f"  SPY return next 20d:")
print(f"    Mean: {valid.ret_next_20d.mean():.2f}%")
print(f"    Median: {valid.ret_next_20d.median():.2f}%")
print(f"    Win rate (>0%): {(valid.ret_next_20d > 0).mean()*100:.1f}%")
print(f"    Win rate (>3%): {(valid.ret_next_20d > 3).mean()*100:.1f}%")

up_days = valid[valid.ret_next_20d > 3]
print(f"\n  VIX > 25 but SPY +3% in next 20d: {len(up_days)} days ({len(up_days)/len(valid)*100:.1f}%)")
print(f"  Examples:")
for _, r in up_days.head(8).iterrows():
    print(f"    {str(r.Date)[:10]} VIX={r.VIX:.1f}, SPY=${r.Close:.0f}, DD={r.Drawdown:.1f}%, next 20d: +{r.ret_next_20d:.1f}%")

print(f"\n{'=' * 70}")
print("3. REGIME DEFINITION - DRAWDOWN FROM ATH")
print("=" * 70)

spy['is_bear'] = spy['Drawdown'] < -10
spy['is_correction'] = (spy['Drawdown'] < -5) & (spy['Drawdown'] >= -10)
spy['is_bull'] = spy['Drawdown'] >= -5

print(f"\nRegime distribution (5 years):")
print(f"  Bull (DD > -5%):        {spy.is_bull.sum()} days ({spy.is_bull.mean()*100:.1f}%)")
print(f"  Correction (-10 to -5%): {spy.is_correction.sum()} days ({spy.is_correction.mean()*100:.1f}%)")
print(f"  Bear (DD < -10%):        {spy.is_bear.sum()} days ({spy.is_bear.mean()*100:.1f}%)")

# Load breakout results
results = pd.read_csv(r"C:\Users\aldoh\Documents\NewTrading\breakout_5y_results.csv")
results['Date'] = pd.to_datetime(results['date'])

spy_regime = spy[['Date','Drawdown','VIX','below_ma50','is_bear','is_correction','is_bull']].copy()
results = results.merge(spy_regime, on='Date', how='left')

print(f"\n{'=' * 70}")
print("4. BREAKOUT RESULTS BY MARKET REGIME")
print("=" * 70)

for regime, label in [('is_bull', 'BULL (DD > -5%)'), ('is_correction', 'CORRECTION (-10 to -5%)'), ('is_bear', 'BEAR (DD < -10%)')]:
    r = results[results[regime] == True]
    v20 = r.ret_20d.dropna()
    if len(v20) > 0:
        vm = r.max_ret.dropna()
        vd = r.max_dd.dropna()
        rr = abs(vm.mean()/vd.mean()) if vd.mean() != 0 else 0
        print(f"\n  {label}: N={len(r)}")
        print(f"    20d: mean={v20.mean():.2f}%, median={v20.median():.2f}%, WR={((v20>0).mean()*100):.1f}%")
        print(f"    Max gain={vm.mean():.2f}%, Max DD={vd.mean():.2f}%, R/R={rr:.2f}")
        for sect in r.groupby('sector').size().sort_values(ascending=False).head(8).index:
            s = r[r.sector == sect]
            sv = s.ret_20d.dropna()
            if len(sv) >= 3:
                print(f"      {sect:25s}: N={len(s)}, 20d mean={sv.mean():+.2f}%, WR={((sv>0).mean()*100):.0f}%")

print(f"\n{'=' * 70}")
print("5. SPX BELOW MA50 AS FILTER")
print("=" * 70)

above = results[results['below_ma50'] == False]
below = results[results['below_ma50'] == True]
va = above.ret_20d.dropna()
vb = below.ret_20d.dropna()
vma = above.max_ret.dropna(); vda = above.max_dd.dropna()
vmb = below.max_ret.dropna(); vdb = below.max_dd.dropna()

print(f"\n  SPX ABOVE MA50: N={len(above)}, 20d mean={va.mean():.2f}%, WR={((va>0).mean()*100):.1f}%")
print(f"    Max gain={vma.mean():.2f}%, Max DD={vda.mean():.2f}%, R/R={abs(vma.mean()/vda.mean()):.2f}")
print(f"\n  SPX BELOW MA50: N={len(below)}, 20d mean={vb.mean():.2f}%, WR={((vb>0).mean()*100):.1f}%")
print(f"    Max gain={vmb.mean():.2f}%, Max DD={vdb.mean():.2f}%, R/R={abs(vmb.mean()/vdb.mean()):.2f}")

print(f"\n{'=' * 70}")
print("6. BULL REGIME - SECTOR BREAKDOWN")
print("=" * 70)

good = results[results.is_bull == True]
vg = good.ret_20d.dropna()
vmg = good.max_ret.dropna(); vdg = good.max_dd.dropna()
print(f"\n  BULL ONLY (DD > -5%): N={len(good)}, 20d mean={vg.mean():.2f}%, WR={((vg>0).mean()*100):.1f}%")
print(f"    Max gain={vmg.mean():.2f}%, Max DD={vdg.mean():.2f}%, R/R={abs(vmg.mean()/vdg.mean()):.2f}")

print(f"\n  BY SECTOR (bull regime only):")
for sect in good.groupby('sector').size().sort_values(ascending=False).index:
    s = good[good.sector == sect]
    sv = s.ret_20d.dropna()
    smx = s.max_ret.dropna(); sdd = s.max_dd.dropna()
    if len(sv) >= 3:
        rr = abs(smx.mean()/sdd.mean()) if sdd.mean() != 0 else 0
        print(f"    {sect:25s}: N={len(s):3d}, 20d mean={sv.mean():+6.2f}%, WR={((sv>0).mean()*100):5.1f}%, R/R={rr:.2f}")

print(f"\n{'=' * 70}")
print("7. CORRECTION REGIME - WHICH SECTORS STILL WORK?")
print("=" * 70)

corr = results[results.is_correction == True]
vc = corr.ret_20d.dropna()
print(f"\n  CORRECTION (DD -5 to -10%): N={len(corr)}, 20d mean={vc.mean():.2f}%, WR={((vc>0).mean()*100):.1f}%")
print(f"\n  BY SECTOR (correction regime):")
for sect in corr.groupby('sector').size().sort_values(ascending=False).index:
    s = corr[corr.sector == sect]
    sv = s.ret_20d.dropna()
    if len(sv) >= 2:
        print(f"    {sect:25s}: N={len(s):3d}, 20d mean={sv.mean():+6.2f}%, WR={((sv>0).mean()*100):5.1f}%")
