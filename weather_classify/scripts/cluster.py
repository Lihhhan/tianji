#coding=utf-8
from math import sqrt
import random, logging

#计算两个向量v1, v2之间的欧几里得距离,完全相同为1
def euc(v1, v2):
    Sum = 0.0
    for i in range(len(v1)):
       Sum += (v1[i] - v2[i])**2
    return 1/(1+Sum**0.5)

#计算两个向量v1, v2之间的pearson相关度 返回1.0则完全匹配， 毫无关系返回0.0
def pearson(v1, v2):
    
    sum1 = sum(v1)
    sum1Sq = sum([v**2 for v in v1])
    
    sum2 = sum(v2)
    sum2Sq = sum([v**2 for v in v2])

    pSum = sum([v1[i]*v2[i] for i in range(len(v1))])
   
    num = pSum - (sum1*sum2/len(v1))
    score = sqrt((sum1Sq - sum1**2/len(v1))*(sum2Sq - sum2**2/len(v2)))
    if score == 0:
        return 0
    return 1.0-num/score

#K-Means cluster
#rows 是readfile()返回的data格式的数据
#distance 是计算向量之间距离的函数，默认是pearson相关度
#k 是生成聚类的个数
def kcluster(rows, distance=pearson, k=4):
    ranges = [( min([row[i] for row in rows]), max([row[i] for row in rows])) for i in range(len(rows[0]))]
    #生成k个每个维度在data最值之间的种子点
    clusters = [ [ random.random()*(ranges[i][1] - ranges[i][0]) + ranges[i][0] for i in range(len(rows[0]))] for j in range(k)]
    lastmatches = None
    
    for row in rows:
        print row

    for times in range(100):
        #聚类迭代
        logging.info('第%s次聚类迭代..'%times)
        bestmatches = [[] for i in range(k)]
        sum_dis = 0
        for i in range(len(rows)):
            bestmatch = 0
            min_dis = distance(rows[i], clusters[bestmatch])
            for j in range(len(clusters)-1):
                d = distance(rows[i], clusters[j+1])
                if d < min_dis:
                    bestmatch = j+1
                    min_dis = d

            bestmatches[bestmatch].append(i)
            sum_dis += min_dis
        
        print bestmatches
        logging.info('第%s次聚类all_dis为%s'%(times, sum_dis))
        if lastmatches == bestmatches:
            logging.info('聚类迭代在第%s次结束'%times)
            break
        lastmatches = bestmatches 
        
        #第一轮分类结束，重新计算聚类中心，这里就用平均值来算
        for i in range(k):
            temp = [0.0] * len(rows[0])
            if len(bestmatches[i]) == 0:
                clusters[i] = temp 
            else:
                for j in bestmatches[i]:
                    temp = [ temp[item]+rows[j][item] for item in range(len(rows[0])) ]
                clusters[i] = [ temp[items]/len(bestmatches[i]) for items in range(len(rows[0]))]
    return bestmatches



