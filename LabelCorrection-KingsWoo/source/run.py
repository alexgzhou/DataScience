# coding:utf-8

import main

fold = 10
datasets = ['rcv1subset1', 'rcv1subset5', 'yeast', 'scene', 'corel5k',
            'Corel16k001', 'Corel16k002', 'Corel16k003',  'CAL500',
            'emotions', 'enron', 'genbase', 'medical']

algorithms = ['mlknn', 'ecc']

for dataset in datasets:
    for algorithm in algorithms:
        main.single_training_process(algorithm, dataset, fold)
