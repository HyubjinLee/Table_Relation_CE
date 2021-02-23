import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from data.schema import tables
from model.hyperparameter import learning_rate, epoch
from model.relationModel import relationModel
from matplotlib import pyplot as plt

input_data = torch.from_numpy(np.load("data/vector_join/in.npy")).float()
output_data = torch.from_numpy(np.load("data/vector_join/out.npy")).float()

data_size = int(len(input_data) * 0.9)
train_input = input_data[:data_size]
train_output = output_data[:data_size]
validation_input = input_data[data_size:]
validation_output = output_data[data_size:]

batch_size = 100
batch_num = data_size // batch_size

model = relationModel().float()

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

c = 0
x = []
y = []
min_loss = 1
loss = None
for epoch in range(250):
    for b in range(batch_num):
        inputs = train_input[b * batch_size:(b + 1) * batch_size]
        outputs = train_output[b * batch_size:(b + 1) * batch_size]

        optimizer.zero_grad()
        predicts = model(inputs)
        loss = criterion(predicts, outputs)

        loss.backward()
        optimizer.step()

    x.append(c)
    c += 1
    val_loss = criterion(model(validation_input), validation_output)
    y.append(val_loss)

    if val_loss < min_loss:
        min_loss = val_loss
        torch.save(model.state_dict(), "model/save_join/save.pth")

        print(epoch, val_loss)
        print(model(validation_input[0:5]))
        print(validation_output[0:5])

print(min_loss)
plt.plot(x, y)
plt.show()
