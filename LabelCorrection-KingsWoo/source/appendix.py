# coding:utf-8
import numpy as np
from sklearn.svm import SVC
from evaluate import Evaluate
import readfile as rf


def regression_method(y_tr, y_va, y_va_, y_te, y_te_, param):
    """
    使用svm内核做回归与标签矫正
    :param y_tr: 训练集金标准
    :param y_va: 验证集金标准
    :param y_va_: 验证集矫正前结果
    :param y_te: 测试集金标准（仅在测试期需要）
    :param y_te_: 测试集矫正前结果
    :param param: 输入参数
    :return: 测试集矫正后结果
    """
# ------------------- 数据预处理，参数提取，初始化 ----------------------------
    y_dim = np.size(y_tr, axis=1)           # y空间的维度
    m_tr = np.size(y_tr, axis=0)            # 训练集的数量
    m_te = np.size(y_te, axis=0)            # 测试集的数量
    m_va = np.size(y_va, axis=0) - m_te     # 验证集（确定优化顺序）数量
    m_vc = m_te                             # 验证集（确定截止位置）数量

    y_tr = np.array(y_tr)
    y_vc = np.array(y_va)[m_va:m_va+m_vc, :]
    y_vc_ = np.array(y_va_)[m_va:m_va + m_vc, :]
    y_va = np.array(y_va)[0:m_va, :]
    y_va_ = np.array(y_va_)[0:m_va, :]
    y_te = np.array(y_te)
    y_te_ = np.array(y_te_)

    ev = Evaluate()
    best_pos_thres = np.ones([y_dim])
    best_neg_thres = np.zeros([y_dim])
    best_pos_impro = np.zeros([y_dim])
    best_neg_impro = np.zeros([y_dim])
    best_impro = np.zeros([y_dim])

    thres_pos_list = np.array(range(50, 100)) / 100
    thres_neg_list = np.array(range(50, 0, -1)) / 100

    classifiers = [None for _ in range(y_dim)]

    fold = param['fold']
    algorithm = param['algorithm']
    dataset = param['dataset']
    labels = param['labels']
# ----------------------- 输出y_te,y_te_ ----------0---------------------------
    path = '../results/(dataset=%s,algorithm=%s,fold=%d) y_std.csv' % (dataset, algorithm, fold)
    rf.write_csv(path, np.vstack([labels, y_te]))

    path = '../results/(dataset=%s,algorithm=%s,fold=%d) y_ori.csv' % (dataset, algorithm, fold)
    rf.write_csv(path, np.vstack([labels, y_te_]))

# ------------------ 获取每一维度标签矫正的效果 -------------------------------

    for dim in range(y_dim):

        print('appendix method: %d label in total %d labels, '
              'in the %d fold of dataset "%s" with primer algorithm "%s".'
              % (dim+1, y_dim, fold, dataset, algorithm))

        # 将第dim维的标签作为输出，其他标签作为输入
        dim_rest = list(range(y_dim))
        dim_rest.remove(dim)

        # 重组训练集金标准的标签，获得训练结果
        x = y_tr[:, dim_rest]
        y = y_tr[:, dim]
        if sum(y) == 0 or sum(y) == m_tr:
            continue

        classifier = SVC(probability=True, kernel='linear')
        classifier.fit(x, y)
        classifiers[dim] = classifier

        # 重组验证集的预测标签（y_va_），根据dim维度以外的标签获取该维度下该标签为1的概率
        x = y_va_[:, dim_rest]
        proba = classifier.predict_proba(x)[:, 1]

        y_va_adv = y_va_.copy()

        # 扫描确定更改所使用的正阈值（0 -> 1）
        for thres_pos in thres_pos_list:

            y = [1 if proba[i] > thres_pos else y_va_[i, dim] for i in range(m_va)]
            y_va_adv[:, dim] = y
            imp = ev.improve_function(y_va, y_va_, y_va_adv)
            if imp > best_pos_impro[dim]:
                best_pos_impro[dim] = imp
                best_pos_thres[dim] = thres_pos

        # 扫描确定更改所使用的负阈值（1 -> 0）
        for thres_neg in thres_neg_list:

            y = [0 if proba[i] < thres_neg else y_va_[i, dim] for i in range(m_va)]
            y_va_adv[:, dim] = y
            imp = ev.improve_function(y_va, y_va_, y_va_adv)
            if imp > best_neg_impro[dim]:
                best_neg_impro[dim] = imp
                best_neg_thres[dim] = thres_neg

        # 取最佳的正负阈值联合确定针对该标签的矫正效果（有时只用到一个阈值）
        thres_pos = best_pos_thres[dim]
        thres_neg = best_neg_thres[dim]
        y = y_va_[:, dim].copy()
        y = [1 if proba[i] > thres_pos else y[i] for i in range(m_va)]
        y = [0 if proba[i] < thres_neg else y[i] for i in range(m_va)]
        y_va_adv = y_va_.copy()
        y_va_adv[:, dim] = y

        best_impro[dim] = ev.improve_function(y_va, y_va_, y_va_adv)

# ------------------- 根据改进效果确定纠正的顺序 ----------------------------

    # 提取具有改进效果的维度
    impro_dim = best_impro.nonzero()
    impro_nonzero = best_impro[impro_dim]

    # 输出各个维度的改进效果
    path = '../results/(dataset=%s,algorithm=%s,fold=%d) impro.csv' % (dataset, algorithm, fold)
    rf.write_csv(path, [labels, best_impro])

    # 确定改进顺序以及用于改进的维度
    change_sequence = np.zeros(np.size(impro_dim))
    for i in range(np.size(impro_dim)):

        ind = np.argmax(impro_nonzero)
        dim = impro_dim[0][ind]
        change_sequence[i] = dim
        impro_nonzero[ind] = 0

# ------------------------ 对y_vc_进行纠正 ---------------------------------

    # values_list用于记录各参考量的数据情况
    values_list = [None for _ in range(np.size(change_sequence) + 1)]

    y_vc_ori = np.copy(y_vc_)
    y_vc_adv = np.copy(y_vc_)

    values_list[0] = ev.improve_function(y_vc, y_vc_ori, y_vc_adv)

    # 逐次纠正适合纠正的各个标签维度
    for ind in range(np.size(change_sequence)):

        dim = int(change_sequence[ind])
        dim_rest = list(range(y_dim))
        dim_rest.remove(dim)

        classifier = classifiers[dim]
        x = y_vc_adv[:, dim_rest]
        proba = classifier.predict_proba(x)[:, 1]
        thres_pos = best_pos_thres[dim]
        thres_neg = best_neg_thres[dim]
        y = y_vc_adv[:, dim]
        y = [1 if proba[i] > thres_pos else y[i] for i in range(m_vc)]
        y = [0 if proba[i] < thres_neg else y[i] for i in range(m_vc)]

        y_vc_adv[:, dim] = y

        values_list[ind+1] = ev.improve_function(y_vc, y_vc_ori, y_vc_adv)

    values_list[np.size(change_sequence)] = ev.improve_function(y_vc, y_vc_ori, y_vc_adv)
    # 确定截止位置
    cutoff_index = np.argmax(values_list)

# ------------------------ 对y_te_进行纠正 ---------------------------------

    # values_list用于记录各参考量的数据情况
    values_list = [None for _ in range(int(cutoff_index) + 1)]

    values_list[0] = ev.evaluator(y_te_, y_te)

    y_te_ori = np.copy(y_te_)
    y_te_adv = np.copy(y_te_)

    # 逐次纠正适合纠正的各个标签维度
    for ind in range(int(cutoff_index)):

        dim = int(change_sequence[ind])
        dim_rest = list(range(y_dim))
        dim_rest.remove(dim)

        classifier = classifiers[dim]
        x = y_te_adv[:, dim_rest]
        proba = classifier.predict_proba(x)[:, 1]
        thres_pos = best_pos_thres[dim]
        thres_neg = best_neg_thres[dim]
        y = y_te_adv[:, dim]
        y = [1 if proba[i] > thres_pos else y[i] for i in range(m_te)]
        y = [0 if proba[i] < thres_neg else y[i] for i in range(m_te)]

        y_te_adv[:, dim] = y

        values_list[ind+1] = ev.evaluator(y_te_adv, y_te)

    # 输出各评估指标的变化值
    path = '../results/(dataset=%s,algorithm=%s,fold=%d) values.csv' % (dataset, algorithm, fold)
    names = ['hamming_loss', 'accuracy', 'exact_match', 'f1', 'macro_f1', 'micro_f1']
    rf.write_csv(path, [names] + [[values_list[i][name] for name in names] for i in range(int(cutoff_index) + 1)])

    path = '../results/(dataset=%s,algorithm=%s,fold=%d) y_adv.csv' % (dataset, algorithm, fold)
    rf.write_csv(path, np.vstack([labels, y_te_]))

    path = '../results/analysis/(dataset=%s,algorithm=%s) values_ori.csv' % (dataset, algorithm)
    eval_ori = ev.evaluator(y_te_ori, y_te)
    rf.write_csv(path, [[eval_ori[name] for name in names]], 'a')

    path = '../results/analysis/(dataset=%s,algorithm=%s) values_adv.csv' % (dataset, algorithm)
    eval_adv = ev.evaluator(y_te_adv, y_te)
    rf.write_csv(path, [[eval_adv[name] for name in names]], 'a')
