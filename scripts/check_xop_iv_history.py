"""Pull XOP daily IV30 and HV history from IBKR.
Verify if IV is already coming off recent highs."""
import sys
from pathlib import Path

PKG_ROOT = Path(r"C:/Users/aldoh/Documents/RApplication/Tdata/inst/python")
sys.path.insert(0, str(PKG_ROOT))

import tdata_py
from tdata_py.IB_connection import safe_ib_connect
from ib_async import Stock
import pandas as pd

if not tdata_py.IB_connection.isIBAvailable():
    print("IB not available")
    sys.exit(1)

ib = safe_ib_connect()
c = Stock("XOP", "SMART", "USD")
ib.qualifyContracts(c)

iv_bars = ib.reqHistoricalData(
    c, endDateTime="", durationStr="90 D", barSizeSetting="1 day",
    whatToShow="OPTION_IMPLIED_VOLATILITY", useRTH=True, formatDate=1,
)
hv_bars = ib.reqHistoricalData(
    c, endDateTime="", durationStr="90 D", barSizeSetting="1 day",
    whatToShow="HISTORICAL_VOLATILITY", useRTH=True, formatDate=1,
)

iv = pd.DataFrame([{"date": b.date, "iv30": b.close} for b in iv_bars])
hv = pd.DataFrame([{"date": b.date, "hv30": b.close} for b in hv_bars])
merged = iv.merge(hv, on="date", how="outer").sort_values("date")
merged["iv30%"] = (merged["iv30"]*100).round(1)
merged["hv30%"] = (merged["hv30"]*100).round(1)
merged["vrp"] = (merged["iv30"] - merged["hv30"]).round(3)

# IVP/RVP over the trailing 252d would need a 252d window — let me pull
# a longer window for that.
iv_long = ib.reqHistoricalData(
    c, endDateTime="", durationStr="365 D", barSizeSetting="1 day",
    whatToShow="OPTION_IMPLIED_VOLATILITY", useRTH=True, formatDate=1,
)
hv_long = ib.reqHistoricalData(
    c, endDateTime="", durationStr="365 D", barSizeSetting="1 day",
    whatToShow="HISTORICAL_VOLATILITY", useRTH=True, formatDate=1,
)
iv_long_s = pd.Series([b.close for b in iv_long])
hv_long_s = pd.Series([b.close for b in hv_long])

print(f"=== XOP IV30/HV30 daily — last 30 sessions (IBKR) ===")
print(merged.tail(30)[["date","iv30%","hv30%","vrp"]].to_string(index=False))

current_iv = merged["iv30"].iloc[-1]
current_hv = merged["hv30"].iloc[-1]
ivp = (iv_long_s < current_iv).sum() / len(iv_long_s) * 100
rvp = (hv_long_s < current_hv).sum() / len(hv_long_s) * 100

print(f"\n=== Summary ===")
print(f"Current IV30: {current_iv*100:.2f}%  | 1y IVP: {ivp:.1f}%")
print(f"Current HV30: {current_hv*100:.2f}%  | 1y HVP (=RVP): {rvp:.1f}%")
print(f"VRP (IV-HV):  {(current_iv-current_hv)*100:+.2f} vol-points")

# Path over last 1w / 2w / 1m
for n in [5, 10, 21]:
    prev_iv = merged["iv30"].iloc[-1-n]
    prev_hv = merged["hv30"].iloc[-1-n]
    print(f"\n{n}d ago: IV30={prev_iv*100:.2f}%, HV30={prev_hv*100:.2f}%  → ΔIV={(current_iv-prev_iv)*100:+.2f}vp, ΔHV={(current_hv-prev_hv)*100:+.2f}vp")

ib.sleep(0.5)
ib.disconnect()
