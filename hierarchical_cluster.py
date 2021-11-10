# coding=utf-8
#层次聚类算法
from max_min_cluster import get_distance


def hierarchical_cluster(data, t):
    # N个模式样本自成一类
    result = [[aData] for aData in data]
    step2(result, t)
    return result


def step2(result, t):

    # 记录类间最小距离
    min_dis = min_distance(result[0], result[1])  # 初始为1,2类之间的距离

    # 即将合并的类
    index1 = 0
    index2 = 1

    # 遍历，寻找最小类间距离
    for i in range(len(result)):
        for j in range(i+1, len(result)):
            dis_temp = min_distance(result[i], result[j])
            if dis_temp < min_dis:
                min_dis = dis_temp
                # 记录即将合并的聚类位置下标
                index1 = i
                index2 = j

    # 阈值判断
    if min_dis <= t:
        # 合并聚类index1, index2
        result[index1].extend(result[index2])
        result.pop(index2)
        # 迭代计算，直至min_dis>t为止
        step2(result, t)


def min_distance(list1, list2):

    # 计算两个聚类之间的最小距离：
    # 遍历两个聚类的所有元素，计算距离（方法较为笨拙，有待改进）

    min_dis = get_distance(list1[0], list2[0])
    for i in range(len(list1)):
        for j in range(len(list2)):
            dis_temp = get_distance(list1[i], list2[j])
            if dis_temp < min_dis:
                min_dis = dis_temp
    return min_dis
