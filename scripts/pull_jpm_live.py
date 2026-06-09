"""Pull live JPM snapshot: spot, vol metrics, May 15 330/340 spread + nearby strikes."""
import sys, json
sys.path.insert(0, r'C:/Users/aldoh/Documents/RApplication/Tdata/inst/python')
from tdata_py import contract, impliedvol

OUT = r'C:/Users/aldoh/Documents/NewTrading/jpm_live_20260424.json'
out = {}

# Live spot via stock quote
try:
    spot_df = contract.getValue(['JPM'], currency='USD')
    print('SPOT:', spot_df.to_dict('records'))
    out['spot'] = spot_df.to_dict('records')
except Exception as e:
    print('stock err:', e)
    out['spot_err'] = str(e)

# Vol metrics (1Y lookback)
try:
    vm = impliedvol.get_volatility_metrics('JPM', lookback_days=252, hist=True, price=True)
    print('VOLMETRICS:', vm)
    out['vol_metrics'] = vm
except Exception as e:
    print('volmetrics err:', e)
    out['volmetrics_err'] = str(e)

# May 15 call strikes around the spread
expiries_strikes = {
    '20260515': [315, 320, 325, 330, 335, 340, 345],
}

for exp, strikes in expiries_strikes.items():
    out[exp] = {}
    for right in ['C']:
        try:
            df = contract.getOptValue('JPM', exp, strikes, right, currency='USD')
            rows = {}
            for _, r in df.iterrows():
                k = float(r.get('strike'))
                def f(v):
                    try:
                        fv = float(v)
                        if fv != fv:
                            return None
                        return fv
                    except Exception:
                        return None
                rows[str(k)] = {
                    'iv': f(r.get('iv')),
                    'delta': f(r.get('delta')),
                    'bid': f(r.get('bid')),
                    'ask': f(r.get('ask')),
                    'mkt_price': f(r.get('mkt_price')),
                    'last': f(r.get('last')),
                }
            out[exp][right] = rows
            print(f'OK {exp} {right} n={len(rows)}')
        except Exception as e:
            print(f'ERR {exp} {right}: {e}')
            out[exp][f'{right}_err'] = str(e)

with open(OUT, 'w') as f:
    json.dump(out, f, indent=2, default=str)
print('SAVED', OUT)
