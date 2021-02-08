import torch
import torch.nn as nn
import torch.nn.functional as F
from hyperparameter import single_size


class tableModel(nn.Module):
    def __init__(self):
        super(tableModel, self).__init__()
        self.fc1 = nn.Linear(single_size, 256)
        self.fc2 = nn.Linear(256, 256)
        self.fc3 = nn.Linear(256, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x
