# coding:utf-8

import main
import time
import readfile as rf

fold = 10

datasets = ['CAL500', 'emotions', 'enron', 'genbase', 'medical', 'scene', 'yeast',
            'corel5k', 'Corel16k001', 'Corel16k002', 'Corel16k003', 'rcv1subset1', 'rcv1subset5']

algorithms = ['br']

for algorithm in algorithms:
    for dataset in datasets:
        main.single_training_process(algorithm, dataset, fold)
