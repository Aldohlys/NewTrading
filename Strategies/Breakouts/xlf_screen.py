"""XLF component BOT-gate screen + beta/pay-for-entry filter — current bars via yfinance.

Mirrors xlv_screen.py (Setup S1-S6 + Breakout BK1-BK4 gates from
bot_strategy_checklist.md, EMA50 basis, RS vs sector ETF) and folds in the
ATR%/pay-for-entry filter from reference_atr_move_multiples.md so that
low-beta names (where selling an OTM call won't pay for entry) are flagged
automatically rather than judged by eye.

Pay-for-entry: P(>=6% |move| in 10 sessions) over 5y daily, the proxy for
"an OTM call can ~triple". Buckets (validated 2026-06-08):
  ATR ~1.5%  -> P ~6-8%   long calls structurally lose -> shares or SELL vol
  ATR ~2.0%  -> P ~18-25% spreads / pay-for-entry discipline
  ATR ~4%    -> P ~53-58% long OTM calls in sweet spot
"""
import yfinance as yf
import pandas as pd
import numpy as np

SECTOR_ETF = "XLF"
H = 10          # horizon (sessions) for the move/payable stats
PAYABLE = 6.0   # % move proxy for "OTM call can triple"

# Top XLF holdings (financials). BRK-B = Berkshire B-share on Yahoo.
TICKERS = ["XLF","BRK-B","JPM","V","MA","BAC","WFC","GS","SPGI","MS",
           "AXP","PGR","BLK","C","CB","MMC","FI","SCHW","BX","CME","BK"]

def rsi(series, n=14):
    d = series.diff()
    up = d.clip(lower=0).ewm(alpha=1/n, adjust=False).mean()
    dn = (-d.clip(upper=0)).ewm(alpha=1/n, adjust=False).mean()
    rs = up / dn.replace(0, np.nan)
    return 100 - 100/(1+rs)

def wilder_atr(df, n=14):
    pc = df["Close"].shift(1)
    tr = pd.concat([df["High"]-df["Low"], (df["High"]-pc).abs(),
                    (df["Low"]-pc).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1/n, adjust=False).mean()

# 5y daily for the payable/beta stats; gates use the tail.
data = yf.download(TICKERS, period="5y", interval="1d",
                   auto_adjust=True, progress=False, group_by="ticker")

sec = data[SECTOR_ETF]["Close"].dropna()
sec_ret_3m = sec.iloc[-1]/sec.iloc[-63] - 1 if len(sec) > 63 else np.nan

def bucket(atr_pct):
    if atr_pct < 1.7:  return "LOW  shares/sell-vol"
    if atr_pct < 2.7:  return "MID  spread"
    return "HIGH long-call"

rows = []
for t in TICKERS:
    try:
        df = data[t].dropna().copy()
    except Exception:
        continue
    if len(df) < 300:
        continue
    c = df["Close"]; v = df["Volume"]; h = df["High"]; l = df["Low"]
    ema50 = c.ewm(span=50, adjust=False).mean()
    price = c.iloc[-1]; ema = ema50.iloc[-1]
    ema_slope = (ema50.iloc[-1]/ema50.iloc[-6]-1)*100
    dist_ema = (price/ema-1)*100
    r = rsi(c); rsi_now = r.iloc[-1]; rsi_slope = r.iloc[-1]-r.iloc[-4]
    obv = (np.sign(c.diff()).fillna(0)*v).cumsum()
    obv_slope = obv.iloc[-1]-obv.iloc[-21]
    ret_3m = price/c.iloc[-63]-1 if len(c) > 63 else np.nan
    rs_vs_sec = (ret_3m - sec_ret_3m)*100 if t != SECTOR_ETF else 0.0
    rng20 = (h.rolling(20).max()-l.rolling(20).min()).iloc[-1]
    rng40 = (h.rolling(40).max()-l.rolling(40).min()).iloc[-1]
    squeeze = rng20/rng40 if rng40 else np.nan
    vdec = v.rolling(20).mean().iloc[-1]/v.rolling(50).mean().iloc[-1]
    up_v = v[c.diff() > 0].iloc[-20:].sum(); dn_v = v[c.diff() < 0].iloc[-20:].sum()
    ud = up_v/dn_v if dn_v else np.nan
    hi20 = h.rolling(20).max().iloc[-1]; lo20 = l.rolling(20).min().iloc[-1]
    rng_pct = (price-lo20)/(hi20-lo20)*100 if hi20 > lo20 else np.nan
    vsurge = v.iloc[-1]/v.rolling(20).mean().iloc[-1]

    # --- beta / pay-for-entry (5y) ---
    atr_pct = (wilder_atr(df)/c*100).median()
    fwd = (c.shift(-H)/c - 1).dropna().abs()*100
    p_pay = (fwd >= PAYABLE).mean()*100
    typ10 = 1.5*atr_pct          # typical 10d move
    strong10 = 4.0*atr_pct       # strong (p90) 10d move

    S1 = price > ema; S2 = ema_slope > 0; S3 = rs_vs_sec > 0
    S4 = obv_slope > 0; S5 = squeeze < 0.65; S6 = vdec < 0.95
    BK1 = (rsi_now > 50) and (rsi_slope > 0); BK2 = ud > 1.1
    BK3 = rng_pct >= 70; BK4 = vsurge >= 1.2
    S = sum([S1,S2,S3,S4,S5,S6]); BK = sum([BK1,BK2,BK3,BK4])
    if S >= 5 and BK >= 3: sig = "GREEN"
    elif (S >= 5 and BK >= 1) or (S >= 4 and BK >= 3): sig = "AMBER"
    else: sig = "grey"
    rows.append(dict(t=t, px=round(price,2), dEMA=round(dist_ema,1),
                     slope=round(ema_slope,2), rsi=round(rsi_now,0),
                     rs_sec=round(rs_vs_sec,1), sqz=round(squeeze,2),
                     rngpct=round(rng_pct,0), vsrg=round(vsurge,2),
                     atrp=round(atr_pct,2), typ10=round(typ10,1),
                     strg10=round(strong10,1), Ppay=round(p_pay,0),
                     vehicle=bucket(atr_pct),
                     S=S, BK=BK, gates=f"S{S}/BK{BK}", sig=sig,
                     SB=f"{int(S1)}{int(S2)}{int(S3)}{int(S4)}{int(S5)}{int(S6)}",
                     BKb=f"{int(BK1)}{int(BK2)}{int(BK3)}{int(BK4)}"))

out = pd.DataFrame(rows).sort_values(["S","BK","dEMA"], ascending=False)
pd.set_option("display.width", 240, "display.max_columns", 40)
print(f"\nSector XLF 3m return: {sec_ret_3m*100:+.1f}%")
print("Gate cols: SB=S1S2S3S4S5S6  BKb=BK1BK2BK3BK4")
print("Beta cols: atrp=ATR%  typ10/strg10=typical/strong 10d move%  Ppay=P(>=6%/10d)  vehicle by ATR%\n")
print(out.to_string(index=False))

print("\n--- Adequate-beta breakout candidates (atrp>=1.7 AND S>=4) ---")
cand = out[(out.atrp >= 1.7) & (out.S >= 4) & (out.t != SECTOR_ETF)]
print(cand[["t","px","gates","sig","dEMA","slope","rs_sec","atrp","Ppay","vehicle"]].to_string(index=False)
      if len(cand) else "  (none)")

print("\n--- Low-beta names filtered OUT (atrp<1.7: OTM call won't pay) ---")
low = out[(out.atrp < 1.7) & (out.t != SECTOR_ETF)]
print(", ".join(f"{r.t}({r.atrp})" for r in low.itertuples()) if len(low) else "  (none)")
