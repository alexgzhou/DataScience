# coding: utf-8

import mat4py as mp
import evaluate as ev
import numpy as np
import readfile as rf
import log
import appendix as ap

datasets = ['yeast',  'scene', 'CAL500', 'emotions', 'enron', 'genbase', 'medical',
            'corel5k', 'Corel16k001', 'Corel16k002', 'Corel16k003',
            'rcv1subset1', 'rcv1subset5']

algorithms = ['LPLC']

l = log.Log('LPLC')

for dataset in datasets:
    for algorithm in algorithms:
        file = mp.loadmat('../LPLC_result/%s.mat' % dataset)
        for k in range(10):

            path_label = '../datasets/%s/%s.xml' % (dataset, dataset)
            param = {
                'fold': k,
                'algorithm': algorithm,
                'dataset': dataset,
                'labels': rf.read_labels_from_xml(path_label)
                }

            y_tr = file['save_fold_%d_y_tr' % (k + 1)]
            y_te = file['save_fold_%d_y_te' % (k + 1)]
            y_te_ = file['save_fold_%d_y_te_' % (k + 1)]
            y_va = file['save_fold_%d_y_va' % (k + 1)]
            y_va_ = file['save_fold_%d_y_va_' % (k + 1)]

            # 日志log文档记录点
            behave = 'appendix training'
            l.write_format_log(behave, dataset, algorithm, fold=k)

            ap.regression_method(y_tr, y_va, y_va_, y_te, y_te_, param)

