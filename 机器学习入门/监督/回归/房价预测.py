# 数据集: 面积,价格;  进行回归
# 已知面积,预测房屋价格

import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np


# 数据预处理
data_x = []
data_y = []
f = open('prices.txt','r')
lines = f.readlines()
for line in lines:
    items = line.strip().split(',')
    # print ("%d %d " % (int(items[0]),int(items[1])))
    data_x.append(int(items[0]))
    data_y.append(int(items[1]))
# plt.scatter(data_x,data_y,c='r')
# plt.plot(x, linear.predict(x), c='b')
# plt.xlabel('Area')
# plt.ylabel('Price')
# plt.show()

length = len(data_x)
data_x = np.array(data_x).reshape([length,1]) # 转化为二维数组(回归函数参数需要)
data_y = np.array(data_y)
minx = min(data_x)
maxx = max(data_x)
print(minx , '  ', maxx)
x = np.arange(minx,maxx).reshape([-1,1]) # 等差数列

# 训练
linear = linear_model.LinearRegression()
linear.fit(data_x, data_y)

# 回归方程系数,截距
print('Coefficient:', linear.coef_, ';  intercept:', linear.intercept_)

plt.scatter(data_x,data_y,c='r')
plt.plot(x, linear.predict(x), c='b')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()