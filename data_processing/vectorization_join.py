import pandas as pd
import numpy as np
import torch
from model.tableModel import tableModel
from model.hyperparameter import join_size, join_feature
from data.schema import tables, columns, min_max, cardinality

df = pd.read_csv("../data/query_join.csv", sep='#')
join = [[], []]  # [[input(feature)], [output(cardinality)]]

models = {}
for table in tables:
    models[table] = tableModel().float()
    models[table].load_state_dict(torch.load("../model/save_single/" + table + ".pth"))

for i in range(1):
    table = df["table"][i].split(',')
    predicate = df["predicate"][i].split(',')
    vector = []

    for t in tables:
        if t in table:
            print(t)
            for p in range(0, len(predicate), 3):
                if predicate[p] in columns[t]:
                    index = columns[t].index(predicate[p])
        else:
            vector.extend([0 for _ in range(join_feature)])

    # join[1].append([int(df["cardinality"][i]) / cardinality[table]])
