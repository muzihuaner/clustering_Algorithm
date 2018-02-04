# coding=utf-8

from Max_Min_Cluster import max_min_cluster
from knn_cluster import knn_cluster


data = [[0, 0], [3, 8], [1, 1], [2, 2], [5, 3], [4, 8], [6, 3], [5, 4], [6, 4], [7, 5]]

# 测试Max_Min_CLuster
t = 0.5
result = max_min_cluster(data, t)

# # 测试knn_Cluster
# t = 4.5
# result = knn_cluster(data, t)

for i in range(len(result)):
    print "----------第" + str(i+1) + "个聚类----------"
    print result[i]
