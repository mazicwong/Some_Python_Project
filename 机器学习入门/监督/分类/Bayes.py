# 朴素贝叶斯: 生成学习方法
# 学习联合概率分布,求后验概率分布
# 参数
# priors: 先验概率

import numpy as np
from sklearn.naive_bayes import GaussianNB #朴素bayes
X = np.array([[-1,-1], [-1,-1], [-3,-2], [1,1], [2,1], [3,2]])
y = np.array([1,1,1,2,2,2])

#训练
clf = GaussianNB(priors=None) #默认参数,创建分类器
clf.fit(X,y)

#预测
print(clf.predict([[-0.8,-1]]))
