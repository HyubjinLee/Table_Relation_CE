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

for i in range(len(df)):
    tables = df["table"][i].split(',')
    vectors = [0 for _ in range(join_size)]

    predicates = df["predicate"][i].split(',')
    for p in range(0, len(predicate), 3):  # 3 is predicate size: ['a', '>', '100']
        index = columns[table].index(predicate[p]) * single_feature
        if predicate[p + 1] == '>':
            vector[index] = 1
        elif predicate[p + 1] == '=':
            vector[index + 1] = 1
        else:  # '<'
            vector[index + 2] = 1

        vector[index + 3] = (float(predicate[p + 2]) - min_max[predicate[p]][0]) / (
                min_max[predicate[p]][1] - min_max[predicate[p]][0])

    joins = df["join"][i].replace('=', ',').split(',')

    single[table][0].append(vector)
    single[table][1].append([int(df["cardinality"][i]) / cardinality[table]])

for table in tables:
    print(len(single[table][0]))
    single[table][0] = np.array(single[table][0])
    np.save("../data/vector_single/in_" + table + ".npy", single[table][0])
    single[table][1] = np.array(single[table][1])
    np.save("../data/vector_single/out_" + table + ".npy", single[table][1])
