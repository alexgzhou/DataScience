import mat4py as mp
from evaluate import Evaluate
import numpy as np
import readfile as rf
import log
import appendix as ap
import math
import random
import predictor as pred
import readfile as rf

fold = 10

datasets = ['yeast',  'scene', 'CAL500', 'emotions', 'enron', 'genbase', 'medical',
            'corel5k', 'Corel16k001', 'Corel16k002', 'Corel16k003',
            'rcv1subset1', 'rcv1subset5']

algorithms = ['2br']

l = log.Log('2BR')

ev = Evaluate()

for dataset in datasets:
    for algorithm in algorithms:

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

        m = int(math.floor(np.size(x, axis=0) / fold))
        indices = np.reshape(random.sample(range(m * fold), m * fold), [fold, m])

        labels = y_label

        # 第k次检验,选择训练集、测试集和验证集
        for k in range(fold):
            # 日志log文档记录点
            behave = 'pre-processing'
            l.write_format_log(behave, dataset, algorithm, fold=k)

            v = 4  # 3+1 3份用于确定优化顺序，1份用于确定优化截止点
            group_tr = list(range(fold))
            group_tr.remove(k)
            group_te = k

            indice_tr = np.reshape(indices[group_tr], [m * (fold - 1)])
            indice_te = np.reshape(indices[group_te], [m])

            x_tr = x[indice_tr]
            y_tr = y[indice_tr]
            x_te = x[indice_te]
            y_te = y[indice_te]

            # -------------------------------- 选择使用的前置算法 ------------------------------------
            # 在这里调用所查到的算法代码，其输入训练数据x_tr, y_tr和测试集的x_te，输出为算法预测结果y_
            # y_ = function(x_tr, y_tr, x_te)
            # 注意！y_te不能够输入至算法内！

            # 日志log文档记录点
            behave = 'original training'
            l.write_format_log(behave, dataset, algorithm, fold=k)

            y_te_ = pred.predictor(algorithm, x_tr, y_tr, x_te)

            path = '../results/(dataset=%s,algorithm=%s,fold=%d) y_std.csv' % (dataset, algorithm, k)
            rf.write_csv(path, np.vstack([labels, y_te]))

            path = '../results/(dataset=%s,algorithm=%s,fold=%d) y_ori.csv' % (dataset, algorithm, k)
            rf.write_csv(path, np.vstack([labels, y_te_]))

            path = '../results/analysis/(dataset=%s,algorithm=%s) values.csv' % (dataset, algorithm)
            eval_te = ev.evaluator(y_te_, y_te)
            names = ['hamming_loss', 'accuracy', 'exact_match', 'f1', 'macro_f1', 'micro_f1']
            rf.write_csv(path, [[eval_te[name] for name in names]], 'a')
