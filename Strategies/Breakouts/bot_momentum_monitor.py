"""
BOT Momentum Monitor
Checks open BOT trades for momentum loss signals.
Run daily after swing_scanner. Inserts alerts into DB Alerts table.

Signals:
  1. Directional efficiency < 50% (after day 5)
  2. Range contraction: ATR recent / ATR initial < 0.6
  3. Profit retracement: current profit < 40% of max profit achieved
  4. Volume dying: recent volume < 40% of breakout day volume
  5. Never in profit after 5 days

Usage:
  python bot_momentum_monitor.py          # check and insert alerts
  python bot_momentum_monitor.py --dry    # check only, no DB write
"""

import yfinance as yf
import pandas as pd
import numpy as np
import sqlite3
import sys
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

DB_PATH = r"C:\Users\aldoh\Documents\RApplication\data\mydb.db"
DRY_RUN = '--dry' in sys.argv

def get_open_bot_trades(conn):
    """Get open BOT trades from DB, grouped by underlying."""
    query = """
        SELECT Ssjacent, MIN(TradeDate) as entry_date,
               SUM(CASE WHEN Right = 'P' THEN 1 ELSE 0 END) as put_count,
               SUM(CASE WHEN Right = 'C' THEN 1 ELSE 0 END) as call_count,
               GROUP_CONCAT(DISTINCT Instrument) as instruments
        FROM Trades
        WHERE Strategy = 'BOT' AND Statut = 'Ouvert'
        AND Ssjacent NOT LIKE 'MSF%'
        GROUP BY Ssjacent
    """
    trades = pd.read_sql(query, conn)
    result = []
    for _, t in trades.iterrows():
        # Determine direction from option type
        if t.put_count > t.call_count:
            direction = 'short'
        else:
            direction = 'long'

        # Convert YYYYMMDD to date string
        dt = str(int(t.entry_date))
        entry_str = f"{dt[:4]}-{dt[4:6]}-{dt[6:8]}"

        result.append({
            'symbol': t.Ssjacent,
            'entry_date': entry_str,
            'direction': direction,
            'instruments': t.instruments
        })
    return result

def check_momentum(symbol, entry_date, direction):
    """Check momentum signals for a single trade."""
    # Fetch price data from entry date minus 5 days (for context)
    start = (pd.Timestamp(entry_date) - timedelta(days=7)).strftime('%Y-%m-%d')
    df = yf.download(symbol, start=start, interval='1d', progress=False)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [c[0] if isinstance(c, tuple) else c for c in df.columns]
    df = df.reset_index()

    # Filter to post-entry only
    df = df[df.Date >= entry_date].reset_index(drop=True)

    if len(df) < 3:
        return None  # not enough data

    entry_price = float(df.iloc[0]['Close'])
    current_price = float(df.iloc[-1]['Close'])
    total_days = len(df) - 1

    # 1. Directional efficiency
    if direction == 'long':
        up_days = int((df['Close'].diff() > 0).sum())
    else:
        up_days = int((df['Close'].diff() < 0).sum())
    dir_eff = up_days / total_days * 100 if total_days > 0 else 100

    # 2. Range contraction
    df['TR'] = np.maximum(
        df['High'] - df['Low'],
        np.maximum(
            abs(df['High'] - df['Close'].shift()),
            abs(df['Low'] - df['Close'].shift())
        )
    )
    window = min(5, max(3, len(df) // 2))
    atr_initial = float(df['TR'].iloc[1:window+1].mean())
    atr_recent = float(df['TR'].iloc[-window:].mean())
    range_ratio = atr_recent / atr_initial if atr_initial > 0 else 1.0

    # 3. Profit retracement
    if direction == 'long':
        max_favorable = float(df['High'].max())
        if max_favorable > entry_price:
            profit_retrace = (current_price - entry_price) / (max_favorable - entry_price) * 100
        else:
            profit_retrace = -100
    else:
        min_favorable = float(df['Low'].min())
        if min_favorable < entry_price:
            profit_retrace = (entry_price - current_price) / (entry_price - min_favorable) * 100
        else:
            profit_retrace = -100

    # 4. Volume decay
    vol_day1 = float(df['Volume'].iloc[0])
    vol_recent = float(df['Volume'].iloc[-window:].mean())
    vol_ratio = vol_recent / vol_day1 if vol_day1 > 0 else 1.0

    # 5. Price move
    if direction == 'long':
        move_pct = (current_price - entry_price) / entry_price * 100
    else:
        move_pct = (entry_price - current_price) / entry_price * 100

    # Determine alerts
    alerts = []
    if dir_eff < 50 and total_days >= 5:
        alerts.append(f"Directional efficiency low ({dir_eff:.0f}% of days in trade direction)")
    if range_ratio < 0.6 and total_days >= 5:
        alerts.append(f"Range contracting (recent ATR = {range_ratio:.0%} of initial)")
    if 0 < profit_retrace < 40:
        alerts.append(f"Profit retracing (keeping only {profit_retrace:.0f}% of max gain)")
    if profit_retrace <= -100 and total_days >= 5:
        alerts.append(f"Never been in profit after {total_days} days")
    if vol_ratio < 0.4 and total_days >= 5:
        alerts.append(f"Volume dying ({vol_ratio:.0%} of breakout day)")

    return {
        'symbol': symbol,
        'direction': direction,
        'entry_price': entry_price,
        'current_price': current_price,
        'move_pct': move_pct,
        'days': total_days,
        'dir_eff': dir_eff,
        'range_ratio': range_ratio,
        'profit_retrace': profit_retrace,
        'vol_ratio': vol_ratio,
        'alerts': alerts
    }

def insert_alert(conn, symbol, description):
    """Insert momentum alert into Alerts table if not already present today."""
    today = datetime.now().strftime('%Y-%m-%d')

    # Check if similar alert exists for today
    existing = pd.read_sql(
        f"SELECT id FROM Alerts WHERE Asset = ? AND AlertDate = ? AND Theme = 'Momentum'",
        conn, params=[symbol, today]
    )

    if len(existing) > 0:
        # Update existing
        conn.execute(
            "UPDATE Alerts SET Description = ?, CreatedAt = ? WHERE id = ?",
            [description, datetime.now().strftime('%Y-%m-%d %H:%M:%S'), int(existing.iloc[0]['id'])]
        )
    else:
        # Insert new
        conn.execute(
            "INSERT INTO Alerts (Theme, Asset, AlertDate, Description, Active, CreatedAt) VALUES (?, ?, ?, ?, 1, ?)",
            ['Momentum', symbol, today, description, datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
        )
    conn.commit()

def main():
    conn = sqlite3.connect(DB_PATH)
    trades = get_open_bot_trades(conn)

    if not trades:
        print("No open BOT trades found.")
        return

    print(f"Checking {len(trades)} open BOT trades...")
    print("=" * 70)

    any_alerts = False
    for trade in trades:
        result = check_momentum(trade['symbol'], trade['entry_date'], trade['direction'])
        if result is None:
            print(f"{trade['symbol']}: insufficient data")
            continue

        r = result
        status_icon = "OK" if not r['alerts'] else "ALERT"
        print(f"\n{r['symbol']} ({r['direction']}) | ${r['entry_price']:.2f} -> ${r['current_price']:.2f} ({r['move_pct']:+.1f}%) | {r['days']}d")
        print(f"  Dir eff: {r['dir_eff']:.0f}% | Range: {r['range_ratio']:.2f} | Profit retrace: {r['profit_retrace']:.0f}% | Vol: {r['vol_ratio']:.2f}x")

        if r['alerts']:
            any_alerts = True
            alert_text = " | ".join(r['alerts'])
            print(f"  >>> {status_icon}: {alert_text}")

            # Build alert description for DB
            desc = (
                f"BOT momentum alert for {r['symbol']} ({r['direction']}): "
                f"entry ${r['entry_price']:.2f}, current ${r['current_price']:.2f} ({r['move_pct']:+.1f}%), "
                f"{r['days']} days held. "
                f"Signals: {alert_text}. "
                f"Review position — consider closing if thesis no longer holds."
            )

            if not DRY_RUN:
                insert_alert(conn, r['symbol'], desc)
                print(f"  -> Alert inserted into DB")
            else:
                print(f"  -> [DRY RUN] Would insert alert")
        else:
            print(f"  >>> {status_icon}")

    if not any_alerts:
        print("\nAll trades OK — no momentum alerts.")

    print("\n" + "=" * 70)
    conn.close()

if __name__ == '__main__':
    main()
