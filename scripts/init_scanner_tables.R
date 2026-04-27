# init_scanner_tables.R — Create new DB tables for scanner v5
#
# Creates:
#   option_skew_history     — daily 25Δ skew per ticker, for Step C.2
#   option_chain_oi_history — daily per-strike OI snapshot, for Step D.3
#   scanner_rich_universe   — weekly rich-options gate state, for Step A.1
#
# Idempotent — safe to re-run.

suppressPackageStartupMessages({ library(DBI); library(RSQLite) })

DB_PATH <- "C:/Users/aldoh/Documents/RApplication/data/mydb.db"
con <- dbConnect(SQLite(), DB_PATH)

# ── option_skew_history ─────────────────────────────────────────────────────
# One row per ticker-date. Sources: gate3 vol_profile + 25Δ call/put IV from
# the option chain at the nearest monthly. Skew = call25_iv − put25_iv.
dbExecute(con, "
CREATE TABLE IF NOT EXISTS option_skew_history (
  cache_date   TEXT    NOT NULL,
  sym          TEXT    NOT NULL,
  iv30         REAL,
  iv90         REAL,
  iv180        REAL,
  rv30         REAL,
  call25_iv    REAL,
  put25_iv     REAL,
  skew_25d     REAL,
  PRIMARY KEY (cache_date, sym)
)")
dbExecute(con,
  "CREATE INDEX IF NOT EXISTS idx_skew_sym_date ON option_skew_history (sym, cache_date)")

# ── option_chain_oi_history ─────────────────────────────────────────────────
# One row per (ticker, expiry, strike, right, date). Step D.3 reads the 5-day
# median per strike for OI_Cap calculation (anti-noise convention N.2).
dbExecute(con, "
CREATE TABLE IF NOT EXISTS option_chain_oi_history (
  cache_date   TEXT    NOT NULL,
  sym          TEXT    NOT NULL,
  expiry       TEXT    NOT NULL,
  strike       REAL    NOT NULL,
  right        TEXT    NOT NULL,
  open_interest INTEGER,
  avg_volume    INTEGER,
  qualified     INTEGER NOT NULL DEFAULT 1,
  PRIMARY KEY (cache_date, sym, expiry, strike, right)
)")
dbExecute(con,
  "CREATE INDEX IF NOT EXISTS idx_oi_sym_expiry_date ON option_chain_oi_history (sym, expiry, cache_date)")

# ── scanner_rich_universe ───────────────────────────────────────────────────
# Weekly snapshot of rich-options gate state per ticker (Phase A).
dbExecute(con, "
CREATE TABLE IF NOT EXISTS scanner_rich_universe (
  cache_date          TEXT NOT NULL,
  sym                 TEXT NOT NULL,
  has_weekly          INTEGER NOT NULL,
  atm_bid_ask_pct     REAL,
  passes_gate         INTEGER NOT NULL,
  reason              TEXT,
  PRIMARY KEY (cache_date, sym)
)")

# ── scanner_results_v5 ──────────────────────────────────────────────────────
# Per-day master output of new scanner. Replaces the legacy scanner_results
# write path; legacy table preserved separately for transition.
dbExecute(con, "
CREATE TABLE IF NOT EXISTS scanner_results_v5 (
  cache_date          TEXT NOT NULL,
  sym                 TEXT NOT NULL,
  sector              TEXT,
  -- Phase B: Pull
  stage               TEXT,
  pull_score          INTEGER,
  pull_direction      TEXT,
  sector_rs_rank      INTEGER,
  -- Phase C: Cheap
  cheap_score         INTEGER,
  cheap_side          TEXT,
  ivp_2y              REAL,
  vrp                 REAL,
  -- Phase D: Setup / Chain / R:R
  vehicle             TEXT,
  strike              REAL,
  expiry              TEXT,
  spot_target_low     REAL,
  spot_target_high    REAL,
  targets_agreeing    INTEGER,
  fib_confirms        INTEGER,
  oi_cap_call         REAL,
  oi_cap_put          REAL,
  chain_state         TEXT,
  crowded_flag        INTEGER,
  effective_target    REAL,
  entry_floor         REAL,
  entry_ceiling       REAL,
  entry_state         TEXT,
  rr                  REAL,
  headroom_band       TEXT,
  -- Phase E: Classification
  rank                TEXT,
  phase_of_drop       TEXT,
  PRIMARY KEY (cache_date, sym)
)")

# Verify
tables <- dbListTables(con)
new_tables <- c("option_skew_history", "option_chain_oi_history",
                "scanner_rich_universe", "scanner_results_v5")
present <- new_tables %in% tables
cat("Created/verified tables:\n")
for (i in seq_along(new_tables)) {
  cat(sprintf("  %-30s %s\n", new_tables[i],
              ifelse(present[i], "OK", "MISSING")))
}

dbDisconnect(con)
cat("\nDone.\n")
