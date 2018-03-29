# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:05:29 2018

@author: 31401
"""              
#导入数据，只要修改第十行就可以了
import numpy as np
import copy
data_random_1w = np.load('data_random_1w.npy')
data_random_1w = data_random_1w.tolist()
data = copy.deepcopy(data_random_1w)

#找出一直为0的特征
feature_nonexist = ['feature nonexist']   #feature_nonexist.npy
for i in range(1,len(data[0])):
    if [x[i] for x in data].count('1') == 0:
        feature_nonexist.append(data[0][i])
        
#删去一直为0的特征    
for k in range(1,len(feature_nonexist)):   
    pos = data[0].index(feature_nonexist[k])  
    for m in range(len(data)):
        data[m].pop(pos)     

#存储删好的在real里，以后real都不变
data_random_1w_real = copy.deepcopy(data)

#把特征分成多组，每组是同时出现的。第一个数为该组出现的频率，得到group，此时data已毁
group = [['each row is a group']]
temp = []
while len(data[0]) > 1:
    temp.append([x[1] for x in data].count('1'))  #看这一组的出现频率
    temp.append(data[0][1]) #temp中存储了此轮的title
    for i in range(2,len(data[0])):   #列，从第二列开始判断与第一列是否一致，这个for整个走完则一组产生
        if [x[1] for x in data[1:]] == [x[i] for x in data[1:]]:   #若一致则加进去,存title
            temp.append(data[0][i]) 
    for k in range(1,len(temp)):   #最后一次，把一致的都删掉，将temp加到group
        pos = data[0].index(temp[k])  #找到该列位置
        for m in range(len(data)):
            data[m].pop(pos)
    group.append(temp)
    temp = []
    
#把同组的特征放一起，得到data2
data = copy.deepcopy(data_random_1w_real)
data2 = [[0 for i in range(len(data[0]))]for i in range(len(data))]
count_column = 1
for i in range(1,len(group)):  #对每组
    for j in range(1,len(group[i])):  #该组的每个元素，即特征
        pos = data[0].index(group[i][j])  #该特征所在列
        for k in range(len(data)):  #每项都拷贝到data2中
            data2[k][count_column] = data[k][pos]
        count_column = count_column + 1
for i in range(len(data)):  #拷贝patient_id列
    data2[i][0] = data[i][0]
    
#将patient根据接受检查的数量排列，得到data3，data3已是最终版，data_random_1w_sort.npy
title_new = copy.deepcopy(data2[0])
data2_pure = data2[1:]
data3 = sorted(data2_pure, key = lambda data2_pure: data2_pure.count('1'), reverse = 1)
data3.insert(0,title_new)

#提取最终的data3作图，data3_pure只有数字，data_random_1w_sort_pic.txt
data3_pure = copy.deepcopy(data3[1:])
for i in range(len(data3_pure)):
    data3_pure[i].pop(0)
for i in range(len(data3_pure)):
    for j in range(len(data3_pure[0])):
        data3_pure[i][j] = int(data3_pure[i][j])