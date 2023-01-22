from audioop import rms
from DeepLearner import *
import matplotlib.pyplot as plt

data_name = input("Data name: ")
model_name = input("Model name: ")

Model = Model_Class()
Model.load(model_name)

Data = Data_Class()
Data.extract(data_name + "TEST")

Model.test(Data)

prediction_values = ["1" if Model.output_values[i] <= Model.output_values[i+1] else "0" for i in range(len(Model.output_values)//2)]

print("\n".join(prediction_values[::-1]))