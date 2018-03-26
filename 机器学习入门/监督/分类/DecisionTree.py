# 决策树
# 参数
# criterion: gini(基尼系数)/entropy(信息增益)
# max_features: 节点处分裂时,从多少个特征选择最优特征,默认使用所有特征个数

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

clf = DecisionTreeClassifier() #默认gini
iris = load_iris()
data = iris.data      # 数据
target = iris.target  # 标签作为目标结构

#训练
# 10则交叉验证
cross_val_score(clf, iris.data, iris.target, cv=10)
clf.fit(X,y)

#预测
print(clf.predict(X))