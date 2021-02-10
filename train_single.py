import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from model.tableModel import tableModel
from matplotlib import pyplot as plt

learning_rate = 0.01

input_data = torch.from_numpy(np.load("data/vector_single/in2.npy")).float()
output_data = torch.from_numpy(np.load("data/vector_single/out2.npy")).float()

data_size = 1000
batch_size = 100
batch_num = data_size // batch_size

model = tableModel().float()

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

x = []
c = 0
y = []
loss = None
for epoch in range(100):
    for b in range(batch_num):
        inputs = input_data[b * batch_size:(b + 1) * batch_size]
        outputs = output_data[b * batch_size:(b + 1) * batch_size]

        optimizer.zero_grad()
        predicts = model(inputs)
        loss = criterion(predicts, outputs)

        loss.backward()
        optimizer.step()

    x.append(c)
    c += 1
    y.append(criterion(model(input_data[data_size:]), output_data[data_size:]))
    g = model(input_data[data_size:]) / output_data[data_size:]


plt.plot(x, y)
plt.show()
