#! /bin/bash

TABLE=./all-foods-per-100g.txt

index=$1

grep $index "$TABLE" | awk -F \" '{ print $6, $10, $8}' | grep -v -E '%|\sug\s|C[0-9]' | sort | \
	grep -F \
"Available carbohydrate, with sugar alcohols
Calcium
Dietary fibre
Energy, including dietary fibre
Fat
Iron
Moisture
Protein
Potassium
Sodium (Na)
Starch
Total saturated fatty acids (g)
Total sugars"

