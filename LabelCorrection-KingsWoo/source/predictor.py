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
    pred = pt.BinaryRelevance(svm.LinearSVC())
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


def dbr(x_tr, y_tr, x_te, x_va=None):

    x_tr = np.array(x_tr)
    y_tr = np.int32(y_tr)

    pred_base = pt.BinaryRelevance(svm.LinearSVC())
    pred_meta = [svm.LinearSVC() for _ in range(np.size(y_tr, axis=1))]

    pred_base.fit(x_tr, y_tr)

    for i, pred in enumerate(pred_meta):
        x_add = np.copy(y_tr)
        x = np.hstack((x_tr, x_add[:, 0:i], x_add[:, i+1:pred_meta.__len__()+1]))
        y = y_tr[:, i]
        pred.fit(x, y)
        print('training meta %d' % i)

    n_te, n_va = 0, 0

    if x_va is not None:
        n_te = np.size(x_te, axis=0)
        n_va = np.size(x_va, axis=0)
        x_te = np.vstack((x_te, x_va))
    else:
        x_te = np.array(x_te)

    y_te_base = sparse.dok_matrix.toarray(pred_base.predict(x_te))
    y_te_ = np.zeros([np.size(x_te, axis=0), pred_meta.__len__()])
    for i, pred in enumerate(pred_meta):
        x_add = np.copy(y_te_base)
        x = np.hstack((x_te, x_add[:, 0:i], x_add[:, i+1:pred_meta.__len__()+1]))
        y_te_[:, i] = pred.predict(x)

    if x_va is not None:
        y_va_ = y_te_[n_va:, :]
        y_te_ = y_te_[0: n_te, :]
        return y_te_, y_va_
    else:
        return y_te_


def predictor(algorithm, x_tr, y_tr, x_te, x_va=None):

    # 该步用于矫正SVC输入为one class的情况

    n_te = np.size(x_te, axis=0)
    p = np.size(y_tr, axis=1)
    count_one = np.sum(y_tr, axis=0)
    non_zero_line = count_one != 0
    y_tr = y_tr[:, non_zero_line]

    if x_va is not None:

        n_va = np.size(x_va, axis=0)
        y_te_, y_va_ = selector(algorithm, x_tr, y_tr, x_te, x_va)
        y_te_out = np.zeros([n_te, p])
        y_te_out[:, non_zero_line] = y_te_
        y_va_out = np.zeros([n_va, p])
        y_va_out[:, non_zero_line] = y_va_
        return y_te_out, y_va_out

    else:

        y_te_ = selector(algorithm, x_tr, y_tr, x_te, x_va)
        y_te_out = np.zeros([n_te, p])
        y_te_out[:, non_zero_line] = y_te_
        return y_te_out


def selector(algorithm, x_tr, y_tr, x_te, x_va=None):

    if algorithm == 'mlknn':
        return mlknn(x_tr, y_tr, x_te, x_va)
    elif algorithm == 'ecc':
        return ecc(x_tr, y_tr, x_te, x_va)
    elif algorithm == 'br':
        return br(x_tr, y_tr, x_te, x_va)
    elif algorithm == 'dbr':
        return dbr(x_tr, y_tr, x_te, x_va)
