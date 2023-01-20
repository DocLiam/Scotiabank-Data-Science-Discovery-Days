import csv

csv_filer = csv.DictReader(open("extracted_train_ScotiaDSD.csv"))

i = 0

for row in csv_filer:
    
    
    i += 1