import csv
from csv_mappings import *
import itertools

#def export_csv(items, columns, csv_path):
#	with open(csv_path, 'wt') as csv_file:
#		csv_writer = csv.DictWriter(csv_file, columns, dialect='excel')
#		csv_writer.writeheader()
#		for i in items.values():
#			csv_writer.writerow(i.data)

def csv_str(x): 
    if type(x) == str:
        return f'"{x}"' if x != "" else ""
    elif type(x) == float:
        return str(x)
    elif x is None:
        return ""
    else:
        raise TypeError(f"Unknown type for csv value: {x}")

def process_csv(path, mappings):
    output_csv = []
    with open(path, 'rt') as f:
        reader = csv.DictReader(f, dialect='excel')
        # input csv column names where mapping function is not None
        in_cols = list((i[0] for i in mappings.items() if i[1][1] != None))
        for row in reader:
            output_row = {}
            for col in in_cols:
                # one input CSV column can map to multiple output columns
                mapping_func = mappings[col][1]
                output_cols = mappings[col][0]
                output_data = mapping_func(row[col])
                for (c, d) in zip(output_cols, output_data):
                    output_row[c] = d
            output_csv.append(output_row)
        return output_csv


def print_csv(csv, limit=0):
    if len(csv) > 0:
        header = csv[0].keys()
        print(",".join(header))

    n = 0
    for row in csv:
        print(",".join(csv_str(x) for x in row.values()))
        n += 1
        if n == limit:
            break

def fix_nutrition_details_header(csv_file_in: str, csv_file_out: str):
    with open(csv_file_in, 'rt') as csv_orig:
        reader = csv.reader(csv_orig, dialect='excel')
        row_1 = next(reader) # header titles, some blank
        row_2 = next(reader) # units

        fixed_header_row = []
        last_column = ""
        for column, unit in zip(row_1, row_2):
            if len(column) > 0:
                last_column = column
                column_str = column
            else:
                column_str = last_column
            unit_str = f" ({unit})" if len(unit) > 0 else ""

            fixed_header_row.append(column_str + unit_str)

        with open(csv_file_out, 'wt') as csv_fixed:
            writer = csv.writer(csv_fixed, dialect='excel')
            writer.writerow(fixed_header_row)
            # write remaining rows the same
            writer.writerows((row for row in reader))



def get_food_details(csv_filename: str):
    processed_csv = process_csv(csv_filename, food_details_mappings)
    # add extra columns
    extra_data = {
            "food_type": "nuttab",
            "brand": None,
            "category": "uncategorised"
    }
    for row in processed_csv:
        row.update(extra_data)

    return processed_csv

# need to use the csv after modifying by fix_nutrition_details_header
def get_nutrition_details(csv_filename: str):
    processed_csv = process_csv(csv_filename, nutrition_mappings)

    # add extra columns
    extra_data = {
            "quantity": 100.0,
            "quantity_unit": None, # change to g or ml as appropriate
            "energy_unit": "kj",
            "salt": None
    }
    for row in processed_csv:
        row.update(extra_data)
        # correct sugar alcohol
        row["sugar_alcohol"] -= row["carbohydrate"]

    return processed_csv

# returns (unordered) set of NUTTAB IDs of liquid foods
def get_liquid_foods(liquids_csv: str):
    with open(liquids_csv, 'rt') as f:
        reader = csv.DictReader(f, dialect='excel')
        return set(row['Public Food Key'] for row in reader)

def get_servings(csv_filename: str):
    processed_csv = process_csv(csv_filename, serving_mappings)

    return processed_csv


def main():
    # files
    liquids_csv = 'liquids-per100ml.csv'
    food_csv = 'food-details.csv'
    nutrition_csv_orig = 'foods-per100g-liquids-per100ml.csv'
    # after header mod
    nutrition_csv_fixed = 'food-nutrients-fixed.csv'

    servings_csv = 'measures.csv'


    # fix up nutrition details header
    fix_nutrition_details_header(nutrition_csv_orig, nutrition_csv_fixed)

    # get liquid foods
    liquid_foods = get_liquid_foods(liquids_csv)
    # get nutrition details
    nut_details_out_csv = get_nutrition_details(nutrition_csv_fixed)
    # get food details
    food_details_out_csv = get_food_details(food_csv)

    servings_out_csv = get_servings(servings_csv)
    
    # combine food details with nutrition details, adding values for
    # extra columns energy unit column
    
    food_details_by_index = {}
    for row in food_details_out_csv:
        index = row["nuttab_index"]
        food_details_by_index[index] = row

    #serving_details_by_index = {}
    #for row in servings_out_csv:
    #    index = row["NUTTAB index"]
    #    serving_details_by_index[index] = row

    nut_details_by_index = {}
    for row in nut_details_out_csv:
        index = row["nuttab_index"]
        nut_details_by_index[index] = row

    combined_csv = []
    for index, food_details in food_details_by_index.items():
        nut_details = nut_details_by_index[index]
        if index in liquid_foods:
            nut_details["quantity_unit"] = "ml"
        else:
            nut_details["quantity_unit"] = "g"
        combined_row = {}
        combined_row.update(food_details)
        combined_row.update(nut_details)
        combined_csv.append(combined_row)

    print_csv(combined_csv)

    print("\n\n\n\nSERVINGS\n")
    
    print_csv(servings_out_csv)

if __name__ == "__main__":
    main()
