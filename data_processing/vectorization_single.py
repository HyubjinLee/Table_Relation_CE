import pandas as pd
import numpy as np
from model.hyperparameter import single_size, single_feature
from data.schema import tables, columns, min_max, cardinality

df = pd.read_csv("../data/query_single.csv", sep='#')

single = {x: [[], []] for x in tables}  # [[input(feature)], [output(cardinality)]]
for i in range(len(df)):
    table = df["table"][i]
    vector = [0 for _ in range(single_size)]

    predicate = df["predicate"][i].split(',')
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

    single[table][0].append(vector)
    single[table][1].append([int(df["cardinality"][i]) / cardinality[table]])

for table in tables:
    print(len(single[table][0]))
    single[table][0] = np.array(single[table][0])
    np.save("../data/vector_single/in_" + table + ".npy", single[table][0])
    single[table][1] = np.array(single[table][1])
    np.save("../data/vector_single/out_" + table + ".npy", single[table][1])


