# Copyright 2017 Chengkai Wu. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");

import numpy as np
import math

class Evaluate:

    def __init__(self):

        return

    @staticmethod
    def eval_hamming_loss(y, y_):
        return np.sum(np.not_equal(y, y_)) / np.size(y)

    @staticmethod
    def eval_accuracy(y, y_):
        y_and = np.sum(np.logical_and(y, y_), axis=1)
        y_or = np.sum(np.logical_or(y, y_), axis=1)
        # to avoid y_or == 0
        y_and = y_and
        y_or = y_or + np.equal(y_or, 0)

        return np.mean(y_and / y_or)

    @staticmethod
    def eval_exact_match(y, y_):
        dim = np.size(y, axis=1)
        cor = np.sum(list(map(lambda a, b: a == b, y, y_)), axis=1)

        return sum(dim == cor) / len(y)

    @staticmethod
    def eval_f1(y, y_):
        tp = np.sum(np.logical_and(y == 1, y_ == 1), axis=1)
        fp = np.sum(np.logical_and(y == 0, y_ == 1), axis=1)
        fn = np.sum(np.logical_and(y == 1, y_ == 0), axis=1)
        p = (tp + ((tp + fp) == 0)) / ((tp + fp) + ((tp + fp) == 0))
        r = (tp + ((tp + fn) == 0)) / ((tp + fn) + ((tp + fn) == 0))
        f1 = np.mean(2 * p * r / ((p + r) + np.equal(p + r, 0)))

        return f1

    @staticmethod
    def eval_macro_f1(y, y_):
        tp = np.sum(np.logical_and(y == 1, y_ == 1), axis=0)
        fp = np.sum(np.logical_and(y == 0, y_ == 1), axis=0)
        fn = np.sum(np.logical_and(y == 1, y_ == 0), axis=0)
        p = (tp + ((tp + fp) == 0)) / ((tp + fp) + ((tp + fp) == 0))
        r = (tp + ((tp + fn) == 0)) / ((tp + fn) + ((tp + fn) == 0))
        macro_f1 = np.mean((2 * p * r) / ((p + r) + np.equal(p + r, 0)))

        return macro_f1

    @staticmethod
    def eval_micro_f1(y, y_):
        return 2 * np.sum(np.logical_and(y, y_)) / (np.sum(y) + np.sum(y_))

    def evaluator(self, y, y_):

        return {
            'hamming_loss': self.eval_hamming_loss(y, y_),
            'accuracy': self.eval_accuracy(y, y_),
            'exact_match': self.eval_exact_match(y, y_),
            'f1': self.eval_f1(y, y_),
            'macro_f1': self.eval_macro_f1(y, y_),
            'micro_f1': self.eval_micro_f1(y, y_),
        }

    def improve_function(self, y, y_ori, y_adv):

        names = ['hamming_loss', 'accuracy', 'exact_match', 'f1', 'macro_f1', 'micro_f1']
        signs = [-1, 1, 1, 1, 1, 1]
        k = 1

        values_ori = self.evaluator(y, y_ori)
        values_adv = self.evaluator(y, y_adv)

        values_diff = [signs[i] * (values_adv[names[i]] - values_ori[names[i]]) for i in range(6)]
        values_base = [2 * math.sqrt(values_ori[names[i]] * (1 - values_ori[names[i]])) for i in range(6)]

        # return sum([- math.exp(-k * values_diff[i] / values_base[i]) + 1 for i in range(6)])
        return sum([- math.exp(-k * values_diff[i]) + 1 for i in range(6)])





