"""Pull live OESX (ESTX50) put quotes from TWS for hedge-roll decision."""
import sys, json
sys.path.insert(0, r'C:/Users/aldoh/Documents/RApplication/Tdata/inst/python')
from tdata_py import contract

jobs = {
    '20260918': [4700, 4800, 5000, 5200, 5400, 5500, 5600, 5700],
    '20261218': [4800, 4900, 5000, 5500, 5600, 5700],
}

out = {}
for exp, strikes in jobs.items():
    print(f'=== FETCH {exp} P strikes={strikes} ===', flush=True)
    try:
        df = contract.getOptValue('ESTX50', exp, strikes, 'P',
                                  currency='EUR', force_refresh=True)
        def f(v):
            try:
                fv = float(v)
                return None if fv != fv else round(fv, 4)
            except Exception:
                return None
        for _, r in df.iterrows():
            k = f(r.get('strike'))
            bid, ask = f(r.get('bid')), f(r.get('ask'))
            mid = round((bid + ask) / 2, 2) if bid and ask else None
            rec = {'bid': bid, 'ask': ask, 'mid': mid,
                   'iv': f(r.get('iv')), 'delta': f(r.get('delta'))}
            out.setdefault(exp, {})[str(k)] = rec
            print(f'  {exp} {k:>6}P  bid={bid}  ask={ask}  mid={mid}  '
                  f'iv={rec["iv"]}  delta={rec["delta"]}', flush=True)
    except Exception as e:
        print(f'  ERR {exp}: {e}', flush=True)

json.dump(out, open(r'C:/Users/aldoh/Documents/NewTrading/oesx_quotes.json', 'w'), indent=2)
print('DONE', flush=True)
