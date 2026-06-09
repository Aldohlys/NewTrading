args <- commandArgs(trailingOnly = TRUE)
path <- args[1]
x <- readLines(path, warn = FALSE)
s <- paste(x, collapse = "")
# Find the Outright table — between its h3 and the next h3
mm <- regexpr("Outright .+? grid.+?</table>", s, perl = TRUE)
if (mm[1] < 0) { cat("no outright table\n"); quit(status = 0) }
m <- substr(s, mm[1], mm[1] + attr(mm, "match.length") - 1)
hdr <- regmatches(m, gregexpr("<th[^>]*>.+?</th>", m, perl = TRUE))[[1]]
hdr_txt <- gsub("<[^>]+>", "", hdr)
cat("HEADERS:", paste(hdr_txt, collapse = " | "), "\n\n")
rows <- regmatches(m, gregexpr("<tr[^>]*>.+?</tr>", m, perl = TRUE))[[1]]
for (r in rows) {
  cells <- regmatches(r, gregexpr("<td[^>]*>.+?</td>", r, perl = TRUE))[[1]]
  cells <- gsub("<[^>]+>", "", cells)
  cells <- gsub("&mdash;", "-", cells)
  cells <- gsub("&[a-z]+;", "", cells)
  cells <- trimws(cells)
  if (length(cells) > 0) cat(paste(cells, collapse = " | "), "\n")
}
