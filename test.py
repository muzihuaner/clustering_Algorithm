# coding=utf-8

import math

from max_min_cluster import max_min_cluster
from knn_cluster import knn_cluster
from hierarchical_cluster import hierarchical_cluster
from k_means_cluster import k_means_cluster


# data = [[0, 0], [3, 8], [1, 1], [2, 2], [5, 3], [4, 8], [6, 3], [5, 4], [6, 4], [7, 5]]

# 测试max_min_CLuster
# t = 0.5
# result = max_min_cluster(data, t)

# 测试knn_Cluster
# t = 4.5
# result = knn_cluster(data, t)

# 测试hierarchical_cluster
# data = [[0, 3, 1, 2, 0], [1, 3, 0, 1, 0], [3, 3, 0, 0, 1], [1, 1, 0, 2, 0], [3, 2, 1, 2, 1], [4, 1, 1, 1, 0]]
# t = math.sqrt(5.5)
# result = hierarchical_cluster(data, t)

# 测试k_means_cluster
data = [[0, 0], [1, 0], [0, 1], [1, 1], [2, 1], [1, 2], [2, 2], [3, 2], [6, 6], [7, 6], [8, 6], [6, 7], [7, 7], [8, 7],
        [9, 7], [7, 8], [8, 8], [9, 8], [8, 9], [9, 9]]
k = 2
result = k_means_cluster(data, k)


for i in range(len(result)):
    print "----------第" + str(i+1) + "个聚类----------"
    print result[i]
