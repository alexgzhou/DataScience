# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 14:40:37 2018

@author: 31401
"""
#导入数据,data为加过title的原始数据
import numpy as np
data = np.load('D:\I_AM\data.npy')
data = data.tolist()

#转换01，做过的的为1，没做过的为0
for k in range(1,len(data)):   
    for m in range(1,len(data[0])):
        if data[k][m] == 1 or data[k][m] == -1 or data[k][m] == 0:
            data[k][m] = 1
        else:
            data[k][m] = 0

#找出一直为0的特征
feature_nonexist = ['feature nonexist']   #feature_nonexist.npy，300+个
for i in range(1,len(data[0])):
    if [x[i] for x in data].count(1) == 0:
        feature_nonexist.append(data[0][i])
        
#删去一直为0的特征    
for k in range(1,len(feature_nonexist)):   
    pos = data[0].index(feature_nonexist[k])  
    for m in range(len(data)):
        data[m].pop(pos)     
        
#找出没有做过检查的患者
patient_nonexist = ['patient nonexist']   #patient_nonexist.npy，1w+个
for i in range(1,len(data)):
    if data[i].count(1) == 0:
        patient_nonexist.append(data[i][0])
        
#删去一直没有做过检查的患者（这个很慢）
for k in range(1,len(patient_nonexist)):   
    pos = [x[0] for x in data].index(patient_nonexist[k])  
    data.pop(pos)
    
#随机取1w个，取3次
import random
title = data[0]  #title.npy
data.pop(0)
data_random_1w = random.sample(data,10000)  
data_random_1w_2 = random.sample(data,10000)
data_random_1w_3 = random.sample(data,10000)
data_random_1w.insert(0,title)   #data_random_1w.npy
data_random_1w_2.insert(0,title)  #data_random_1w_2.npy
data_random_1w_3.insert(0,title)  #data_random_1w_3.npy
