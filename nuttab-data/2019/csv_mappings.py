from typing import Callable

# Mapping data structure (dict)
# key: Source csv name (string)
# value: ((Dest csv name1, name2), mapping fn: string -> (tuple of strings)}



copy = lambda x: (x,)
numeric = lambda x: (float(x) if x != '' else None,)
numeric_zero_null = lambda x: (float(x) if x != '0' else None,)


CsvMappings = dict[str, tuple[tuple[str, ...], Callable[[str], tuple[str, ...]]]]


# returns tuple of (name, variety, extra_desc)
# from NUTTAB Food Name
def process_name(food_name: str) -> tuple[str, str, str]:
    split = food_name.split(",", maxsplit=2)
    if len(split) == 1:
        name = food_name.lower().strip()
        variety = ""
        extra_desc = ""
    else:
        name = split[0].lower().strip()
        variety = split[1].strip()
        extra_desc = split[2].strip() if len(split) > 2 else ""

    return (name, variety, extra_desc)

food_details_mappings: CsvMappings = {
    "Public Food Key": (("NUTTAB index",), copy), 
    "Food Profile ID": ((), None), 
    "Derivation": (("data_source",), copy), 
    #"Name": ((), None), 
    "Name": (("name", "variety", "extra_desc"), process_name), 
    "Description": (("notes",), copy), 
    "Scientific Name": ((), None), 
    "Sampling details": (("data_notes",), copy), 
    "Nitrogen Factor": ((), None), 
    "Fat Factor": ((), None), 
    "Specific Gravity": (("density",), numeric_zero_null), 
    "Analysed portion": ((), None), 
    "Unanalysed portion": ((), None), 
    "Classification ID": ((), None), 
    "Classification Name": ((), None),
}

serving_mappings: CsvMappings = {
    "Public Food Key": (("NUTTAB index",), copy),
    "Measure description 1": (("name",), copy),
    "Quantity": (("quantity", ), numeric),
    "Quantity Unit": (("quantity_unit",), copy),
    "Measure derivation description": (("notes",), copy)
}


nutrition_mappings: CsvMappings = {
    "Public Food Key": (("NUTTAB index",), copy), 
    "Classification": ((), None), 
    #"Food Name": (("name", "variety", "extra_desc"), process_name), 
    "Food Name": ((), None),
    "Energy, with dietary fibre (kJ)": (("energy",), numeric), 
    "Energy, without dietary fibre (kJ)": ((), None), 
    "Moisture (water) (g)": (("water",), numeric), 
    "Protein (g)": (("protein",), numeric), 
    "Nitrogen (g)": ((), None), 
    "Total fat (g)": (("fat",), numeric), 
    "Ash (g)": ((), None), 
    "Total dietary fibre (g)": (("fibre",), numeric), 
    "Alcohol (g)": (("alcohol",), None), 
    "Fructose (g)": ((), None), 
    "Glucose (g)": ((), None), 
    "Sucrose (g)": ((), None), 
    "Maltose (g)": ((), None), 
    "Lactose (g)": ((), None), 
    "Galactose (g)": ((), None), 
    "Maltotriose (g)": ((), None), 
    "Total sugars (g)": (("sugar",), numeric), 
    "Added sugars (g)": ((), None), 
    "Free sugars (g)": ((), None), 
    "Starch (g)": (("starch",), numeric), 
    "Dextrin (g)": ((), None), 
    "Glycerol (g)": ((), None), 
    "Glycogen (g)": ((), None), 
    "Inulin (g)": ((), None), 
    "Mannitol (g)": ((), None), 
    "Maltodextrin (g)": ((), None), 
    "Oligosaccharides (g)": ((), None), 
    "Raffinose (g)": ((), None), 
    "Stachyose (g)": ((), None), 
    "Sorbitol (g)": ((), None), 
    "Resistant starch (g)": ((), None), 
    "Available carbohydrate, without sugar alcohols (g)": (("carbohydrate",), numeric), 
    "Available carbohydrate, with sugar alcohols (g)": (("sugar_alcohol",), numeric), 
    "Acetic acid (g)": ((), None), 
    "Citric acid (g)": ((), None), 
    "Fumaric acid (g)": ((), None), 
    "Lactic acid (g)": ((), None), 
    "Malic acid (g)": ((), None), 
    "Oxalic acid (g)": ((), None), 
    "Propionic acid (g)": ((), None), 
    "Quinic acid (g)": ((), None), 
    "Succinic acid (g)": ((), None), 
    "Tartaric acid (g)": ((), None), 
    "Aluminium (Al) (ug)": ((), None), 
    "Antimony (Sb) (ug)": ((), None), 
    "Arsenic (As) (ug)": ((), None), 
    "Cadmium (Cd) (mg)": ((), None), 
    "Calcium (Ca) (ug)": (("calcium",), None), 
    "Chromium (Cr) (ug)": ((), None), 
    "Chloride (Cl) (mg)": ((), None), 
    "Cobalt (Co) (ug)": ((), None), 
    "Copper (Cu) (mg)": ((), None), 
    "Fluoride (F) (ug)": ((), None), 
    "Iodine (I) (ug)": ((), None), 
    "Iron (Fe) (mg)": (("iron",), None), 
    "Lead (Pb) (ug)": ((), None), 
    "Magnesium (Mg) (mg)": ((), None), 
    "Manganese (Mn) (mg)": ((), None), 
    "Mercury (Hg) (ug)": ((), None), 
    "Molybdenum (Mo) (ug)": ((), None), 
    "Nickel (Ni) (ug)": ((), None), 
    "Phosphorus (P) (mg)": ((), None), 
    "Potassium (K) (mg)": (("potassium",), None), 
    "Selenium (Se) (ug)": ((), None), 
    "Sodium (Na) (mg)": (("sodium",), None), 
    "Sulphur (S) (mg)": ((), None), 
    "Tin (Sn) (ug)": ((), None), 
    "Zinc (Zn) (mg)": ((), None), 
    "Retinol (preformed vitamin A) (ug)": ((), None), 
    "Alpha-carotene (ug)": ((), None), 
    "Beta-carotene (ug)": ((), None), 
    "Cryptoxanthin (ug)": ((), None), 
    "Beta-carotene equivalents (provitamin A) (ug)": ((), None), 
    "Vitamin A retinol equivalents (ug)": ((), None), 
    "Lutein (ug)": ((), None), 
    "Lycopene (ug)": ((), None), 
    "Xanthophyl (ug)": ((), None), 
    "Thiamin (B1) (mg)": ((), None), 
    "Riboflavin (B2) (mg)": ((), None), 
    "Niacin (B3) (mg)": ((), None), 
    "Niacin derived from tryptophan (mg)": ((), None), 
    "Niacin derived equivalents (mg)": ((), None), 
    "Pantothenic acid (B5) (mg)": ((), None), 
    "Pyridoxine (B6) (mg)": ((), None), 
    "Biotin (B7) (ug)": ((), None), 
    "Cobalamin (B12) (ug)": ((), None), 
    "Folate, natural (ug)": ((), None), 
    "Folic acid (ug)": ((), None), 
    "Total folates (ug)": ((), None), 
    "Dietary folate equivalents (ug)": ((), None), 
    "Vitamin C (mg)": (("vitamin_c"), None), 
    "Cholecalciferol (D3) (ug)": ((), None), 
    "Ergocalciferol (D2) (ug)": ((), None), 
    "25-hydroxy cholecalciferol (25-OH D3 (ug)": ((), None), 
    "25-hydroxy ergocalciferol (25-OH D2) (ug)": ((), None), 
    "Vitamin D3 equivalents (ug)": ((), None), 
    "Alpha tocopherol (mg)": ((), None), 
    "Alpha tocotrienol (mg)": ((), None), 
    "Beta tocopherol (mg)": ((), None), 
    "Beta tocotrienol (mg)": ((), None), 
    "Delta tocopherol (mg)": ((), None), 
    "Delta tocotrienol (mg)": ((), None), 
    "Gamma tocopherol (mg)": ((), None), 
    "Gamma tocotrienol (mg)": ((), None), 
    "Vitamin E (mg)": ((), None), 
    "Total saturated fatty acids (g)": (("saturated_fat",), numeric), 
    "Total monounsaturated fatty acids (g)": (("monounsaturated_fat",), numeric), 
    "Other polyunsaturated fatty acids (g)": ((), None), 
    "Total polyunsaturated fatty acids (g)": (("polyunsaturated_fat",), numeric), 
    "Total long chain omega 3 fatty acids (mg)": (("omega_3",), None), 
    "Total undifferentiated fatty acids (mg)": ((), None), 
    "Total trans fatty acids (mg)": (("trans_fat",), numeric), 
    "Caffeine (mg)": (("caffeine",), numeric), 
    "Cholesterol (mg)": ((), None), 
    "Tryptophan (mg)": ((), None), 
    "Alanine (mg)": ((), None), 
    "Arginine (mg)": ((), None), 
    "Aspartic acid (mg)": ((), None), 
    "Cystine plus cysteine (mg)": ((), None), 
    "Glutamic acid (g)": ((), None), 
    "Glycine (mg)": ((), None), 
    "Histidine (mg)": ((), None), 
    "Isoleucine (mg)": ((), None), 
    "Leucine (mg)": ((), None), 
    "Lysine (mg)": ((), None), 
    "Methionine (mg)": ((), None), 
    "Phenylalanine (mg)": ((), None), 
    "Proline (mg)": ((), None), 
    "Serine (mg)": ((), None), 
    "Threonine (mg)": ((), None), 
    "Tyrosine (mg)": ((), None), 
    "Valine (mg)": ((), None), 
}
