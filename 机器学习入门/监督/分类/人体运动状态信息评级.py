import numpy as np
import pandas as pd

from sklearn.preprocessing import Imputer #预处理模块
from sklearn.model_selection import train_test_split #生成数据模块
from sklearn.metrics import classification_report #评估模块
# 导入分类器模块
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

# 数据处理,传入特征列表,和标签列表
def load_dataset(feature_paths, label_paths):
    feature = np.ndarray(shape=(0,41))  # 列41,特征维度41 (想象成一个41维的列向量)
    label = np.ndarray(shape=(0,1))     # 列1,标签维度1