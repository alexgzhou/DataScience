# coding:utf-8

import mat4py as mp
import csv
from xml.dom.minidom import parse
import xml.dom.minidom
import numpy as np


def read_mat(path):
    """
    读取来自.mat文件中的x,y数据
    :param path: 文件位置
    :return:x,y
    """
    data = mp.loadmat(path, False)
    x = data['xs']
    y = data['ys']
    return x, y


def read_labels_from_xml(path):
    """
    读取来自.xml文件中的labels列表
    :param path:文件位置
    :return:标签列表
    """
    dom = xml.dom.minidom.parse(path)
    collection = dom.documentElement.getElementsByTagName('label')
    labels = [each.getAttribute('name') for each in collection]
    return labels


def divide_csv(path, y_labels):
    """
    读取并分割来自.csv文件中的x,y数据至分别的文件内(~_x.csv,~_y.csv)
    :param path: 文件位置
    :param y_labels: y的标签名，csv文件中标签名存在于输入列表中的被认为是y数据，否则被认为是x数据
    :return: 当y_labels=None时，输出csv的直接读取结果,当输入y_labels时，分别输出x,y的读取结果
    """
    path_x = path.replace('.csv', '_x.csv')
    path_y = path.replace('.csv', '_y.csv')

    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        writer_x = csv.writer(open(path_x, 'w', newline=''))
        writer_y = csv.writer(open(path_y, 'w', newline=''))

        # 记录行数
        row_number = -1
        column_flag = []

        for row in reader:
            row_number += 1
            if row_number == 0:
                column_flag = np.array(['y' if column_name in y_labels else 'x' for column_name in row])
                title_x = np.array(row)[column_flag == 'x']
                title_y = np.array(row)[column_flag == 'y']
                writer_x.writerow(title_x)
                writer_y.writerow(title_y)

            else:
                raw = np.array(row, dtype=np.float32)
                x = raw[column_flag == 'x']
                y = raw[column_flag == 'y']
                writer_x.writerow(x)
                writer_y.writerow(y)

                if row_number % 100 == 0:
                    print('processing the %d row of file %s;' % (row_number, path))


def read_csv(path):
    """
    直接读取带标签行的csv文件
    :param path:
    :return: 标签列表和数据集
    """
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile)

        mat = [row for row in reader]
        title = mat[0]
        mat.remove(title)

        print('reading file %s;' % path)

        return np.array(mat, dtype=float), title


def write_csv(path, data, mode = 'w'):
    """
    write matrix into csv file
    :param path:
    :param data:
    :return:
    """
    with open(path, mode, newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)

