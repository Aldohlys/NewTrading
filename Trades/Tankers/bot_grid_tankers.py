"""
BOT Grid Analysis for TNK and STNG — Pull vol metrics + option chain from IBKR TWS
"""
import sys
import importlib.util
import json

# Import tdata_py directly to avoid dependency chain
tdata_path = r"C:\Users\aldoh\Documents\RApplication\Tdata\inst\python\tdata_py"
sys.path.insert(0, r"C:\Users\aldoh\Documents\RApplication\Tdata\inst\python")

from tdata_py.impliedvol import get_volatility_metrics, get_iv_percentile_levels
from tdata_py.contract import getOptValue
from tdata_py.chains_manager import getChains

results = {}

for sym in ["TNK", "STNG"]:
    print(f"\n{'='*60}")
    print(f"  {sym} — VOL METRICS")
    print(f"{'='*60}")

    # 1. Get comprehensive vol metrics (IV + HV + price)
    vol = get_volatility_metrics(sym, secType="STK", currency="USD", exchange="SMART",
                                  lookback_days=252, hist=True, price=True)
    if vol:
        print(f"\n--- Volatility Metrics ---")
        for k, v in vol.items():
            if isinstance(v, float):
                print(f"  {k}: {v:.4f}")
            else:
                print(f"  {k}: {v}")

    # 2. Get IV percentile levels
    ivp = get_iv_percentile_levels(sym, secType="STK", currency="USD", exchange="SMART",
                                    lookback_days=252)
    if ivp:
        print(f"\n--- IV Percentile Levels ---")
        for k, v in ivp.items():
            if isinstance(v, float):
                print(f"  {k}: {v:.4f}")
            else:
                print(f"  {k}: {v}")

    # 3. Get option chains to find available expirations
    chains = getChains(sym, secType="STK", currency="USD", exchangeSec="SMART", exchangeOpt="SMART")

    near_exp = None
    next_exp = None
    available_strikes = []

    if chains and isinstance(chains, list) and len(chains) > 0:
        # Get expirations sorted
        all_exps = sorted(chains[0][4])
        available_strikes = sorted(chains[0][5])

        # Find near-term (20-40 DTE) and next-term (40-70 DTE) expirations
        from datetime import datetime, timedelta
        today = datetime.now()

        print(f"\n--- Available Expirations (next 4 months) ---")
        for exp in all_exps:
            exp_date = datetime.strptime(exp, "%Y%m%d")
            dte = (exp_date - today).days
            if 0 < dte < 120:
                print(f"  {exp} (DTE: {dte})")
                if near_exp is None and 20 <= dte <= 45:
                    near_exp = exp
                elif next_exp is None and dte > 45:
                    next_exp = exp

        # Get current price from vol metrics
        current_price = vol.get('current_price', None) if vol else None
        print(f"\n  Current price: {current_price}")

        # Find ATM strikes
        if current_price and available_strikes:
            atm_strikes = sorted(available_strikes, key=lambda s: abs(s - current_price))[:10]
            print(f"  Nearest strikes: {atm_strikes}")

        # 4. Get option chain data for near-term expiration
        if near_exp and current_price:
            # Select strikes around ATM (±15%)
            low = current_price * 0.85
            high = current_price * 1.15
            chain_strikes = [s for s in available_strikes if low <= s <= high]

            print(f"\n--- Option Chain: {near_exp} ---")
            print(f"  Strikes: {chain_strikes}")

            # Get calls
            calls = getOptValue(sym, near_exp, chain_strikes, 'C', currency="USD")
            if calls is not None:
                print(f"\n  CALLS:")
                print(calls.to_string(index=False))

            # Get puts
            puts = getOptValue(sym, near_exp, chain_strikes, 'P', currency="USD")
            if puts is not None:
                print(f"\n  PUTS:")
                print(puts.to_string(index=False))

            # Also get next-term if available
            if next_exp:
                print(f"\n--- Option Chain: {next_exp} ---")
                calls2 = getOptValue(sym, next_exp, chain_strikes, 'C', currency="USD")
                if calls2 is not None:
                    print(f"\n  CALLS:")
                    print(calls2.to_string(index=False))

                puts2 = getOptValue(sym, next_exp, chain_strikes, 'P', currency="USD")
                if puts2 is not None:
                    print(f"\n  PUTS:")
                    print(puts2.to_string(index=False))

    # Store results
    results[sym] = {"vol": vol, "ivp": ivp, "near_exp": near_exp, "next_exp": next_exp}

print(f"\n{'='*60}")
print("  DONE — All data collected")
print(f"{'='*60}")
