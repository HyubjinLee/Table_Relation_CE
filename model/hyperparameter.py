learning_rate = 0.001
epoch = 500

table_num = 8
attribute_num = 5

single_feature = 4
single_size = attribute_num * single_feature

join_feature = 3
join_info = table_num * attribute_num
join_vec = 1 + attribute_num * join_feature
join_size = join_vec * table_num + join_info
