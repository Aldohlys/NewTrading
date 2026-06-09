"""TSLA: pull live OI for front expiry chain + run Tdata spread analyzer for risk-budget-bound spreads."""
import sys, json, os
sys.path.insert(0, r'C:/Users/aldoh/Documents/RApplication/Tdata/inst/python')
from tdata_py import contract
from tdata_py.spread import compute_spread_risk_reward
from tdata_py.contract import Stock, Option, IB
import pandas as pd

OUT_OI = r'C:/Users/aldoh/Documents/NewTrading/tsla_oi.json'
OUT_SPREADS = r'C:/Users/aldoh/Documents/NewTrading/tsla_spreads.csv'

S = 375.41
EXPIRIES = ['20260529', '20260618']  # 31 DTE, 51 DTE — both clean of earnings
RISK_BUDGET = 300.0  # USD per lot (full structure)
MAX_WIDTH = 10  # spread width <= 10 pts per user

# ---- Phase D.3 piece: pull OI for K from 320 to 460 around current spot, both expiries ----
ib = IB()
ib.connect('127.0.0.1', 7496, clientId=97)
chains = contract.getChains('TSLA', currency='USD')
all_strikes = chains[0][5]
strikes_near = [k for k in all_strikes if 320 <= k <= 460]
print(f'Strikes 320-460: {len(strikes_near)}')

oi_all = {}
for EXP in EXPIRIES:
    oi = {'C': {}, 'P': {}}
    for right in ['C', 'P']:
        for K in strikes_near:
            opt = Option('TSLA', EXP, K, right, 'SMART', tradingClass='TSLA', currency='USD')
            try:
                qual = ib.qualifyContracts(opt)
                if not qual:
                    continue
                tk = ib.reqMktData(qual[0], '101', False, False)
                ib.sleep(2)
                v = tk.callOpenInterest if right == 'C' else tk.putOpenInterest
                if v is not None and v == v:
                    oi[right][K] = int(v)
                ib.cancelMktData(qual[0])
            except Exception as e:
                print(f'OI err {EXP} {K}{right}: {e}')
    oi_all[EXP] = oi

oi = oi_all[EXPIRIES[0]]  # primary expiry for cap
with open(OUT_OI, 'w') as f:
    json.dump(oi_all, f, indent=2)

print('\n=== OI snapshot ===')
print('CALLS:')
for k in sorted(oi['C']):
    v = oi['C'][k]
    print(f'  K={k:>6.1f}  OI={v:>6}')
print('PUTS:')
for k in sorted(oi['P']):
    v = oi['P'][k]
    print(f'  K={k:>6.1f}  OI={v:>6}')

# Find OI cap (max-OI strike above spot for calls, below for puts)
cap_call = None; cap_call_oi = 0
for k, v in oi['C'].items():
    if k > S and v > cap_call_oi:
        cap_call = k; cap_call_oi = v
cap_put = None; cap_put_oi = 0
for k, v in oi['P'].items():
    if k < S and v > cap_put_oi:
        cap_put = k; cap_put_oi = v
print(f'\noi_cap_call: K={cap_call} OI={cap_call_oi}')
print(f'oi_cap_put:  K={cap_put}  OI={cap_put_oi}')

ib.disconnect()

# ---- Phase D.4 piece: run spread analyzer with force_refresh=True for both expiries ----
print('\n=== Spread enumeration (call DEBIT verticals, force_refresh=True) ===')
all_results = []
for EXP in EXPIRIES:
    for width in [5, 10]:
        df = compute_spread_risk_reward(
            sym='TSLA', trading_class='TSLA', expiration=EXP,
            current_price=S, moneyness_pct=0.20, spread_width=width, right='C',
            multiplier=100, currency='USD', exchangeSec='SMART', exchangeOpt='SMART',
            force_refresh=True,
        )
        if df is not None and not df.empty:
            df['width_pts'] = width
            df['expiry'] = EXP
            all_results.append(df)

if all_results:
    full = pd.concat(all_results, ignore_index=True)
    debit = full[(full['spread_type'] == 'DEBIT') & (full['max_risk'] <= RISK_BUDGET)].copy()
    debit = debit.sort_values(['reward_risk_ratio'], ascending=False)
    debit.to_csv(OUT_SPREADS, index=False)
    cols = ['expiry','width_pts','short_strike','long_strike','net_premium','max_risk','max_reward','reward_risk_ratio','prob_success_delta','prob_success_market','edge','expected_value']
    print(f'\nDEBIT call spreads with max_risk <= ${RISK_BUDGET} per lot, sorted by R:R:')
    print(debit[cols].head(25).to_string(index=False))
print('\nDONE')
