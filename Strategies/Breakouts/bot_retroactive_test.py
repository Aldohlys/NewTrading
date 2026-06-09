"""
BOT Retroactive Test
Applies the Setup/Breakout scoring to all historical BOT trades
to verify if the filter would have correctly passed winners and blocked losers.
"""

import yfinance as yf
import pandas as pd
import numpy as np
import sqlite3
from datetime import timedelta
import warnings
warnings.filterwarnings('ignore')

DB_PATH = r"C:\Users\aldoh\Documents\RApplication\data\mydb.db"

# ── Get all closed BOT trades with P&L ─────────────────────────────────
conn = sqlite3.connect(DB_PATH)

trades = pd.read_sql("""
    SELECT TradeNr, MIN(TradeDate) as EntryDate, Ssjacent as Symbol,
           SUM(PnL) as PnL,
           GROUP_CONCAT(DISTINCT Remarques) as Notes,
           SUM(CASE WHEN Right = 'P' THEN 1 ELSE 0 END) as put_count,
           SUM(CASE WHEN Right = 'C' THEN 1 ELSE 0 END) as call_count,
           MAX(CASE WHEN Instrument LIKE '%MCL%' OR Instrument LIKE '%GCM%' OR Instrument LIKE '%MSF%' THEN 1 ELSE 0 END) as is_futures
    FROM Trades
    WHERE Strategy = 'BOT' AND Statut LIKE 'Ferm%'
    GROUP BY TradeNr
    HAVING SUM(PnL) <> 0
""", conn)

# Get sector mapping
sectors = pd.read_sql("SELECT Symbol, Sector FROM ScannerUniverse WHERE IsActive = 1", conn)
sector_map = dict(zip(sectors.Symbol, sectors.Sector))
conn.close()

# Determine direction
trades['direction'] = np.where(trades.put_count > trades.call_count, 'short', 'long')
trades['is_winner'] = trades.PnL > 0
trades['sector'] = trades.Symbol.map(sector_map).fillna('Unknown')

# Convert date
trades['entry_str'] = trades.EntryDate.astype(str).apply(lambda x: f"{x[:4]}-{x[4:6]}-{x[6:8]}")

print(f"Total closed BOT trades with P&L: {len(trades)}")
print(f"Winners: {trades.is_winner.sum()}, Losers: {(~trades.is_winner).sum()}")
print(f"Excluding futures: {trades.is_futures.sum()} trades")

# Exclude futures and short trades (BOT long only)
trades = trades[(trades.is_futures == 0) & (trades.direction == 'long')].copy()
print(f"Long non-futures trades to test: {len(trades)}")

# ── Download price data and compute indicators ──────────────────────────
def compute_bot_score(symbol, entry_date):
    """Compute S/BK scores for a symbol at a given entry date."""
    start = (pd.Timestamp(entry_date) - timedelta(days=120)).strftime('%Y-%m-%d')
    end = (pd.Timestamp(entry_date) + timedelta(days=5)).strftime('%Y-%m-%d')

    try:
        df = yf.download(symbol, start=start, end=end, interval='1d', progress=False)
    except Exception:
        return None

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [c[0] if isinstance(c, tuple) else c for c in df.columns]
    df = df.reset_index()

    if len(df) < 55:
        return None

    # Find the entry date row (or closest before)
    df['Date'] = pd.to_datetime(df['Date'])
    entry_ts = pd.Timestamp(entry_date)
    entry_idx = df[df.Date <= entry_ts].index
    if len(entry_idx) == 0:
        return None
    i = entry_idx[-1]

    if i < 50:
        return None

    closes = df['Close'].values.astype(float)
    highs = df['High'].values.astype(float)
    lows = df['Low'].values.astype(float)
    volumes = df['Volume'].values.astype(float)
    price = closes[i]

    # MA50
    if i < 50:
        return None
    ma50 = np.mean(closes[i-49:i+1])
    ma50_prev5 = np.mean(closes[i-54:i-4])
    ma50_slope = (ma50 - ma50_prev5) / ma50_prev5 * 100 if ma50_prev5 > 0 else 0

    # RSI14
    deltas = np.diff(closes[i-14:i+1])
    gains = np.where(deltas > 0, deltas, 0)
    losses = np.where(deltas < 0, -deltas, 0)
    avg_gain = np.mean(gains) if len(gains) > 0 else 0
    avg_loss = np.mean(losses) if len(losses) > 0 else 0
    if avg_loss == 0:
        rsi = 100
    else:
        rs = avg_gain / avg_loss
        rsi = 100 - 100 / (1 + rs)

    # RSI slope (vs 5 bars ago) — simplified
    deltas_prev = np.diff(closes[i-19:i-4])
    gains_p = np.where(deltas_prev > 0, deltas_prev, 0)
    losses_p = np.where(deltas_prev < 0, -deltas_prev, 0)
    avg_gain_p = np.mean(gains_p) if len(gains_p) > 0 else 0
    avg_loss_p = np.mean(losses_p) if len(losses_p) > 0 else 0
    if avg_loss_p == 0:
        rsi_prev = 100
    else:
        rs_p = avg_gain_p / avg_loss_p
        rsi_prev = 100 - 100 / (1 + rs_p)
    rsi_slope = rsi - rsi_prev

    # OBV slope (20d)
    direction = np.sign(np.diff(closes[i-20:i+1]))
    obv = np.cumsum(direction * volumes[i-19:i+1])
    obv_slope = obv[-1] - obv[0]

    # Up/Down volume ratio (10d)
    up_mask = closes[i-9:i+1] >= closes[i-10:i]
    up_vol = np.sum(volumes[i-9:i+1][up_mask])
    dn_vol = np.sum(volumes[i-9:i+1][~up_mask])
    updn_ratio = up_vol / dn_vol if dn_vol > 0 else 2.0

    # RS vs sector (simplified: use 20d return, no ETF comparison = set to positive if >0)
    ret20 = (closes[i] - closes[i-20]) / closes[i-20] * 100 if i >= 20 else 0

    # Range position
    high20 = np.max(highs[i-19:i+1])
    low20 = np.min(lows[i-19:i+1])
    rng_pct = (price - low20) / (high20 - low20) * 100 if high20 != low20 else 50

    # Squeeze
    high40 = np.max(highs[i-39:i+1]) if i >= 40 else np.max(highs[:i+1])
    low40 = np.min(lows[i-39:i+1]) if i >= 40 else np.min(lows[:i+1])
    range_20 = high20 - low20
    range_40 = high40 - low40
    squeeze_ratio = range_20 / range_40 if range_40 > 0 else 1.0

    # Volume decline
    vol_20 = np.mean(volumes[i-19:i+1])
    vol_50 = np.mean(volumes[i-49:i+1]) if i >= 50 else np.mean(volumes[:i+1])
    vol_decline = vol_20 / vol_50 if vol_50 > 0 else 1.0

    # Volume surge
    vol_surge = volumes[i] / vol_20 if vol_20 > 0 else 1.0

    # ── SETUP (6 criteria) ──────────────────────────────────
    S1 = price > ma50
    S2 = ma50_slope > 0
    S3 = ret20 > 0  # simplified: no ETF comparison
    S4 = obv_slope > 0
    S5 = squeeze_ratio < 0.65
    S6 = vol_decline < 0.90

    # ── BREAKOUT (4 criteria) ───────────────────────────────
    BK1 = rsi > 50 and rsi_slope > 0
    BK2 = updn_ratio > 1.1
    BK3 = rng_pct >= 70
    BK4 = vol_surge >= 1.2

    setup = sum([S1, S2, S3, S4, S5, S6])
    breakout = sum([BK1, BK2, BK3, BK4])

    # Color classification
    if setup >= 5 and breakout >= 3:
        color = 'GREEN'
    elif (setup >= 5 and breakout >= 1) or (setup >= 4 and breakout >= 3):
        color = 'AMBER'
    else:
        color = 'GREY'

    return {
        'setup': setup,
        'breakout': breakout,
        'color': color,
        'squeeze': round(squeeze_ratio, 3),
        'vol_dec': round(vol_decline, 3),
        'vol_surge': round(vol_surge, 2),
        'rng_pct': round(rng_pct, 1),
        'rsi': round(rsi, 1),
        'ma50_dist': round((price - ma50) / ma50 * 100, 1),
        'flags': f"S1:{'+'if S1 else'-'} S2:{'+'if S2 else'-'} S3:{'+'if S3 else'-'} S4:{'+'if S4 else'-'} S5:{'+'if S5 else'-'} S6:{'+'if S6 else'-'} | BK1:{'+'if BK1 else'-'} BK2:{'+'if BK2 else'-'} BK3:{'+'if BK3 else'-'} BK4:{'+'if BK4 else'-'}"
    }


# ── Run test ────────────────────────────────────────────────────────────
print("\nComputing BOT scores for each historical trade...\n")

results = []
symbols_done = set()
symbol_cache = {}

for _, trade in trades.iterrows():
    sym = trade.Symbol
    entry = trade.entry_str

    score = compute_bot_score(sym, entry)

    if score is None:
        results.append({**trade.to_dict(), 'setup': None, 'breakout': None, 'color': 'NO DATA'})
        continue

    results.append({**trade.to_dict(), **score})

results_df = pd.DataFrame(results)

# ── Analysis ────────────────────────────────────────────────────────────
valid = results_df[results_df.color != 'NO DATA'].copy()
print(f"Trades with computed scores: {len(valid)} / {len(results_df)}")

print("\n" + "=" * 70)
print("RESULTS BY COLOR (would the filter have worked?)")
print("=" * 70)

for color in ['GREEN', 'AMBER', 'GREY']:
    subset = valid[valid.color == color]
    if len(subset) == 0:
        print(f"\n{color}: 0 trades")
        continue
    winners = subset[subset.is_winner]
    losers = subset[~subset.is_winner]
    total_pnl = subset.PnL.sum()
    avg_pnl = subset.PnL.mean()
    wr = len(winners) / len(subset) * 100

    print(f"\n{color}: {len(subset)} trades | WR: {wr:.0f}% | Total P&L: ${total_pnl:.0f} | Avg P&L: ${avg_pnl:.0f}")
    print(f"  Winners: {len(winners)} (avg ${winners.PnL.mean():.0f})" if len(winners) > 0 else "  Winners: 0")
    print(f"  Losers:  {len(losers)} (avg ${losers.PnL.mean():.0f})" if len(losers) > 0 else "  Losers: 0")

    for _, r in subset.sort_values('PnL', ascending=False).iterrows():
        marker = "W" if r.is_winner else "L"
        flags = r.get('flags', '')
        print(f"    [{marker}] {r.Symbol:6s} {r.entry_str} S:{r.setup:.0f} BK:{r.breakout:.0f} P&L=${r.PnL:+.0f} | {flags}")

print("\n" + "=" * 70)
print("FILTER EFFECTIVENESS")
print("=" * 70)

green = valid[valid.color == 'GREEN']
amber = valid[valid.color == 'AMBER']
grey = valid[valid.color == 'GREY']

# What would you have traded? GREEN + maybe AMBER
traded_green = green
traded_both = pd.concat([green, amber])

print(f"\nIf you only trade GREEN (S>=5 BK>=3):")
if len(traded_green) > 0:
    print(f"  Trades: {len(traded_green)}")
    print(f"  Win rate: {traded_green.is_winner.mean()*100:.0f}%")
    print(f"  Total P&L: ${traded_green.PnL.sum():.0f}")
    print(f"  Avg P&L: ${traded_green.PnL.mean():.0f}")
else:
    print("  No trades")

print(f"\nIf you trade GREEN + AMBER:")
if len(traded_both) > 0:
    print(f"  Trades: {len(traded_both)}")
    print(f"  Win rate: {traded_both.is_winner.mean()*100:.0f}%")
    print(f"  Total P&L: ${traded_both.PnL.sum():.0f}")
    print(f"  Avg P&L: ${traded_both.PnL.mean():.0f}")

print(f"\nGREY trades (would have been filtered out):")
if len(grey) > 0:
    print(f"  Trades: {len(grey)}")
    print(f"  Win rate: {grey.is_winner.mean()*100:.0f}%")
    print(f"  Total P&L: ${grey.PnL.sum():.0f}")
    print(f"  Avg P&L: ${grey.PnL.mean():.0f}")
    grey_winners = grey[grey.is_winner]
    if len(grey_winners) > 0:
        print(f"  MISSED winners (false negatives):")
        for _, r in grey_winners.sort_values('PnL', ascending=False).iterrows():
            print(f"    {r.Symbol:6s} {r.entry_str} S:{r.setup:.0f} BK:{r.breakout:.0f} P&L=${r.PnL:+.0f}")

print(f"\nComparison vs actual (all trades):")
print(f"  All trades: {len(valid)} trades, WR={valid.is_winner.mean()*100:.0f}%, P&L=${valid.PnL.sum():.0f}, Avg=${valid.PnL.mean():.0f}")

# Save results
results_df.to_csv(r"C:\Users\aldoh\Documents\NewTrading\bot_retroactive_results.csv", index=False)
print(f"\nResults saved to bot_retroactive_results.csv")
