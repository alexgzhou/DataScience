# coding:utf-8

import main
import time
import readfile as rf

fold = 10
datasets = ['yeast', 'rcv1subset1', 'rcv1subset5',  'scene', 'corel5k',
            'Corel16k001', 'Corel16k002', 'Corel16k003',  'CAL500',
            'emotions', 'enron', 'genbase', 'medical']

algorithms = ['mlknn', 'ecc', 'br']

for dataset in datasets:
    for algorithm in algorithms:
        main.single_training_process(algorithm, dataset, fold)
