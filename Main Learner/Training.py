#Copyright (c) 2023 by Liam Watson and Watcode. All rights reserved. For licensing, contact lrwatson@uwaterloo.ca or +1 437 688 3927

from DeepLearner import *

data_name = input("Data name: ")
model_name = input("Model name: ")

Model = Model_Class()
Model.load(model_name, min_diff=0.01, learning_rate=0.0000001, cycles=500, hidden_shaped=True, normaliser_depth=0)

Data_train = Data_Class()
Data_validate = Data_Class()

Data_train.extract(data_name + "TRAIN")
Data_validate.extract(data_name + "VALIDATE")

#Model.genetic_train(Data_train, 0.8, 10, 200)

Model.train(Data_train, Data_validate)
Model.save()