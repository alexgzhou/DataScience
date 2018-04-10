# coding:utf-8

import readfile as rf
import numpy as np
import random
import math
import predictor as pred
import appendix as ap
import log


def single_training_process(algorithm, dataset, fold=10):

    # ----------------- .csv源文件数据分割 ------------------------

    # 分割未分割.csv文件中存储的数据至~_x.csv,~_y.csv两个文件中
    # path_y_label = '../datasets/corel16k/corel16k001.xml'
    # path_dataset = '../datasets/corel16k/corel16k001.csv'
    # rf.divide_csv(path_dataset, rf.read_labels_from_xml(path_y_label))

    # --------------------- 数据来源是.mat ------------------------
    # 读取.mat文件中存储的数据集
    # x_tr, y_tr = rf.read_mat('../datasets/CAL500_train.mat')
    # x_te, y_te = rf.read_mat('../datasets/CAL500_test.mat')
    # x_tr = np.array(x_tr)
    # y_tr = np.array(y_tr)
    # x_te = np.array(x_te)
    # y_te = np.array(y_te)

    # ---------------------- 生成Log文件 --------------------------
    l = log.Log('default-%s-%s' % (algorithm, dataset))

    # --------------------- 数据来源是.csv ------------------------
    # 读取来自_x.csv,_y.csv文件的输入、金标准数据以及其label

    # 日志log文档记录点
    behave = 'start reading dataset'
    l.write_format_log(behave, dataset, algorithm)

    path_x = '../datasets/%s/%s_x.csv' % (dataset, dataset)
    path_y = '../datasets/%s/%s_y.csv' % (dataset, dataset)
    x, x_label = rf.read_csv(path_x)
    y, y_label = rf.read_csv(path_y)

    # 日志log文档记录点
    behave = 'finish reading dataset'
    l.write_format_log(behave, dataset, algorithm)

    # 随机分为fold折进行交叉验证，每一折的测试集序号

    m = int(math.floor(np.size(x, axis=0)/fold))
    indices = np.reshape(random.sample(range(m*fold), m*fold), [fold, m])

    # 第k次检验,选择训练集、测试集和验证集
    for k in range(fold):

        # 日志log文档记录点
        behave = 'pre-processing'
        l.write_format_log(behave, dataset, algorithm, fold=k)

        v = 4   # 3+1 3份用于确定优化顺序，1份用于确定优化截止点
        group_tr = list(range(fold))
        group_tr.remove(k)
        group_te = k
        group_va = [(k + e) % fold for e in range(1, v+1)]

        indice_tr = np.reshape(indices[group_tr], [m*(fold-1)])
        indice_te = np.reshape(indices[group_te], [m])
        indice_va = np.reshape(indices[group_va], [m*v])

        x_tr = x[indice_tr]
        y_tr = y[indice_tr]
        x_te = x[indice_te]
        y_te = y[indice_te]
        x_va = x[indice_va]
        y_va = y[indice_va]

    # -------------------------------- 选择使用的前置算法 ------------------------------------
        # 在这里调用所查到的算法代码，其输入训练数据x_tr, y_tr和测试集的x_te，输出为算法预测结果y_
        # y_ = function(x_tr, y_tr, x_te)
        # 注意！y_te不能够输入至算法内！

        # 日志log文档记录点
        behave = 'original training'
        l.write_format_log(behave, dataset, algorithm, fold=k)

        y_te_, y_va_ = pred.predictor(algorithm, x_tr, y_tr, x_te, x_va)
    # -------------------------------- 选择使用的前置算法 ------------------------------------

        # 通过后缀算法更改预测结果
        param = {
            'fold': k,
            'algorithm': algorithm,
            'dataset': dataset,
            'labels': y_label
            }

        # 日志log文档记录点
        behave = 'appendix training'
        l.write_format_log(behave, dataset, algorithm, fold=k)

        ap.regression_method(y_tr, y_va, y_va_, y_te, y_te_, param)

