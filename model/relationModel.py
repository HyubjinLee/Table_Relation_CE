import torch
import torch.nn as nn
import torch.nn.functional as F
from model.hyperparameter import join_size


class relationModel(nn.Module):
    def __init__(self):
        super(relationModel, self).__init__()
        self.fc1 = nn.Linear(join_size, 256)
        self.fc2 = nn.Linear(256, 256)
        self.fc3 = nn.Linear(256, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x
