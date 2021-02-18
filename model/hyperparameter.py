learning_rate = 0.001
epoch = 500

table_num = 8
column_num = 5

single_feature = 4
single_size = column_num * single_feature

join_feature = 3
join_info = table_num * column_num
join_size = (1 + column_num * join_feature) * table_num + join_info
