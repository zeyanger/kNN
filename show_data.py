#！/usr/bin/env.python
# _*_ coding:utf-8 _*_

import matplotlib
from matplotlib import pyplot as plt
import numpy as np

import functions

dating_datamat, dating_labels = functions.file2matrix('datingTestSet2.txt')

# 设置图的大小，添加子图
fig = plt.figure()
ax = fig.add_subplot(111)

ax.scatter(dating_datamat[:, 0], dating_datamat[:, 1],
           10.0 * np.array(dating_labels),
           np.array(dating_labels))


plt.title('dating classify', fontsize=24)
plt.xlabel('distance of flight', fontsize=20, color='b')
plt.ylabel('time percent of playing game', fontsize=20, color='b')
plt.show()

