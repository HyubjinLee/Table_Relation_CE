import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from data.schema import tables
from model.hyperparameter import learning_rate, epoch
from model.tableModel import tableModel
from matplotlib import pyplot as plt


model = tableModel().float()
model.load_state_dict(torch.load("model/save_single/title t99.pth"))
optimizer = optim.Adam(model.parameters(), lr=learning_rate)
input_data = torch.from_numpy(np.load("data/vector_single/in_title t.npy")).float()
output_data = torch.from_numpy(np.load("data/vector_single/out_title t.npy")).float()

data_size = int(len(input_data) * 0.9)
criterion = nn.MSELoss()

val_loss = criterion(model(input_data[data_size:]), output_data[data_size:])
print(val_loss)