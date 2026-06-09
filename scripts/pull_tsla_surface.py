"""Pull TSLA vol surface — v3: known-good expiries from chain discovery."""
import sys, json, os
sys.path.insert(0, r'C:/Users/aldoh/Documents/RApplication/Tdata/inst/python')
from tdata_py import contract

OUT = r'C:/Users/aldoh/Documents/NewTrading/tsla_vol_surface.json'
LOG = r'C:/Users/aldoh/Documents/NewTrading/tsla_surface.log'

def log(msg):
    with open(LOG, 'a') as f:
        f.write(msg + '\n')
    print(msg, flush=True)

# Confirmed valid expiries from getChains:
# 20260506 (8d), 20260529 (31d), 20260618 (51d), 20260821 (115d)
CHOSEN = ['20260506', '20260529', '20260618', '20260821']

# Spot ~375. Strikes from confirmed grid (2.5 increments below 510)
STRIKES = [325, 335, 345, 355, 365, 370, 372.5, 375, 377.5, 380, 385, 395, 405, 415, 425]

out = {}
if os.path.exists(OUT):
    try:
        out = json.load(open(OUT))
    except Exception:
        out = {}

for exp in CHOSEN:
    if exp not in out:
        out[exp] = {}
    for right in ['C', 'P']:
        if right in out[exp] and len(out[exp][right]) >= 8:
            log(f'SKIP {exp} {right} (cached n={len(out[exp][right])})')
            continue
        log(f'FETCH {exp} {right}')
        try:
            df = contract.getOptValue('TSLA', exp, STRIKES, right, currency='USD')
            if df is None:
                log(f'NULL df {exp} {right}'); continue
            rows = {}
            for _, r in df.iterrows():
                k = float(r.get('strike'))
                def f(v):
                    try:
                        fv = float(v)
                        if fv != fv: return None
                        return fv
                    except Exception:
                        return None
                rows[str(k)] = {
                    'iv': f(r.get('iv')),
                    'delta': f(r.get('delta')),
                    'bid': f(r.get('bid')),
                    'ask': f(r.get('ask')),
                    'mkt_price': f(r.get('mkt_price')),
                    'volume': f(r.get('volume')),
                    'open_interest': f(r.get('open_interest')) or f(r.get('openInterest')),
                }
            out[exp][right] = rows
            with open(OUT, 'w') as f:
                json.dump(out, f, indent=2)
            log(f'SAVED {exp} {right} n={len(rows)}')
        except Exception as e:
            log(f'ERR {exp} {right}: {e}')

log('DONE')
