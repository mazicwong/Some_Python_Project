# SVM

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
def load_datasets(feature_paths, label_paths):
    feature = np.ndarray(shape=(0,41))  # 列41,特征维度41 (想象成一个41维的列向量)
    label = np.ndarray(shape=(0,1))     # 列1,标签维度1
    for file in feature_paths:
        file = '~/Downloads/mooc课程数据/课程数据/分类/dataset/'+file
        df = pd.read_table(file, delimiter=',', na_values='?', header=None)
        imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
        imp.fit(df)
        df = imp.transform(df)
        feature = np.concatenate((feature, df))

    for file in label_paths:
        file = '~/Downloads/mooc课程数据/课程数据/分类/dataset/' + file
        df = pd.read_table(file, header=None)
        label = np.concatenate((label, df))

    label = np.ravel(label)
    return feature, label


if __name__ == '__main__':
    ''' 数据路径 '''
    featurePaths = ['A/A.feature', 'B/B.feature', 'C/C.feature', 'D/D.feature', 'E/E.feature']
    labelPaths = ['A/A.label', 'B/B.label', 'C/C.label', 'D/D.label', 'E/E.label']
    ''' 读入数据  '''
    x_train, y_train = load_datasets(featurePaths[:4], labelPaths[:4])
    x_test, y_test = load_datasets(featurePaths[4:], labelPaths[4:])
    x_train, x_, y_train, y_ = train_test_split(x_train, y_train, test_size=0.0)

    print('Start training knn')
    knn = KNeighborsClassifier().fit(x_train, y_train)
    print('Training done')
    answer_knn = knn.predict(x_test)
    print('Prediction done')

    print('Start training DT')
    dt = DecisionTreeClassifier().fit(x_train, y_train)
    print('Training done')
    answer_dt = dt.predict(x_test)
    print('Prediction done')

    print('Start training Bayes')
    gnb = GaussianNB().fit(x_train, y_train)
    print('Training done')
    answer_gnb = gnb.predict(x_test)
    print('Prediction done')

    print('\n\nThe classification report for knn:')
    print(classification_report(y_test, answer_knn))
    print('\n\nThe classification report for DT:')
    print(classification_report(y_test, answer_dt))
    print('\n\nThe classification report for Bayes:')
    print(classification_report(y_test, answer_gnb))