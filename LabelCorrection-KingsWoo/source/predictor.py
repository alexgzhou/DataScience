# coding:utf-8


from skmultilearn.adapt import MLkNN
from skmultilearn.problem_transform import ClassifierChain
import numpy as np
from scipy import sparse
import classifier_chain as cc
from sklearn import linear_model as lm
from sklearn import svm
from skmultilearn import problem_transform as pt


def mlknn(x_tr, y_tr, x_te, x_va=None):
    """
    mlknn
    :param x_tr:
    :param y_tr:
    :param x_te:
    :param x_va:
    :return:
    """
    pred = MLkNN(k=10, s=True)
    y_tr = np.int32(y_tr)
    pred.fit(x_tr, y_tr)

    if x_va is None:
        y_te_ = sparse.dok_matrix.toarray(pred.predict(x_te))
        return y_te_
    else:
        y_te_ = sparse.dok_matrix.toarray(pred.predict(x_te))
        y_va_ = sparse.dok_matrix.toarray(pred.predict(x_va))
        return y_te_, y_va_


def ecc(x_tr, y_tr, x_te, x_va=None):
    """
    ensemble classifier chain
    :param x_tr: 
    :param y_tr: 
    :param x_te: 
    :param x_va: 
    :return: 
    """
    base_classifier = lm.LogisticRegression(penalty="l1", C=1)
    pred = cc.ClassifierChainEnsemble(base_classifier)
    x_tr = np.array(x_tr)
    y_tr = np.int32(y_tr)
    x_te = np.array(x_te)
    pred.fit(x_tr, y_tr)
    if x_va is None:
        y_te_ = pred.predict(x_te)
        return y_te_
    else:
        y_te_ = pred.predict(x_te)
        y_va_ = pred.predict(x_va)
        return y_te_, y_va_


def br(x_tr, y_tr, x_te, x_va=None):
    """
    BR算法，基于SVC，使用默认参数
    :param x_tr:
    :param y_tr:
    :param x_te:
    :param x_va:
    :return:
    """
    pred = pt.BinaryRelevance(svm.SVC())
    x_tr = np.array(x_tr)
    y_tr = np.int32(y_tr)
    x_te = np.array(x_te)
    x_va = np.array(x_va)
    pred.fit(x_tr, y_tr)
    if x_va is None:
        y_te_ = sparse.dok_matrix.toarray(pred.predict(x_te))
        return y_te_
    else:
        y_te_ = sparse.dok_matrix.toarray(pred.predict(x_te))
        y_va_ = sparse.dok_matrix.toarray(pred.predict(x_va))
        return y_te_, y_va_


def predictor(algorithm, x_tr, y_tr, x_te, x_va=None):

    # 该步用于矫正SVC输入为one class的情况
    n_tr = np.size(y_tr, axis=0)
    n_te = np.size(x_te, axis=0)
    n_va = np.size(x_va, axis=0)
    p = np.size(y_tr, axis=1)
    count_one = np.sum(y_tr, axis=0)
    non_zero_line = count_one != 0

    y_tr_input = y_tr[:, non_zero_line]
    y_te_ = None
    y_va_ = None

    if x_va is not None:
        if algorithm == 'mlknn':
            y_te_, y_va_ = mlknn(x_tr, y_tr_input, x_te, x_va)
        elif algorithm == 'ecc':
            y_te_, y_va_ = ecc(x_tr, y_tr_input, x_te, x_va)
        elif algorithm == 'br':
            y_te_, y_va_ = br(x_tr, y_tr_input, x_te, x_va)
        y_te_out = np.zeros([n_te, p])
        y_te_out[:, non_zero_line] = y_te_
        y_va_out = np.zeros([n_va, p])
        y_va_out[:, non_zero_line] = y_va_
        return y_te_out, y_va_out
    else:
        if algorithm == 'mlknn':
            y_te_ = mlknn(x_tr, y_tr_input, x_te, x_va)
        elif algorithm == 'ecc':
            y_te_ = ecc(x_tr, y_tr_input, x_te, x_va)
        elif algorithm == 'br':
            y_te_ = br(x_tr, y_tr_input, x_te, x_va)
        y_te_out = np.zeros([n_te, p])
        y_te_out[:, non_zero_line] = y_te_
        return y_te_out
