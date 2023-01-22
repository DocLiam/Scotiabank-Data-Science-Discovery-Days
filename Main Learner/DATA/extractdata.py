#Copyright (c) 2023 by Liam Watson and Watcode. All rights reserved. For licensing, contact lrwatson@uwaterloo.ca or +1 437 688 3927

import csv

desired_headers = []

for line in open("desired_headers.txt", "r").read().split("\n"):
    (lambda x : desired_headers.append(x[0]) if x[1] == "1" else None)(line.split(" "))

print(desired_headers)

csv_filer = csv.DictReader(open("train_ScotiaDSD.csv"))

with open("extracted_train_ScotiaDSD.csv", 'w', newline='') as csv_filew:
    writer = csv.writer(csv_filew, delimiter=',')
    
    writer.writerow(desired_headers)
    
    for row in csv_filer:
        writer.writerow([row[header] for header in desired_headers])