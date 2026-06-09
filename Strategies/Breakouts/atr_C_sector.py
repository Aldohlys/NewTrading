"""Sector calibration of the C coefficient in  move(N) = C * ATR% * sqrt(N).

Question: is C (the normalized move/ATR shape) sector-specific, or universal?
Because C divides out ATR%, the large cross-sector VOL-LEVEL gap (tech ~2x staples'
daily range) lives in the ATR% input, NOT in C. This tests whether the residual
SHAPE differs by sector. N = 10 sessions.

Result (5y daily): C_med spread only 0.46-0.52 (~+/-6%); C_p90 1.18-1.35 (more
sector-dependent — Tech/Financials carry fatter tails). Driver is trend/gap/
event-density, not beta (Financials cluster with Tech despite moderate ATR%).
Companion to Reports/atr_move_heuristic_validation_20260608.md.
"""
import yfinance as yf, numpy as np, pandas as pd

SEC = {
    'Tech/Semi':  ['AAPL','MSFT','NVDA','AVGO','AMD','MU','AMAT','ORCL','CRM','QCOM'],
    'Healthcare': ['LLY','JNJ','ABBV','UNH','MRK','TMO','ABT','ISRG','AMGN','PFE'],
    'Staples':    ['PG','KO','PEP','CL','KMB','MO','WMT','MDLZ'],
    'Energy':     ['XOM','CVX','COP','SLB','EOG','MPC','VLO','PSX'],
    'Financials': ['JPM','BAC','GS','MS','C','WFC','AXP','SCHW'],
}
N = 10; sq = np.sqrt(N)
allt = sorted({t for v in SEC.values() for t in v})

def watr(df, n=14):
    pc = df['Close'].shift(1)
    tr = pd.concat([df['High']-df['Low'], (df['High']-pc).abs(), (df['Low']-pc).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1/n, adjust=False).mean()

data = yf.download(allt, period='5y', interval='1d', auto_adjust=True, progress=False, group_by='ticker')

def stats(t):
    df = data[t].dropna(); c = df['Close']
    if len(df) < 300:
        return None
    atr = (watr(df)/c*100).median()
    m = (c.shift(-N)/c - 1).dropna().abs()*100
    return atr, m.median()/(atr*sq), m.quantile(.90)/(atr*sq)

rows = []
for s, ts in SEC.items():
    cm = []; cp = []; at = []
    for t in ts:
        r = stats(t)
        if r:
            at.append(r[0]); cm.append(r[1]); cp.append(r[2])
    cm = np.array(cm); cp = np.array(cp); at = np.array(at)
    rows.append((s, len(cm), at.mean(), cm.mean(), cm.std(), cp.mean(), cp.std()))

print(f'{"Sector":>11} {"n":>2} {"ATR%":>5} | {"C_med":>6} {"sd":>5} | {"C_p90":>6} {"sd":>5}')
for s, n, a, m, ms, p, ps in rows:
    print(f'{s:>11} {n:>2} {a:>5.2f} | {m:>6.3f} {ms:>5.3f} | {p:>6.3f} {ps:>5.3f}')
allcm = [r[3] for r in rows]; allcp = [r[5] for r in rows]
print(f'\nCross-sector spread: C_med {min(allcm):.3f}-{max(allcm):.3f} (range {max(allcm)-min(allcm):.3f})'
      f'  C_p90 {min(allcp):.3f}-{max(allcp):.3f} (range {max(allcp)-min(allcp):.3f})')
print('ATR% (level) carries the "tech is wild" effect; C (shape) is far more universal.')
