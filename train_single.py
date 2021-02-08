import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from matplotlib import pyplot as plt

input_data = torch.from_numpy(np.load("data/vector_single/in0.npy")).float()
print(input_data[0])