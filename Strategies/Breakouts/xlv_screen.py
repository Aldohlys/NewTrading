"""XLV component BOT-gate screen — current bars via yfinance.
Computes the Setup (S1/S2/S3-proxy/S4/S5/S6) and Breakout (BK1-BK4) gates
from bot_strategy_checklist.md on the latest data. EMA50 basis.
RS (S3) is computed vs XLV (sector ETF), not vs SPY.
"""
import yfinance as yf
import pandas as pd
import numpy as np

SECTOR_ETF = "XLV"
# Top XLV holdings (will reconcile weights from web)
TICKERS = ["XLV","LLY","UNH","JNJ","ABBV","MRK","TMO","ABT","ISRG",
           "AMGN","DHR","PFE","BMY","BSX","GILD","VRTX","MDT","SYK","EW","DXCM"]

def rsi(series, n=14):
    d = series.diff()
    up = d.clip(lower=0).ewm(alpha=1/n, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1/n, adjust=False).mean()
    rs = up / dn.replace(0, np.nan)
    return 100 - 100/(1+rs)

# Download ~10 months daily
data = yf.download(TICKERS, period="10mo", interval="1d",
                   auto_adjust=True, progress=False, group_by="ticker")

# sector ETF close for RS
sec = data[SECTOR_ETF]["Close"].dropna()
sec_ret_3m = sec.iloc[-1]/sec.iloc[-63] - 1 if len(sec) > 63 else np.nan

rows = []
for t in TICKERS:
    try:
        df = data[t].dropna().copy()
    except Exception:
        continue
    if len(df) < 70:
        continue
    c = df["Close"]; v = df["Volume"]; h = df["High"]; l = df["Low"]
    ema50 = c.ewm(span=50, adjust=False).mean()
    price = c.iloc[-1]
    ema = ema50.iloc[-1]
    ema_slope = (ema50.iloc[-1]/ema50.iloc[-6]-1)*100   # 5-bar % slope
    dist_ema = (price/ema-1)*100
    r = rsi(c); rsi_now = r.iloc[-1]; rsi_slope = r.iloc[-1]-r.iloc[-4]
    # OBV
    obv = (np.sign(c.diff()).fillna(0)*v).cumsum()
    obv_slope = obv.iloc[-1]-obv.iloc[-21]
    # RS vs sector (3m)
    ret_3m = price/c.iloc[-63]-1 if len(c) > 63 else np.nan
    rs_vs_sec = (ret_3m - sec_ret_3m)*100 if t != SECTOR_ETF else 0.0
    # Squeeze: range_20/range_40
    rng20 = (h.rolling(20).max()-l.rolling(20).min()).iloc[-1]
    rng40 = (h.rolling(40).max()-l.rolling(40).min()).iloc[-1]
    squeeze = rng20/rng40 if rng40 else np.nan
    # Volume decline 20/50
    vdec = v.rolling(20).mean().iloc[-1]/v.rolling(50).mean().iloc[-1]
    # Up/down vol ratio (20d)
    up_v = v[c.diff() > 0].iloc[-20:].sum(); dn_v = v[c.diff() < 0].iloc[-20:].sum()
    ud = up_v/dn_v if dn_v else np.nan
    # Range position (20d)
    hi20 = h.rolling(20).max().iloc[-1]; lo20 = l.rolling(20).min().iloc[-1]
    rng_pct = (price-lo20)/(hi20-lo20)*100 if hi20 > lo20 else np.nan
    # Volume surge today vs 20d avg
    vsurge = v.iloc[-1]/v.rolling(20).mean().iloc[-1]
    atr_pct = (h-l).rolling(14).mean().iloc[-1]/price*100

    S1 = price > ema
    S2 = ema_slope > 0
    S3 = rs_vs_sec > 0
    S4 = obv_slope > 0
    S5 = squeeze < 0.65
    S6 = vdec < 0.95
    BK1 = (rsi_now > 50) and (rsi_slope > 0)
    BK2 = ud > 1.1
    BK3 = rng_pct >= 70
    BK4 = vsurge >= 1.2
    S = sum([S1,S2,S3,S4,S5,S6]); BK = sum([BK1,BK2,BK3,BK4])
    if S >= 5 and BK >= 3: sig = "GREEN"
    elif (S >= 5 and BK >= 1) or (S >= 4 and BK >= 3): sig = "AMBER"
    else: sig = "grey"
    rows.append(dict(t=t, px=round(price,2), dEMA=round(dist_ema,1),
                     slope=round(ema_slope,2), rsi=round(rsi_now,0),
                     rs_sec=round(rs_vs_sec,1), sqz=round(squeeze,2),
                     rngpct=round(rng_pct,0), vsrg=round(vsurge,2),
                     atrp=round(atr_pct,1),
                     S=S, BK=BK, gates=f"S{S}/BK{BK}", sig=sig,
                     SB=f"{int(S1)}{int(S2)}{int(S3)}{int(S4)}{int(S5)}{int(S6)}",
                     BKb=f"{int(BK1)}{int(BK2)}{int(BK3)}{int(BK4)}"))

out = pd.DataFrame(rows).sort_values(["S","BK","dEMA"], ascending=False)
pd.set_option("display.width", 200, "display.max_columns", 30)
print(f"\nSector XLV 3m return: {sec_ret_3m*100:+.1f}%\n")
print(out.to_string(index=False))
