oldzip=$(find . -name "*(Version*.zip" -print0 | xargs -r -0 ls -1 -t | sort -n | head -1)
newzip=$(find . -name "*(Version*.zip" -print0 | xargs -r -0 ls -1 -t | sort -n | sed -n '2 p')

echo -e "Diffing\n  old: $oldzip\n  new: $newzip"

oldfile=$(mktemp)
newfile=$(mktemp)

unzip -p "$oldzip" main.tex > "$oldfile"
unzip -p "$newzip" main.tex > "$newfile"

latexdiff "$oldfile" "$newfile" > diff.tex

rm "$oldfile" "$newfile" "$oldzip" "$newzip"

echo "Done. Zips deleted. See diff.tex"
