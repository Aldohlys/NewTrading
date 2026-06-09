"""Empirically validate the ATR -> 10-day-move heuristic.
Heuristic under test: a 'strong' 10-day move ~ 3-4 x daily ATR%.
Theory (random walk, ATR~1.4*sigma): median ~1.5x ATR%, p90 ~3.7x ATR%, 10d_sigma/1d_sigma ~3.16.
Pure OHLC test (realized), 5y daily.
"""
import yfinance as yf, numpy as np, pandas as pd

UNIV = {
  "PG":"low","KO":"low","PEP":"low","JNJ":"low",
  "ABBV":"mid","MRK":"mid","UNH":"mid","TMO":"mid","XLV":"mid",
  "NVDA":"high","TSLA":"high","AMD":"high",
}
H = 10        # horizon (sessions)
PAYABLE = 6.0 # % move proxy for "OTM call can triple"

def wilder_atr(df, n=14):
    pc = df["Close"].shift(1)
    tr = pd.concat([df["High"]-df["Low"], (df["High"]-pc).abs(), (df["Low"]-pc).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1/n, adjust=False).mean()

data = yf.download(list(UNIV), period="5y", interval="1d", auto_adjust=True, progress=False, group_by="ticker")
rows=[]
for t in UNIV:
    df = data[t].dropna().copy()
    if len(df) < 300: continue
    c = df["Close"]
    atr = wilder_atr(df); atr_pct = (atr/c*100).dropna()
    atr_med = atr_pct.median()
    lr = np.log(c/c.shift(1)).dropna()
    sig_d = lr.std()*100                          # daily close-close sigma %
    sig_10 = (np.log(c/c.shift(H)).dropna()).std()*100   # realized 10d sigma %
    fwd = (c.shift(-H)/c - 1).dropna()*100         # 10d forward % (signed)
    amove = fwd.abs()
    med, p75, p90 = amove.median(), amove.quantile(.75), amove.quantile(.90)
    p_pay = (amove >= PAYABLE).mean()*100          # P(|10d move| >= 6%)
    rows.append(dict(t=t, beta=UNIV[t],
        ATRpct=round(atr_med,2), sigD=round(sig_d,2), ATR_over_sig=round(atr_med/sig_d,2),
        sig10_over_sigD=round(sig_10/sig_d,2),
        med10=round(med,1), p75_10=round(p75,1), p90_10=round(p90,1),
        k_med=round(med/atr_med,2), k_p90=round(p90/atr_med,2),
        Ppayable=round(p_pay,0)))

out = pd.DataFrame(rows).sort_values("ATRpct")
pd.set_option("display.width",200,"display.max_columns",30)
print("\nPer-name (5y daily, H=10 sessions):\n")
print(out.to_string(index=False))
print("\nLegend: k_med = median 10d|move| / ATR%  (theory~1.52)")
print("        k_p90 = p90 10d|move| / ATR%      (theory~3.72)")
print("        sig10_over_sigD: realized 10d/1d sigma (theory sqrt10=3.16)")
print(f"        Ppayable = P(|10d move| >= {PAYABLE}%)  [proxy: OTM call can ~3x]")
print(f"\nPooled means: k_med={out.k_med.mean():.2f}  k_p90={out.k_p90.mean():.2f}  "
      f"sig-ratio={out.sig10_over_sigD.mean():.2f}  ATR/sig={out.ATR_over_sig.mean():.2f}")
print("\nBy beta bucket (k_p90 = the 'strong move' multiple):")
print(out.groupby("beta")[["ATRpct","k_med","k_p90","Ppayable"]].mean().round(2).to_string())
