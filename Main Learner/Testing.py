#Copyright (c) 2023 by Liam Watson and Watcode. All rights reserved. For licensing, contact lrwatson@uwaterloo.ca or +1 437 688 3927

from audioop import rms
from DeepLearner import *
import matplotlib.pyplot as plt
import csv

data_name = input("Data name: ")
model_name = input("Model name: ")

Model = Model_Class()
Model.load(model_name)

Data = Data_Class()
Data.extract(data_name + "TEST")

Model.test(Data)

predicted_values = [1 if Model.output_values[i] <= Model.output_values[i+1] else 0 for i in range(0, len(Model.output_values), 2)]
probability_values = [abs(Model.output_values[i]-Model.output_values[i+1]) for i in range(0, len(Model.output_values), 2)]

required_values = [1 if Data.target_values[i] <= Data.target_values[i+1] else 0 for i in range(0, len(Data.target_values), 2)]

print("\n".join([str(i) for i in predicted_values[::-1]]))

missed_fraud_values = []
declined_non_fraud_values = []

for i in range(len(predicted_values)):
    missed_fraud_values.append(1) if predicted_values[i]-required_values[i] < 0 else (declined_non_fraud_values.append(1) if predicted_values[i]-required_values[i] > 0 else None)

print("Missed fraud cases: ", sum(missed_fraud_values))
print("Declined non-fraud cases: ", sum(declined_non_fraud_values))

print("Total fraud cases predictions: ", sum(predicted_values))
print("Total actual fraud cases: ", sum(required_values))

print("Sample size: ", len(predicted_values))

test = True

if test:
    csv_filer = csv.DictReader(open("./DATA/extracted_test_ScotiaDSD.csv"))

    with open("submission.csv", 'w', newline='') as csv_filew:
        writer = csv.writer(csv_filew, delimiter=',')
        
        writer.writerow(["TRANSACTION_ID", "PREDICTION", "PROBABILITY"])
        
        i = 0
        
        for row in csv_filer:
            writer.writerow([row["TRANSACTION_ID"], int(predicted_values[i]), round(float(probability_values[i]), 5)])
            
            i += 1
else:
    csv_filer = csv.DictReader(open("./DATA/train_ScotiaDSD.csv"))
    
    x_values = [i*10000 for i in range(11)]
    y_values = [0 for i in range(11)]
    y_values2 = [0 for i in range(11)]
    
    count_values = [0 for i in range(11)]
    
    for row in csv_filer:
        y_values[int(float(row["CREDIT_LIMIT"])//10000)] += float(row["FRAUD_FLAG"])
    
        count_values[int(float(row["CREDIT_LIMIT"])//10000)] += 1
        
    y_values = [y_values[i]/float(count_values[i]) if count_values[i] > 0 else 0 for i in range(len(y_values))]
    
    plt.plot(x_values, y_values)
    plt.show()