"""Verify XOP recent price action + IV30 history.
Question: is XOP down on the week? Is IV30 already coming off?
"""
import sys
from pathlib import Path

PKG_ROOT = Path(r"C:/Users/aldoh/Documents/RApplication/Tdata/inst/python")
sys.path.insert(0, str(PKG_ROOT))

import tdata_py
import yfinance as yf
import pandas as pd

# ── Recent price action (yfinance) ──────────────────────────────────────
t = yf.Ticker("XOP")
df = t.history(period="3mo", interval="1d", auto_adjust=False)
df = df.tail(25).copy()
df["chg%"] = df["Close"].pct_change() * 100
df["roll5d%"] = df["Close"].pct_change(5) * 100

print("=== XOP daily (last 25 sessions) ===")
print(df[["Open","High","Low","Close","Volume","chg%","roll5d%"]].round(2).to_string())

last = df["Close"].iloc[-1]
print(f"\n5d return:  {(last/df['Close'].iloc[-6]-1)*100:+.2f}%")
print(f"10d return: {(last/df['Close'].iloc[-11]-1)*100:+.2f}%")
print(f"20d return: {(last/df['Close'].iloc[-21]-1)*100:+.2f}%")

# ── Realized vol path ───────────────────────────────────────────────────
import numpy as np
ret = np.log(df["Close"] / df["Close"].shift(1)).dropna()
print(f"\nRV(20d, annualized): {ret.tail(20).std()*np.sqrt(252)*100:.1f}%")
print(f"RV(10d, annualized): {ret.tail(10).std()*np.sqrt(252)*100:.1f}%")
print(f"RV(5d, annualized):  {ret.tail(5).std()*np.sqrt(252)*100:.1f}%")

# ── IV30 history via Tdata IV history (IBKR HISTORICAL_VOLATILITY) ───────
if not tdata_py.IB_connection.isIBAvailable():
    print("\nIB not available — skipping IV history")
    sys.exit(0)

iv_hist = tdata_py.iv.getIvHistory(symbol="XOP", currency="USD", days=60)
if iv_hist is None or iv_hist.empty:
    print("\nIV history empty")
    sys.exit(0)

iv_hist = iv_hist.tail(30).copy()
print("\n=== XOP IV30 daily history (last 30 sessions, IBKR) ===")
print(iv_hist.round(3).to_string())
