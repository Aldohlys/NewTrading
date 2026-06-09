"""Pull SMH vol surface from TWS — per-expiry, per-right, with incremental save."""
import sys, json, os
sys.path.insert(0, r'C:/Users/aldoh/Documents/RApplication/Tdata/inst/python')
from tdata_py import contract

OUT = r'C:/Users/aldoh/Documents/NewTrading/smh_vol_surface.json'
LOG = r'C:/Users/aldoh/Documents/NewTrading/smh_surface.log'

def log(msg):
    with open(LOG, 'a') as f:
        f.write(msg + '\n')
    print(msg, flush=True)

expiries_strikes = {
    '20260501': [480, 485, 490, 495, 497.5, 500, 505, 510, 515, 520],
    '20260522': [450, 460, 470, 480, 490, 497.5, 505, 515, 525, 535, 545],
    '20260618': [430, 445, 460, 475, 490, 497.5, 510, 525, 540, 555, 570],
    '20260821': [400, 420, 440, 460, 480, 497.5, 515, 535, 560, 585, 610, 640],
}

out = {}
if os.path.exists(OUT):
    try:
        out = json.load(open(OUT))
    except Exception:
        out = {}

for exp, strikes in expiries_strikes.items():
    if exp not in out:
        out[exp] = {}
    for right in ['C', 'P']:
        if right in out[exp] and len(out[exp][right]) >= len(strikes):
            log(f'SKIP {exp} {right} (cached)')
            continue
        log(f'FETCH {exp} {right} strikes={strikes}')
        try:
            df = contract.getOptValue('SMH', exp, strikes, right, currency='USD')
            rows = {}
            for _, r in df.iterrows():
                k = float(r.get('strike'))
                def f(v):
                    try:
                        fv = float(v)
                        if fv != fv:  # NaN
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
                }
            out[exp][right] = rows
            with open(OUT, 'w') as f:
                json.dump(out, f, indent=2)
            log(f'SAVED {exp} {right} n={len(rows)}')
        except Exception as e:
            log(f'ERR {exp} {right}: {e}')

log('DONE')
