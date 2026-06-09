"""Signed ATR-move quantile coefficients -> support arbitrary confidence intervals
AND asymmetry (separate up/down tails), not just the |move| p50/p90 (0.48/1.25).

For each obs: standardized = signed_Nday_move% / (ATR%*sqrt(N)).
Pool by asset class; report quantile coefficients. Up coef = q(0.80/0.90/0.95),
down coef = q(0.20/0.10/0.05). Asymmetry = up / |down| at matched tail.
"""
import yfinance as yf, numpy as np, pandas as pd

UNIV = {
  "SPY":"ETF-eq","IWM":"ETF-eq","QQQ":"ETF-eq",
  "GLD":"ETF-cmdty","SLV":"ETF-cmdty","USO":"ETF-cmdty",
  "STNG":"US-stk","MP":"US-stk","NVDA":"US-stk","PG":"US-stk",
  "MT":"EU-stk","OR.PA":"EU-stk","CA.PA":"EU-stk","CRST.L":"EU-stk",
  "3440.T":"JP-stk","5982.T":"JP-stk","6797.T":"JP-stk","7399.T":"JP-stk","9273.T":"JP-stk",
  "MRD.TO":"CA-stk","EURUSD=X":"FX","CL=F":"Future",
}
HORIZONS=[10,20]
QS=[0.05,0.10,0.20,0.50,0.80,0.90,0.95]

def wilder_atr(df,n=14):
    pc=df["Close"].shift(1)
    tr=pd.concat([df["High"]-df["Low"],(df["High"]-pc).abs(),(df["Low"]-pc).abs()],axis=1).max(axis=1)
    return tr.ewm(alpha=1/n,adjust=False).mean()

pool={N:{} for N in HORIZONS}   # N -> cls -> list of standardized signed moves
for tk,cls in UNIV.items():
    try:
        df=yf.download(tk,period="8y",interval="1d",auto_adjust=True,progress=False)
        if isinstance(df.columns,pd.MultiIndex): df.columns=df.columns.get_level_values(0)
        df=df.dropna()
    except Exception: continue
    if len(df)<400: continue
    c=df["Close"]; atr_pct=(wilder_atr(df)/c*100).dropna().median()
    for N in HORIZONS:
        sm=((c.shift(-N)/c-1)*100).dropna()/(atr_pct*np.sqrt(N))
        pool[N].setdefault(cls,[]).extend(sm.tolist())

for N in HORIZONS:
    print(f"\n=== N={N} sessions : signed-move quantile coefficients  C(q) = move% / (ATR%*sqrt(N)) ===")
    rows=[]
    for cls,vals in pool[N].items():
        v=np.array(vals); q={p:np.quantile(v,p) for p in QS}
        rows.append(dict(cls=cls, n=len(v),
            c05=round(q[.05],2), c10=round(q[.10],2), c20=round(q[.20],2),
            med=round(q[.50],2),
            c80=round(q[.80],2), c90=round(q[.90],2), c95=round(q[.95],2),
            asym80=round(q[.80]/abs(q[.20]),2), asym90=round(q[.90]/abs(q[.10]),2)))
    out=pd.DataFrame(rows).sort_values("cls")
    pd.set_option("display.width",200,"display.max_columns",30)
    print(out.to_string(index=False))
print("\nasym>1 = up tail bigger than down tail (positive skew); <1 = downside-heavy.")
print("80% CI band = [c20 , c80] x ATR% x sqrt(N) around spot ; 90% CI = [c10 , c90].")
