#! /bin/bash

INPUT_FILE=nutrition-info.ods
OUT_PREFIX=".tmp-out"

if command -v ssconvert >/dev/null; then
	#nothing
	echo -n
else
	echo "ssconvert not found, please install Gnumeric."
	exit 1
fi

ssconvert --import-type=Gnumeric_OpenCalc:openoffice --export-file-per-sheet --export-type=Gnumeric_stf:stf_csv "${INPUT_FILE}" "$OUT_PREFIX"

mv ${OUT_PREFIX}.0 foods.csv
mv ${OUT_PREFIX}.1 servings.csv
mv ${OUT_PREFIX}.2 attributes.csv
mv ${OUT_PREFIX}.3 recipes.csv
mv ${OUT_PREFIX}.4 ingredients.csv
