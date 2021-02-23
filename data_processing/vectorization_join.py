import pandas as pd
import numpy as np
import torch
from model.tableModel import tableModel
from model.hyperparameter import join_size, join_feature, join_vec, join_info, single_size, single_feature
from data.schema import tables, ban_tables, attributes, all_attributes, min_max, cardinality

df = pd.read_csv("../data/query_join.csv", sep='#')
joins = [[], []]  # [[input(feature)], [output(cardinality)]]

models = {}
for table in tables:
    models[table] = tableModel().float()
    models[table].load_state_dict(torch.load("../model/save_single/" + table + ".pth"))

for i in range(3):
    table = df["table"][i].split(',')
    predicate = df["predicate"][i].split(',')
    join = df["join"][i].replace('=', ',').split(',')

    vector = [0 for _ in range(join_vec)]
    information = [0 for _ in range(join_info)]

    for t in table:
        j_index = tables.index(t) * join_vec
        single = [0 for _ in range(single_size)]
        model = models[t]

        predicate_flag = False
        for p in range(0, len(predicate), 3):
            if predicate[p] in attributes[t]:
                predicate_flag = True
                s_index = attributes[t].index(predicate[p]) * single_feature

                if predicate[p + 1] == '>':
                    single[s_index] = 1
                elif predicate[p + 1] == '=':
                    single[s_index + 1] = 1
                else:  # '<'
                    single[s_index + 2] = 1

                single[s_index + 3] = (float(predicate[p + 2]) - min_max[predicate[p]][0]) / (
                            min_max[predicate[p]][1] - min_max[predicate[p]][0])

        single = torch.tensor(single).float()
        print(model(single))

    for j in join:
        information[all_attributes.index(j)] += 1

    vector.extend(information)
    joins[0].append(vector)
    joins[1].append([int(df["cardinality"][i]) / cardinality["join"]])

joins[0] = np.array(joins[0])
np.save("../data/vector_join/in.npy", joins[0])
joins[1] = np.array(joins[1])
np.save("../data/vector_join/out.npy", joins[1])
