#!/usr/bin/env bash
# Fetch the three OFL variable fonts the site uses, latin subset only.
#
# Google serves per-subset woff2 files. We want the LAST @font-face block in the
# CSS (the plain "latin" one), not the first (which is vietnamese). Getting this
# wrong yields a font with no Latin glyphs that silently falls back.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p public/fonts

UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36'

fetch() {
  local name="$1" css="$2" out="$3"
  # take the url from the block whose comment is exactly "latin"
  local url
  url=$(curl -s -A "$UA" "$css" \
        | awk '/\/\* latin \*\//{f=1} f && /url\(https:/{print; exit}' \
        | sed -E 's/.*url\((https:[^)]+)\).*/\1/')
  if [ -z "$url" ]; then
    echo "  $name: FAILED to find latin subset"
    return 1
  fi
  curl -sL "$url" -o "public/fonts/$out"
  local sz
  sz=$(stat -f%z "public/fonts/$out" 2>/dev/null || stat -c%s "public/fonts/$out")
  echo "  $name -> $out  ${sz} bytes"
  if [ "$sz" -lt 5000 ]; then
    echo "     WARNING: suspiciously small, check it loaded a real family"
  fi
}

echo "Fetching fonts (SIL OFL 1.1)…"
fetch "Big Shoulders Display" \
  "https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@100..900&display=swap" \
  "BigShouldersDisplay.woff2"
fetch "Newsreader" \
  "https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,200..800&display=swap" \
  "Newsreader.woff2"
fetch "Martian Mono" \
  "https://fonts.googleapis.com/css2?family=Martian+Mono:wght@300..700&display=swap" \
  "MartianMono.woff2"

echo
ls -la public/fonts/
