#! /bin/bash


if ! command -v ssconvert >/dev/null; then
	echo "ssconvert not found, please install Gnumeric."
	exit 1
fi

function xlsx_to_csv() {
	local INPUT_FILE="$1"
	local OUT_NAME="$2"
	local NUM_SHEETS=$3

	ssconvert --import-type=Gnumeric_Excel:xlsx --export-file-per-sheet --export-type=Gnumeric_stf:stf_csv "${INPUT_FILE}" "$OUT_NAME"

	#for i in $(seq 0 $NUM_SHEETS); do
	#	mv "${OUT_PREFIX}.${i}" foods.csv
	#done
}

declare -a FILES
declare -a NAMES

FILES=(
	'Release 1 - Food details file.xlsx'
	'Release 1 - Food nutrient database.xlsx'
	'Release 1 - Measures file.xlsx'
	'Release 1 - Recipe file.xlsx'
)

NAMES=(
	'food-details'
	'food-nutrients'
	'measures'
	'recipes'
)

for n in seq 1 4; do
	xlsx_to_csv "${FILES[n]}" "${NAMES[n]}"
done



# afterwards -
# renaming files
# delete second line with units
