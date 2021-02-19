import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import numpy as np
from data.schema import tables
from model.hyperparameter import learning_rate, epoch
from model.tableModel import tableModel
from matplotlib import pyplot as plt


df = pd.read_csv("data/query_join.csv", sep='#')
print(max(df["cardinality"]))

# model = tableModel().float()
# model.load_state_dict(torch.load("model/save_single/title t.pth"))
# input_data = torch.from_numpy(np.load("data/vector_single/in_title t.npy")).float()
# output_data = torch.from_numpy(np.load("data/vector_single/out_title t.npy")).float()
#
# data_size = int(len(input_data) * 0.9)
# criterion = nn.MSELoss()
#
# val_loss = criterion(model(input_data[data_size:]), output_data[data_size:])
# print(val_loss)
# print(model(input_data[data_size]))
# print(output_data[data_size])
