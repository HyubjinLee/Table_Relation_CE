import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from model.tableModel import tableModel
from matplotlib import pyplot as plt

learning_rate = 0.01

input_data = torch.from_numpy(np.load("data/vector_single/in0.npy")).float()
output_data = torch.from_numpy(np.load("data/vector_single/out0.npy")).float()

data_size = 1600
batch_size = 100
batch_num = data_size // batch_size

model = tableModel().float()

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

x = []
c = 0
y = []
loss = None
for epoch in range(500):
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
    y.append(criterion(model(input_data[1600:1610]), output_data[1600:1610]))
    print((model(input_data[1]).item()*2528312)//1, (output_data[1].item()*2528312)//1)
    g = model(input_data[1600:1610]) / output_data[1600:1610]

print(x)
print(y)
plt.plot(x, y)
plt.show()
