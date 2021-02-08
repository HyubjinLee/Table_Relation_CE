import pandas as pd

single = {"table": [], "predicate": [], "cardinality": []}
join = {"table": [], "join": [], "predicate": [], "cardinality": []}

df = pd.read_csv("../data/query.csv", sep='#', names=["table", "join", "predicate", "cardinality"])

for i in range(len(df)):
    table = df["table"][i].split(',')
    if len(table) == 1:  # single query
        for key in ["table", "predicate", "cardinality"]:
            single[key].append(df[key][i])
    else:  # join query
        for key in ["table", "join", "predicate", "cardinality"]:
            join[key].append(df[key][i])

single = pd.DataFrame(single)
join = pd.DataFrame(join)
single.to_csv("../data/query_single.csv", sep='#', index=False)
join.to_csv("../data/query_join.csv", sep='#', index=False)
