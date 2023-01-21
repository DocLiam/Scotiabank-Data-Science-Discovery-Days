import csv

test = True

csv_filer = csv.DictReader(open("extracted_" + ("test" if test else "train") + "_ScotiaDSD.csv"))

i = 0

to_write_train = ""
to_write_validate = ""

for row in csv_filer:
    rest_values = []
    
    MEAN_7DAY_values = []
    STD_7DAY_values = []
    COUNT_7DAY_values = []

    MEAN_30DAY_values = []
    STD_30DAY_values = []
    COUNT_30DAY_values = []
    
    FLAG_headers = []
    
    FLAG_count = 0
    
    FLAG_MEAN_value = 0
    
    for header in row:
        FLAG_headers.append(header.split("_")[1]) if header.startswith("FLAG") else None
        
        MEAN_7DAY_values.append(float(row[header])) if header.startswith("MEAN") and header.endswith("7DAY") else None
        STD_7DAY_values.append(float(row[header])) if header.startswith("STD") and header.endswith("7DAY") else None
        COUNT_7DAY_values.append(float(row[header])) if header.startswith("COUNT") and header.endswith("7DAY") else None
    
        MEAN_30DAY_values.append(float(row[header])) if header.startswith("MEAN") and header.endswith("30DAY") else None
        STD_30DAY_values.append(float(row[header])) if header.startswith("STD") and header.endswith("30DAY") else None
        COUNT_7DAY_values.append(float(row[header])) if header.startswith("COUNT") and header.endswith("30DAY") else None

        if header.startswith("MEAN") and header.endswith("30DAY") and header.split("_PAST")[0].split("MEAN_")[1] in FLAG_headers:
            FLAG_count += 1.0
            
            FLAG_MEAN_value += float(row[header])
    
    FLAG_MEAN_value /= FLAG_count
    
    sum_MEAN_7DAY = sum(MEAN_7DAY_values)
    sum_STD_7DAY = sum(STD_7DAY_values)
    sum_COUNT_7DAY = sum(COUNT_7DAY_values)
    
    sum_MEAN_30DAY = sum(MEAN_30DAY_values)
    sum_STD_30DAY = sum(STD_30DAY_values)
    sum_COUNT_30DAY = sum(COUNT_30DAY_values)
    
    adjusted_MEAN_7DAY_values = [value/sum_MEAN_7DAY for value in MEAN_7DAY_values] if sum_MEAN_7DAY > 0 else MEAN_7DAY_values
    adjusted_STD_7DAY_values = [value/sum_STD_7DAY for value in STD_7DAY_values] if sum_STD_7DAY > 0 else STD_7DAY_values
    adjusted_COUNT_7DAY_values = [value/sum_COUNT_7DAY for value in COUNT_7DAY_values] if sum_COUNT_7DAY > 0 else COUNT_7DAY_values
    
    adjusted_MEAN_30DAY_values = [value/sum_MEAN_30DAY for value in MEAN_30DAY_values] if sum_MEAN_30DAY > 0 else MEAN_30DAY_values
    adjusted_STD_30DAY_values = [value/sum_STD_30DAY for value in STD_30DAY_values] if sum_STD_30DAY > 0 else STD_30DAY_values
    adjusted_COUNT_30DAY_values = [value/sum_COUNT_30DAY for value in COUNT_30DAY_values] if sum_COUNT_30DAY > 0 else COUNT_30DAY_values
    
    for header in row:
        if header == "AMOUNT":
            rest_values.append(float(row[header])/FLAG_MEAN_value) if FLAG_MEAN_value != 0 else rest_values.append(1.0)
        elif header == "AVAIL_CRDT" or header == "CREDIT_LIMIT":
            rest_values.append(float(row[header])/10000.0)
        elif not header.endswith("DAY") and not header == "TRANSACTION_ID" and not header == "FRAUD_FLAG":
            rest_values.append(float(row[header]))
    
    rest_values += adjusted_MEAN_7DAY_values
    rest_values += adjusted_STD_7DAY_values
    rest_values += adjusted_COUNT_7DAY_values
    
    rest_values += adjusted_MEAN_30DAY_values
    rest_values += adjusted_STD_30DAY_values
    rest_values += adjusted_COUNT_30DAY_values
    
    if i%2 == 0:
        to_write_train += ",".join([str(value) for value in rest_values]) + ":" + ("" if len(row["FRAUD_FLAG"]) == 0 else ("1.0,0" if float(row["FRAUD_FLAG"]) == 0 else "0,1.0")) + "\n"
    else:
        to_write_validate += ",".join([str(value) for value in rest_values]) + ":" + ("" if len(row["FRAUD_FLAG"]) == 0 else ("1.0,0" if float(row["FRAUD_FLAG"]) == 0 else "0,1.0")) + "\n"
    
    i += 1
    
    #if i == 20000:
        #break

if not test:
    filew_train = open("SCOTIABANKDSDTRAIN.txt", "w")
    filew_train.write(to_write_train[:-1])
    filew_train.close()

    filew_validate = open("SCOTIABANKDSDVALIDATE.txt", "w")
    filew_validate.write(to_write_validate[:-1])
    filew_validate.close()
else:
    filew_test = open("SCOTIABANKDSDTEST.txt", "w")
    filew_test.write(to_write_train + to_write_validate[:-1])
    filew_test.close()