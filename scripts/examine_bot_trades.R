library(Tdata); library(DBI)
conn <- safe_db_connect()

cat("=== BOT TRADES OVERVIEW ===\n")
n <- dbGetQuery(conn, "SELECT COUNT(*) as n FROM Trades WHERE Strategy = 'BOT'")
cat("Total BOT trades:", n$n, "\n\n")

cat("Columns:\n")
cat(paste(dbListFields(conn, "Trades"), collapse=", "), "\n\n")

cat("Date range:\n")
print(dbGetQuery(conn, "SELECT MIN(TradeDate) as earliest, MAX(TradeDate) as latest FROM Trades WHERE Strategy = 'BOT'"))

cat("\nStatus distribution:\n")
print(dbGetQuery(conn, "SELECT Statut, COUNT(*) as n, ROUND(AVG(PnL),2) as avg_pnl, ROUND(SUM(PnL),2) as total_pnl FROM Trades WHERE Strategy = 'BOT' GROUP BY Statut"))

cat("\nInstruments traded:\n")
inst <- dbGetQuery(conn, "SELECT Instrument, COUNT(*) as n, ROUND(AVG(PnL),2) as avg_pnl FROM Trades WHERE Strategy = 'BOT' GROUP BY Instrument ORDER BY n DESC LIMIT 15")
print(inst)

cat("\nSample winning trades (with remarks):\n")
winners <- dbGetQuery(conn, "SELECT TradeNr, TradeDate, Instrument, Pos, Prix, PnL, Remarques FROM Trades WHERE Strategy = 'BOT' AND PnL > 0 ORDER BY PnL DESC LIMIT 10")
print(winners)

cat("\nSample losing trades:\n")
losers <- dbGetQuery(conn, "SELECT TradeNr, TradeDate, Instrument, Pos, Prix, PnL, Remarques FROM Trades WHERE Strategy = 'BOT' AND PnL < 0 ORDER BY PnL ASC LIMIT 10")
print(losers)

# Check if we have Exp.Date for duration calculation
cat("\nExpiry/close dates:\n")
dates <- dbGetQuery(conn, "SELECT TradeDate, [Exp.Date] as ExpDate, Instrument, PnL FROM Trades WHERE Strategy = 'BOT' AND [Exp.Date] IS NOT NULL AND [Exp.Date] != '' LIMIT 10")
print(dates)

dbDisconnect(conn)
