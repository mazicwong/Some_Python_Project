# Deep Q-Network
# 深度强化学习进行Flappy Bird游戏的训练
# tensorflow + pygame +cv2

import tensorflow as tf
import numpy as np
from collections import deque
import random
import sys
sys.path.append('/home/mazic/Downloads/FlappyBirdClone')
# import wrapped_flappy_bird as game
import cv2
import pygame

GAME = 'bird'
ACTIONS = 2
GAMMA = 0.99
OBSERVE = 10000.
EXPLORE = 3000000.
FINAL_EPSILON = 0.0001
INITIAL_EPSILON = 0.0001
REPLAY_MEMORY = 50000
BATCH = 32
FRAME_PER_ACTION = 1

mat1 = tf.constant([[3.,3.]])    # 1*2矩阵
mat2 = tf.constant([[2.],[2.]])  # 2*1矩阵
product = tf.matmul(mat1,mat2)   # 创建op执行两个矩阵的乘法
sess = tf.Session()              # 在Session中执行图
res = sess.run(product)          # 在图中执行op操作

print(res)
sess.close()
