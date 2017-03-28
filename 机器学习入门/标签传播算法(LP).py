#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/25 11:28
# @Author  : mazicwong
# @File    : 标签传播算法(LP).py
import time
import math
import numpy as np
from label_propagation import labelPropagation


# show
def show(Mat_Label, labels, Mat_Unlabel, unlabel_data_labels):
    import matplotlib.pyplot as plt

    for i in range(Mat_Label.shape[0]):
        if int(labels[i]) == 0:
            plt.plot(Mat_Label[i, 0], Mat_Label[i, 1], 'Dr')
        elif int(labels[i]) == 1:
            plt.plot(Mat_Label[i, 0], Mat_Label[i, 1], 'Db')
        else:
            plt.plot(Mat_Label[i, 0], Mat_Label[i, 1], 'Dy')

    for i in range(Mat_Unlabel.shape[0]):
        if int(unlabel_data_labels[i]) == 0:
            plt.plot(Mat_Unlabel[i, 0], Mat_Unlabel[i, 1], 'or')
        elif int(unlabel_data_labels[i]) == 1:
            plt.plot(Mat_Unlabel[i, 0], Mat_Unlabel[i, 1], 'ob')
        else:
            plt.plot(Mat_Unlabel[i, 0], Mat_Unlabel[i, 1], 'oy')

    plt.xlabel('X1');
    plt.ylabel('X2')
    plt.xlim(0.0, 12.)
    plt.ylim(0.0, 12.)
    plt.show()


def loadCircleData(num_data):
    center = np.array([5.0, 5.0])
    radiu_inner = 2
    radiu_outer = 4
    num_inner = num_data / 3
    num_outer = num_data - num_inner

    data = []
    theta = 0.0
    for i in range(int(num_inner)):
        pho = (theta % 360) * math.pi / 180
        tmp = np.zeros(2, np.float32)
        tmp[0] = radiu_inner * math.cos(pho) + np.random.rand(1) + center[0]
        tmp[1] = radiu_inner * math.sin(pho) + np.random.rand(1) + center[1]
        data.append(tmp)
        theta += 2

    theta = 0.0
    for i in range(int(num_outer)):
        pho = (theta % 360) * math.pi / 180
        tmp = np.zeros(2, np.float32)
        tmp[0] = radiu_outer * math.cos(pho) + np.random.rand(1) + center[0]
        tmp[1] = radiu_outer * math.sin(pho) + np.random.rand(1) + center[1]
        data.append(tmp)
        theta += 1

    Mat_Label = np.zeros((2, 2), np.float32)
    Mat_Label[0] = center + np.array([-radiu_inner + 0.5, 0])
    Mat_Label[1] = center + np.array([-radiu_outer + 0.5, 0])
    labels = [0, 1]
    Mat_Unlabel = np.vstack(data)
    return Mat_Label, labels, Mat_Unlabel


def loadBandData(num_unlabel_samples):
    # Mat_Label = np.array([[5.0, 2.], [5.0, 8.0]])
    # labels = [0, 1]
    # Mat_Unlabel = np.array([[5.1, 2.], [5.0, 8.1]])

    Mat_Label = np.array([[5.0, 2.], [5.0, 8.0]])
    labels = [0, 1]
    num_dim = Mat_Label.shape[1]
    Mat_Unlabel = np.zeros((num_unlabel_samples, num_dim), np.float32)
    Mat_Unlabel[:num_unlabel_samples / 2, :] = (np.random.rand(num_unlabel_samples / 2, num_dim) - 0.5) * np.array(
        [3, 1]) + Mat_Label[0]
    Mat_Unlabel[num_unlabel_samples / 2: num_unlabel_samples, :] = (np.random.rand(num_unlabel_samples / 2,
                                                                                   num_dim) - 0.5) * np.array([3, 1]) + \
                                                                   Mat_Label[1]
    return Mat_Label, labels, Mat_Unlabel


# main function
if __name__ == "__main__":
    num_unlabel_samples = 800
    # Mat_Label, labels, Mat_Unlabel = loadBandData(num_unlabel_samples)
    Mat_Label, labels, Mat_Unlabel = loadCircleData(num_unlabel_samples)

    ## Notice: when use 'rbf' as our kernel, the choice of hyper parameter 'sigma' is very import! It should be
    ## chose according to your dataset, specific the distance of two data points. I think it should ensure that
    ## each point has about 10 knn or w_i,j is large enough. It also influence the speed of converge. So, may be
    ## 'knn' kernel is better!
    # unlabel_data_labels = labelPropagation(Mat_Label, Mat_Unlabel, labels, kernel_type = 'rbf', rbf_sigma = 0.2)
    unlabel_data_labels = labelPropagation(Mat_Label, Mat_Unlabel, labels, kernel_type='knn', knn_num_neighbors=10,
                                           max_iter=400)
    show(Mat_Label, labels, Mat_Unlabel, unlabel_data_labels)