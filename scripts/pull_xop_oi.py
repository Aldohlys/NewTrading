"""Pull live XOP option-chain open interest for the 20260626 expiry,
sorted by OI desc, with right (C/P) clearly labeled. Used to verify
the analyze pipeline's oi_cap_call / oi_cap_put values.
"""
import sys
import importlib.util
from pathlib import Path

PKG_ROOT = Path(r"C:/Users/aldoh/Documents/RApplication/Tdata/inst/python")
sys.path.insert(0, str(PKG_ROOT))

import tdata_py
from tdata_py import IB_connection, contract  # noqa: F401

EXPIRY = "20260626"
SYM = "XOP"

if not tdata_py.IB_connection.isIBAvailable():
    print("IB not available — start TWS first")
    sys.exit(1)

# Pull OI for a wide band around spot
spot = 166.10
band_min = spot * 0.75
band_max = spot * 1.25

df = tdata_py.chains_manager.get_chain_oi(
    sym=SYM, expiration=EXPIRY,
    strike_min=band_min, strike_max=band_max,
)

if df is None or df.empty:
    print(f"no rows for {SYM} @ {EXPIRY}")
    sys.exit(1)

# Sort by OI desc, show top 30
df = df.sort_values("open_interest", ascending=False)
print(f"\n=== XOP {EXPIRY} chain OI (band ${band_min:.2f}-${band_max:.2f}, spot ${spot:.2f}) ===")
print(df.head(30).to_string(index=False))

# Per-right top 10
print("\n=== CALLS top 10 ===")
calls = df[df["right"] == "C"].head(10)
print(calls.to_string(index=False))

print("\n=== PUTS top 10 ===")
puts = df[df["right"] == "P"].head(10)
print(puts.to_string(index=False))

# What the analyze pipeline would pick
print("\n=== Pipeline picks ===")
calls_all = df[df["right"] == "C"]
puts_all = df[df["right"] == "P"]
if not calls_all.empty:
    cap_c_row = calls_all.iloc[calls_all["open_interest"].argmax()]
    print(f"oi_cap_call = ${cap_c_row['strike']:.2f}  (OI={cap_c_row['open_interest']:.0f})")
if not puts_all.empty:
    cap_p_row = puts_all.iloc[puts_all["open_interest"].argmax()]
    print(f"oi_cap_put  = ${cap_p_row['strike']:.2f}  (OI={cap_p_row['open_interest']:.0f})")
