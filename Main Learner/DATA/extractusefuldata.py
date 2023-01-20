import csv

csv_filer = csv.DictReader(open("test_ScotiaDSD.csv"))

for row in csv_filer:
    print(row)