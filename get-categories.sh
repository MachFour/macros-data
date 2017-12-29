#! /bin/bash

FOOD_CSV=${1:-/home/max/devel/macros/macros-data/foods.csv}

awk -v FPAT='([^,]*)|("[^"]+")' ' { print $8 }' "$FOOD_CSV" | sort | uniq | tr -d '"' | grep -v category
