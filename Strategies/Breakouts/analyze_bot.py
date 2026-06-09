import sqlite3
import pandas as pd
from datetime import datetime

conn = sqlite3.connect(r'C:/Users/aldoh/Documents/RApplication/data/mydb.db')

query = '''
SELECT TradeNr, Account, TradeDate, Instrument, Pos, Prix, "Comm.", Total,
      "Exp.Date", Risk, Reward, PnL, Statut, Currency, Remarques
FROM Trades
WHERE Strategy = 'BOT'
ORDER BY PnL DESC
'''

df = pd.read_sql_query(query, conn)
conn.close()

# Separate winners and losers (exclude breakeven)
winners = df[df['PnL'] > 0].copy()
losers = df[df['PnL'] < 0].copy()

print('='*80)
print('TOP 15 WINNING TRADES')
print('='*80)
for idx, row in winners.head(15).iterrows():
   print(f"Trade #{row['TradeNr']}: {row['Instrument']} | P&L: ${row['PnL']:,.2f} | Entry: ${row['Prix']}")
   print(f"  Date: {row['TradeDate']} -> Exp: {row['Exp.Date']} | Risk/Reward: {row['Risk']}/{row['Reward']}")
   if pd.notna(row['Remarques']) and str(row['Remarques']).strip():
       print(f"  Comment: {row['Remarques']}")
   print()

print('='*80)
print('TOP 15 LOSING TRADES')
print('='*80)
for idx, row in losers.tail(15).iterrows():
   print(f"Trade #{row['TradeNr']}: {row['Instrument']} | P&L: ${row['PnL']:,.2f} | Entry: ${row['Prix']}")
   print(f"  Date: {row['TradeDate']} -> Exp: {row['Exp.Date']} | Risk/Reward: {row['Risk']}/{row['Reward']}")
   if pd.notna(row['Remarques']) and str(row['Remarques']).strip():
       print(f"  Comment: {row['Remarques']}")
   print()
