# encoding=utf-8

import numpy as np
from scipy import stats
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import seaborn

def calc_statistics(x):
    n = x.shape[0]

    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0

    for i in x:
        m1 += i
        m2 += i**2
        m3 += i**3
        m4 += i**4

    m1 = m1 / n
    m2 = m2 / n
    m3 = m3 / n
    m4 = m4 / n

    sigma = math.sqrt(m2 - m1**2)
    skew = (m3 + 2 * m1**3 - 3 * m2 * m1) / sigma ** 3
    kurtosis = (m4 - 4 * m1 * m3 + 6 * m1 * m1 * m2 - 4 * m1**3 * m1 + m1**4) / sigma ** 4 - 3

    print('手动计算均值、标准差、偏度、峰度: ', m1, sigma, skew, kurtosis)

    m1 = np.mean(x, axis=0)
    sigma = np.std(x, axis=0)
    skew = stats.skew(x)
    kurtosis = stats.kurtosis(x)

    print('库函数计算均值、标准差、偏度、峰度: ', m1, sigma, skew, kurtosis)

    return m1, sigma, skew, kurtosis

if __name__ == '__main__':
    d = np.random.randn(10000)
    mu, sigma, skew, kurtosis = calc_statistics(d)

    mpl.rcParams['font.sans-serif'] = 'SimHei'
    mpl.rcParams['axes.unicode_minus'] = False
    plt.figure(num=1, facecolor='w')

