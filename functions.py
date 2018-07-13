#！/usr/bin/env.python
# _*_ coding:utf-8 _*_

import numpy as np
import operator  # 运算符模块


# 数据解析
def file2matrix(filename):
    with open(filename) as f:
        array_lines = f.readlines()    # 返回一个list对象，每行占一个元素
        num_of_lines = len(array_lines)
        returnMat = np.zeros((num_of_lines, 3))

        class_label_vector = []
        index = 0

        for line in array_lines:
            line = line.strip()
            list_from_line = line.split('\t')
            returnMat[index, :] = list_from_line[0:3]
            class_label_vector.append(int(list_from_line[-1]))
            index += 1

        return returnMat, class_label_vector


# 数值均一化
def auto_norm(dataset):
    min = dataset.min(0)
    max = dataset.max(0)
    norm_dataset = np.zeros(np.shape(dataset))
    m = dataset.shape[0]
    norm_dataset = dataset - np.tile(min, (m, 1))
    norm_dataset = norm_dataset/np.tile(max - min, (m, 1))

    return norm_dataset, max-min, min


