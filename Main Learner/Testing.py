from audioop import rms
from DeepLearner import *
import matplotlib.pyplot as plt

data_name = input("Data name: ")
model_name = input("Model name: ")

Model = Model_Class()
Model.load(model_name)

Data = Data_Class()
Data.extract(data_name + "VALIDATe")

Model.test(Data)

predicted_values = [1 if Model.output_values[i] <= Model.output_values[i+1] else 0 for i in range(0, len(Model.output_values), 2)]
required_values = [1 if Data.target_values[i] <= Data.target_values[i+1] else 0 for i in range(0, len(Data.target_values), 2)]

print("\n".join([str(i) for i in predicted_values[::-1]]))
print([float(i) for i in Model.output_values[:100]])

print(sum([abs(predicted_values[i]-required_values[i]) for i in range(len(predicted_values))]))

print(sum(predicted_values))
print(sum(required_values))

print(len(predicted_values))