import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import matplotlib.dates as mdates

# Connect to database
db_path = r"C:\Users\aldoh\Documents\RApplication\data\mydb.db"
conn = sqlite3.connect(db_path)

# Query to get daily tick variations
query = """
WITH daily_data AS (
    SELECT
        date,
        chf_value,
        LAG(chf_value) OVER (ORDER BY date) AS prev_chf_value
    FROM ConvertToCHF
    WHERE currency = 'USD'
    ORDER BY date
),
tick_data AS (
    SELECT
        date,
        ROUND((chf_value - prev_chf_value) / 0.0001) AS ticks,
        SUBSTR(date, 1, 4) || '-' || SUBSTR(date, 5, 2) || '-' || SUBSTR(date, 7, 2) as formatted_date
    FROM daily_data
    WHERE prev_chf_value IS NOT NULL
)
SELECT
    formatted_date,
    ticks
FROM tick_data
ORDER BY date;
"""

# Execute query and create DataFrame
df = pd.read_sql_query(query, conn)
conn.close()

# Convert date strings to datetime objects
df['date'] = pd.to_datetime(df['formatted_date'])

# Create the plot
plt.figure(figsize=(16, 10))

# Plot the tick variations
plt.plot(df['date'], df['ticks'], linewidth=0.8, alpha=0.7, color='steelblue')

# Add horizontal lines for key levels
plt.axhline(y=0, color='black', linestyle='-', alpha=0.3, linewidth=1)
plt.axhline(y=160, color='red', linestyle='--', alpha=0.7, linewidth=2, label='$600 Loss Threshold (+160 ticks)')
plt.axhline(y=-160, color='green', linestyle='--', alpha=0.7, linewidth=2, label='$600 Gain Threshold (-160 ticks)')

# Highlight extreme moves
extreme_up = df[df['ticks'] >= 160]
extreme_down = df[df['ticks'] <= -160]

plt.scatter(extreme_up['date'], extreme_up['ticks'], color='red', s=50, alpha=0.8, zorder=5, label=f'Extreme CHF Weakness ({len(extreme_up)} days)')
plt.scatter(extreme_down['date'], extreme_down['ticks'], color='green', s=50, alpha=0.8, zorder=5, label=f'Extreme CHF Strength ({len(extreme_down)} days)')

# Formatting
plt.title('USD/CHF Daily Tick Variations (2021-2025)\n3-Contract Long CHF Position Impact', fontsize=16, pad=20)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Daily Tick Change', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(loc='upper right', fontsize=10)

# Format x-axis
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.gca().xaxis.set_minor_locator(mdates.MonthLocator((1, 7)))

# Rotate x-axis labels
plt.xticks(rotation=45)

# Add text annotations for context
plt.text(0.02, 0.98, 'Positive ticks = CHF Weakening = LOSS for CHF holders\nNegative ticks = CHF Strengthening = GAIN for CHF holders',
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.text(0.02, 0.02, f'Total observations: {len(df):,} trading days\nAverage daily move: {df["ticks"].abs().mean():.1f} ticks\nStandard deviation: {df["ticks"].std():.1f} ticks',
         transform=plt.gca().transAxes, fontsize=9, verticalalignment='bottom',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

# Adjust layout and save
plt.tight_layout()
plt.savefig(r'C:\Users\aldoh\Documents\NewTrading\usd_chf_tick_variations.png', dpi=300, bbox_inches='tight')
plt.show()

print("Graph saved as 'usd_chf_tick_variations.png'")
print(f"\nSummary Statistics:")
print(f"Total trading days: {len(df):,}")
print(f"CHF strengthening days (negative ticks): {len(df[df['ticks'] < 0]):,} ({100*len(df[df['ticks'] < 0])/len(df):.1f}%)")
print(f"CHF weakening days (positive ticks): {len(df[df['ticks'] > 0]):,} ({100*len(df[df['ticks'] > 0])/len(df):.1f}%)")
print(f"Days exceeding ±160 ticks: {len(df[abs(df['ticks']) >= 160]):,}")
print(f"Maximum CHF weakening: +{df['ticks'].max():,.0f} ticks")
print(f"Maximum CHF strengthening: {df['ticks'].min():,.0f} ticks")