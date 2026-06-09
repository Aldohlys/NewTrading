"""Stress-test the ATR-move coefficients (C_med~0.48, C_p90~1.25) OUTSIDE their
original calibration domain (60 US single-names, 1-5% ATR, ~10d horizon).

Model under test:  |N-day move|  ~  C * ATR% * sqrt(N)
  - If C is a universal *shape* (level lives in ATR%) it should be ~flat across
    asset class AND across horizon N.
  - C rising with N  => trending/momentum (super-diffusive).
  - C falling with N => mean reversion (sub-diffusive).
  - sqrt(N) scaling test: move_N / move_1  vs  sqrt(N).

Pure OHLC realized test, ~8y daily, auto-adjusted.
"""
import yfinance as yf, numpy as np, pandas as pd

# label -> (yahoo ticker, asset class)
UNIV = {
  # US ETFs
  "SPY":("SPY","ETF-eq"), "IWM":("IWM","ETF-eq"), "QQQ":("QQQ","ETF-eq"),
  # commodity ETFs
  "GLD":("GLD","ETF-cmdty"), "SLV":("SLV","ETF-cmdty"), "USO":("USO","ETF-cmdty"),
  # US single names
  "STNG":("STNG","US-stock"), "MP":("MP","US-stock"), "NVDA":("NVDA","US-stock"), "PG":("PG","US-stock"),
  # European single names
  "MT":("MT","EU-stock"), "OR.PA":("OR.PA","EU-stock"), "ROG.SW":("ROG.SW","EU-stock"),
  "CA.PA":("CA.PA","EU-stock"), "CRST.L":("CRST.L","EU-stock"),
  # Asian (Tokyo) + Canada
  "JP-3440":("3440.T","JP-stock"), "JP-5982":("5982.T","JP-stock"), "JP-6797":("6797.T","JP-stock"),
  "JP-7399":("7399.T","JP-stock"), "JP-9273":("9273.T","JP-stock"), "MRD.TO":("MRD.TO","CA-stock"),
  # FX
  "EURUSD":("EURUSD=X","FX"),
  # Futures (continuous; roll artifacts -- caveat)
  "CL=F":("CL=F","Future"),
}
HORIZONS = [3, 5, 10, 20, 40, 60]

def wilder_atr(df, n=14):
    pc = df["Close"].shift(1)
    tr = pd.concat([df["High"]-df["Low"], (df["High"]-pc).abs(), (df["Low"]-pc).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1/n, adjust=False).mean()

def fetch(tk):
    try:
        df = yf.download(tk, period="8y", interval="1d", auto_adjust=True, progress=False)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        return df.dropna()
    except Exception as e:
        print(f"  !! {tk}: {e}"); return None

rows=[]
for lab,(tk,cls) in UNIV.items():
    df = fetch(tk)
    if df is None or len(df) < 400:
        print(f"  skip {lab} ({tk}): insufficient data ({0 if df is None else len(df)})"); continue
    c = df["Close"]
    atr_pct = (wilder_atr(df)/c*100).dropna()
    atr_med = atr_pct.median()
    sig_d = (np.log(c/c.shift(1)).dropna()).std()*100
    rec = dict(label=lab, cls=cls, ATRpct=round(atr_med,2), sigD=round(sig_d,2),
               ATRoverSig=round(atr_med/sig_d,2), n=len(df))
    move1 = (c.shift(-1)/c - 1).abs().dropna()*100
    m1_med = move1.median()
    for N in HORIZONS:
        fwd = (c.shift(-N)/c - 1).dropna().abs()*100
        if len(fwd) < 100: continue
        med, p90 = fwd.median(), fwd.quantile(.90)
        rec[f"Cmed{N}"] = round(med/(atr_med*np.sqrt(N)),2)
        rec[f"Cp90{N}"] = round(p90/(atr_med*np.sqrt(N)),2)
        rec[f"scale{N}"] = round((med/m1_med)/np.sqrt(N),2)   # 1.0 = perfect sqrt(N)
    rows.append(rec)

out = pd.DataFrame(rows)
pd.set_option("display.width",260,"display.max_columns",60)

print("\n=== ATR% level + ATR/sigma ratio by name ===")
print(out[["label","cls","ATRpct","sigD","ATRoverSig","n"]].sort_values("ATRpct").to_string(index=False))

print("\n=== C_med  (target 0.48) by horizon ===")
cm = [f"Cmed{N}" for N in HORIZONS]
print(out[["label","cls"]+cm].to_string(index=False))

print("\n=== C_p90  (target 1.25) by horizon ===")
cp = [f"Cp90{N}" for N in HORIZONS]
print(out[["label","cls"]+cp].to_string(index=False))

print("\n=== sqrt(N) scaling: move_N/move_1 / sqrt(N)  (1.0=random walk, >1 trend, <1 mean-revert) ===")
sc = [f"scale{N}" for N in HORIZONS]
print(out[["label","cls"]+sc].to_string(index=False))

print("\n=== Pooled by asset class (mean) ===")
agg = out.groupby("cls")[["ATRpct","Cmed10","Cp9010","Cmed20","Cp9020","scale20","scale40"]].mean().round(2)
print(agg.to_string())
print(f"\nGRAND MEAN  C_med10={out.Cmed10.mean():.2f}  C_p9010={out.Cp9010.mean():.2f}  "
      f"C_med20={out.Cmed20.mean():.2f}  C_p9020={out.Cp9020.mean():.2f}  ATR/sig={out.ATRoverSig.mean():.2f}")
