# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 01:30:15 2018

@author: 31401
"""

import numpy as np
import copy
from sklearn.cluster import KMeans

#导入数据
#data3是原始数据永不变，本次用data
#data3 = np.load('data_random_1w_sort.npy')
#data3 = data3.tolist()
data = copy.deepcopy(data3)

#去掉抬头，变为数字
title = data[0]
data.pop(0)
for i in range(len(data)):
    for j in range(1,len(data[0])):
        data[i][j] = int(data[i][j])

#聚类，得到label
center_num = 20
kmeans=KMeans(n_clusters=center_num)
kmeans.fit([x[1:] for x in data])
labels=kmeans.labels_

#根据label重新排序
data2 = [[title] for i in range(center_num)]
for i in range(len(labels)):
    data2[labels[i]].append(data[i])
    
#输出clusters为txt，np.savetxt('data_random_1w_kmeans_1_pic.txt',data2_1_pure)
for i in range(center_num):
    name = 'data2_' + str(i+1) + '_pure'
    exec(name+'=copy.deepcopy(data2[i][1:])')
    for j in range(len(data2[i])-1):
        exec(name+'[j].pop(0)')
        

#kmeans7=KMeans(n_clusters=3)
#kmeans7.fit([x[1:] for x in data2[6]])
#labels7=kmeans7.labels_
#data7 = []