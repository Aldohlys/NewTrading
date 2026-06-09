library(Tdata); library(DBI)
conn <- safe_db_connect()

# Get all BOT trades with dates and P&L
bot <- dbGetQuery(conn, "SELECT TradeNr, TradeDate, Instrument, Pos, Prix, PnL, Statut,
  [Exp.Date] as ExpDate FROM Trades WHERE Strategy = 'BOT' AND TradeDate IS NOT NULL")
cat("BOT trades:", nrow(bot), "\n")
cat("Date range:", min(bot$TradeDate), "to", max(bot$TradeDate), "\n\n")

# Parse trade dates
bot$trade_date <- as.Date(bot$TradeDate, format = "%Y%m%d")

# Extract underlying symbol from instrument
bot$sym <- gsub("\\s.*", "", bot$Instrument)

# Win/loss classification
bot$win <- bot$PnL > 0
cat("Wins:", sum(bot$win), "Losses:", sum(!bot$win), "\n")
cat("Win rate:", round(mean(bot$win) * 100, 1), "%\n\n")

# Check macro cache date range
macro_range <- dbGetQuery(conn, "SELECT MIN(cache_date) as earliest, MAX(cache_date) as latest FROM macro_context_cache")
cat("Macro cache range:", macro_range$earliest, "to", macro_range$latest, "\n")

# Check price cache date range
price_range <- dbGetQuery(conn, "SELECT MIN(cache_date) as earliest, MAX(cache_date) as latest FROM mrbreakouts_cache")
cat("Scanner cache range:", price_range$earliest, "to", price_range$latest, "\n\n")

# How many BOT trades fall within our cached data?
bot_in_range <- bot[bot$trade_date >= as.Date("2025-06-01"), ]
cat("BOT trades since 2025-06:", nrow(bot_in_range), "\n")
cat("Wins:", sum(bot_in_range$win), "Losses:", sum(!bot_in_range$win), "\n\n")

# Check Yahoo historical data availability (we fetch 300 days in scanner)
# VIX history from Yahoo goes back further
cat("=== For backtest we need: ===\n")
cat("1. VIX, rates, DXY, breadth proxies for each trade date\n")
cat("2. Sector ETF prices around each trade date\n")
cat("3. Stock prices around each trade date\n\n")

# Check what symbols we have in cache
cached_syms <- dbGetQuery(conn, "SELECT DISTINCT ticker FROM mrbreakouts_cache")
cat("Cached symbols:", nrow(cached_syms), "\n")

# Check overlap with BOT symbols
bot_syms <- unique(bot$sym)
cat("BOT underlying symbols:", length(bot_syms), "\n")
overlap <- intersect(bot_syms, cached_syms$ticker)
cat("In cache:", length(overlap), "->", paste(overlap, collapse=", "), "\n")
missing <- setdiff(bot_syms, cached_syms$ticker)
cat("NOT in cache:", length(missing), "->", paste(missing, collapse=", "), "\n\n")

# Trade duration distribution
bot$exp_date <- as.Date(bot$ExpDate, format = "%d.%m.%Y")
bot$duration <- as.integer(bot$exp_date - bot$trade_date)
valid_dur <- bot$duration[!is.na(bot$duration) & bot$duration > 0 & bot$duration < 365]
cat("Trade duration (days):\n")
cat("  Median:", median(valid_dur), "\n")
cat("  Mean:", round(mean(valid_dur), 1), "\n")
cat("  25th:", quantile(valid_dur, 0.25), "\n")
cat("  75th:", quantile(valid_dur, 0.75), "\n")

dbDisconnect(conn)
