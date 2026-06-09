args <- commandArgs(trailingOnly = TRUE)
path <- if (length(args) > 0) args[1] else "C:/Users/aldoh/Documents/NewTrading/Reports/analyze_UPS_20260512.html"
x <- readLines(path, warn = FALSE)
s <- paste(x, collapse = "")
mm <- regexpr("Vertical spreads.+?<table class=\"sortable\".+?</table>", s, perl = TRUE)
if (mm[1] < 0) { cat("no match for spreads block\n"); quit(status = 0) }
m <- substr(s, mm[1], mm[1] + attr(mm, "match.length") - 1)
hdr <- regmatches(m, gregexpr("<th[^>]*>.+?</th>", m, perl = TRUE))[[1]]
hdr_txt <- gsub("<[^>]+>", "", hdr)
cat("HEADERS:", paste(hdr_txt, collapse = " | "), "\n\n")
rows <- regmatches(m, gregexpr("<tr[^>]*>.+?</tr>", m, perl = TRUE))[[1]]
for (r in rows) {
  cells <- regmatches(r, gregexpr("<td[^>]*>.+?</td>", r))[[1]]
  cells <- gsub("<[^>]+>", "", cells)
  cells <- gsub("&mdash;", "-", cells)
  cells <- gsub("&[a-z]+;", "", cells)
  cells <- trimws(cells)
  if (length(cells) > 0) cat(paste(cells, collapse = " | "), "\n")
}
