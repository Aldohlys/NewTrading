"""Validate the ATR pay-for-entry framework against actual BOT trades.
Hypothesis: BOT winners skew toward RICH-ATR names; low-ATR names fail
(can't produce the move to pay for an option entry). ATR measured AT TRADE DATE.
"""
import sqlite3, datetime as dt
import yfinance as yf, numpy as np, pandas as pd

DB = r"C:/Users/aldoh/Documents/RApplication/data/mydb.db"
con = sqlite3.connect(DB)
# pull per-leg, classify vehicle from the Instrument string (Right col is half-null)
raw = pd.read_sql("SELECT TradeNr, Ssjacent AS tk, TradeDate, PnL, Instrument FROM Trades WHERE Strategy='BOT';", con)
con.close()

def is_option(instr):
    # option legs look like 'AAPL 26JAN24 190 C' / 'SMH 18JUN26 547.5 P' -> last token C/P
    return str(instr).strip().split()[-1] in ("C", "P") if str(instr).strip() else False

raw["opt_leg"] = raw["Instrument"].map(is_option)
g = raw.groupby("TradeNr")
tr = pd.DataFrame({
    "tk": g["tk"].first(),
    "entry": g["TradeDate"].min(),
    "pnl": g["PnL"].sum().round(0),
    "is_opt": g["opt_leg"].max().astype(int),
}).reset_index()
tr = tr[tr["pnl"].abs() > 0.01].sort_values("entry").reset_index(drop=True)

# map to yfinance symbols (futures/foreign)
YF = {"GCM5":"GC=F","MCL":"CL=F","KNIN":"KNIN.SW","SAF":"SAF.PA","SU":"SU.PA"}
tr["yf"] = tr["tk"].map(lambda t: YF.get(t, t))
tr["entry_dt"] = pd.to_datetime(tr["entry"].astype(str), format="%Y%m%d")

def watr_pct_asof(sym, asof):
    try:
        h = yf.download(sym, start="2021-06-01", end=(asof+pd.Timedelta(days=2)).strftime("%Y-%m-%d"),
                        interval="1d", auto_adjust=True, progress=False)
        if isinstance(h.columns, pd.MultiIndex): h = h.xs(sym, axis=1, level=1)
        h = h.dropna()
        if len(h) < 20: return np.nan
        pc = h["Close"].shift(1)
        tr_ = pd.concat([h["High"]-h["Low"], (h["High"]-pc).abs(), (h["Low"]-pc).abs()],axis=1).max(axis=1)
        atr = tr_.ewm(alpha=1/14, adjust=False).mean()
        return float((atr/h["Close"]*100).iloc[-1])
    except Exception:
        return np.nan

tr["atr_pct"] = [watr_pct_asof(r.yf, r.entry_dt) for r in tr.itertuples()]
tr["win"] = tr["pnl"] > 0
res = tr.dropna(subset=["atr_pct"]).copy()
miss = tr[tr["atr_pct"].isna()]["tk"].tolist()

def bucket(a):
    return "low <1.7" if a < 1.7 else ("mid 1.7-3" if a < 3.0 else "high >=3")
res["b"] = res["atr_pct"].map(bucket)

pd.set_option("display.width",200,"display.max_columns",30)
print(f"\nTrades analyzed: {len(res)}  (excluded, no ATR: {miss})\n")

print("=== Winners vs Losers — ATR% distribution ===")
for lab,g in [("WINNERS",res[res.win]),("LOSERS",res[~res.win])]:
    a=g["atr_pct"]
    print(f"{lab:>8}: n={len(g):>3}  median ATR%={a.median():.2f}  mean={a.mean():.2f}  "
          f"avgPnL={g.pnl.mean():>6.0f}  medPnL={g.pnl.median():>6.0f}")

print("\n=== By ATR bucket ===")
g = res.groupby("b").agg(n=("pnl","size"), win_rate=("win","mean"),
        avg_pnl=("pnl","mean"), med_pnl=("pnl","median"),
        tot_pnl=("pnl","sum"), med_atr=("atr_pct","median"))
g["win_rate"]=(g["win_rate"]*100).round(0)
print(g.round(1).reindex(["low <1.7","mid 1.7-3","high >=3"]).to_string())

print("\n=== Big winners (PnL >= 500) — were they rich-ATR? ===")
bw = res[res.pnl>=500].sort_values("pnl",ascending=False)
print(bw[["tk","entry","pnl","atr_pct","b","is_opt"]].to_string(index=False))

print("\n=== Correlation PnL vs ATR% ===")
print(f"  Pearson r = {res['pnl'].corr(res['atr_pct']):.3f}  |  "
      f"Spearman = {res['pnl'].corr(res['atr_pct'],method='spearman'):.3f}")

print("\n=== Options-vehicle subset only (pay-for-entry applies) ===")
o=res[res.is_opt==1]
for lab,gg in [("WIN",o[o.win]),("LOSE",o[~o.win])]:
    print(f"  {lab}: n={len(gg):>3} median ATR%={gg.atr_pct.median():.2f} avgPnL={gg.pnl.mean():.0f}")
go=o.groupby("b").agg(n=("pnl","size"),win_rate=("win","mean"),avg_pnl=("pnl","mean")).reindex(["low <1.7","mid 1.7-3","high >=3"])
go["win_rate"]=(go["win_rate"]*100).round(0)
print(go.round(1).to_string())
