# coding:utf-8

from skmultilearn.adapt import MLkNN
from skmultilearn.problem_transform import ClassifierChain
import numpy as np
from scipy import sparse
import classifier_chain as cc
from sklearn import linear_model as lm
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


def predictor(algorithm, x_tr, y_tr, x_te, x_va=None):

    if algorithm == 'mlknn':
        return mlknn(x_tr, y_tr, x_te, x_va)
    elif algorithm == 'ecc':
        return ecc(x_tr, y_tr, x_te, x_va)
