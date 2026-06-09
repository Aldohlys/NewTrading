library(Tdata); library(DBI)
conn <- safe_db_connect()
new_tickers <- data.frame(
  Symbol = c("HYG", "LQD", "CPER", "GLD"),
  Sector = rep("Macro", 4),
  Role = rep("macro", 4),
  IsActive = rep(1L, 4),
  Notes = c("Credit: HY bonds", "Credit: IG bonds", "Copper proxy (risk appetite)", "Gold ETF (safe haven)"),
  stringsAsFactors = FALSE
)
existing <- dbGetQuery(conn, "SELECT Symbol FROM ScannerUniverse WHERE Symbol IN ('HYG','LQD','CPER','GLD')")
to_add <- new_tickers[!(new_tickers$Symbol %in% existing$Symbol), ]
if (nrow(to_add) > 0) {
  dbWriteTable(conn, "ScannerUniverse", to_add, append = TRUE)
  cat("Added:", paste(to_add$Symbol, collapse = ", "), "\n")
} else {
  cat("All tickers already exist\n")
}
cat("\nMacro tickers now:\n")
print(dbGetQuery(conn, "SELECT Symbol, Notes FROM ScannerUniverse WHERE Role = 'macro'"))
dbDisconnect(conn)
