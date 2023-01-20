import csv

csv_filer = csv.DictReader(open("extracted_train_ScotiaDSD.csv"))

i = 0

for row in csv_filer:
    MEAN_7DAY_values = []
    STD_7DAY_values = []

    MEAN_30DAY_values = []
    STD_30DAY_values = []
    
    for header in row:
        MEAN_7DAY_values.append(float(row[header])) if header.startswith("MEAN") and header.endswith("7DAY") else None
        STD_7DAY_values.append(float(row[header])) if header.startswith("STD") and header.endswith("7DAY") else None
    
        MEAN_30DAY_values.append(float(row[header])) if header.startswith("MEAN") and header.endswith("30DAY") else None
        STD_30DAY_values.append(float(row[header])) if header.startswith("STD") and header.endswith("30DAY") else None
    
    i += 1