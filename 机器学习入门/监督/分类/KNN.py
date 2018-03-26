# KNN,取与已知点最近的k个点,看占据哪个类别的比例多
# 参数
# n_neighbors:  K(默认5)
# weights: K个点对结果的影响权重(默认平均权重uniform)
# algorithm: 计算临近点方法(ball_tree,kd_tree,brute)
#

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

# 训练
X = [[0],[1],[2],[3]]
y = [0,0,1,1]
clf = KNeighborsClassifier(n_neighbors=3) # k=3
clf.fit(X,y) # 学习

# 使用
print(clf.predict([[1.1]]))
