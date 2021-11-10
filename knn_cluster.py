# coding=utf-8

# 近邻聚类算法的Python实现
# 数据集形式data=[[],[],...,[]]
# 聚类结果形式result=[[[],[],...],[[],[],...],...]
# 其中[]为一个模式样本，[[],[],...]为一个聚类

from max_min_cluster import get_distance, classify


def knn_cluster(data, t):

    # data：数据集，t：距离阈值
    # 算法描述中的介绍的是在寻找聚类中心的同时进行聚类，本次实现中并未采取这种方式，
    # 原因是同时进行的话要既要考虑聚类中心，又要考虑某个类，实现较为麻烦，
    # 此次采取与上次最大最小距离算法相同的方式，先寻找聚类中心，再根据最近邻原则分类，
    # 两种方式实现效果是相同的，同时又可以直接利用最大最小距离聚类算法中写好的classify()分类方法

    zs = [data[0]]  # 聚类中心集，选取第一个模式样本作为第一个聚类中心Z1
    # 计算聚类中心
    get_clusters(data, zs, t)
    # 分类
    result = classify(data, zs, t)
    return result


def get_clusters(data, zs, t):

    # 得到所有的聚类中心

    for aData in data:
        min_distance = get_distance(aData, zs[0])
        for i in range(0, len(zs)):
            distance = get_distance(aData, zs[i])
            if distance < min_distance:
                min_distance = distance
        if min_distance > t:
            zs.append(aData)


# data = [[0, 0], [3, 8], [1, 1], [2, 2], [5, 3], [4, 8], [6, 3], [5, 4], [6, 4], [7, 5]]
# t = 4.5
# result = knn_cluster(data, t)
# for i in range(len(result)):
#     print("----------第" + str(i+1) + "个聚类----------")
#     print(result[i])
