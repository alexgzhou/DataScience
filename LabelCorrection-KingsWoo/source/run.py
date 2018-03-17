# coding:utf-8

import main
import time
import readfile as rf

fold = 10
datasets = ['rcv1subset1', 'rcv1subset5', 'yeast', 'scene', 'corel5k',
            'Corel16k001', 'Corel16k002', 'Corel16k003',  'CAL500',
            'emotions', 'enron', 'genbase', 'medical']

algorithms = ['mlknn', 'ecc', 'br']

time_stamp = time.strftime('%Y%m%d-%H.%M.%S')
file = open('../log/log-%s.txt' % time_stamp, 'w')

for dataset in datasets:
    for algorithm in algorithms:

        time_stamp = time.strftime('%Y%m%d-%H.%M.%S')
        file.write('start:  dataset=%s, algorithm=%s, time=%s\r\n' % (dataset, algorithm, time_stamp))

        main.single_training_process(algorithm, dataset, fold)

        time_stamp = time.strftime('%Y%m%d-%H.%M.%S')
        file.write('finish: dataset=%s, algorithm=%s, time=%s\r\n' % (dataset, algorithm, time_stamp))

