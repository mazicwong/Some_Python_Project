import numpy
import numpy as np

### 引用mnist数据
from keras.datasets import mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1] * X_train.shape[2])
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1] * X_test.shape[2])
Y_train = (numpy.arange(10) == y_train[:, None]).astype(int) # 把index转换为一个one hot的矩阵
Y_test = (numpy.arange(10) == y_test[:, None]).astype(int)  # Y_test.shape

### reshape函数
a = np.array([1,2,3])
print(a.shape) #(3,)
a = a.reshape((1,-1))  # (1,3)
print(a.shape) #(1,3) 1*3矩阵

a = np.array([1,2,3,4,5,6])
print(a.shape)
a = a.reshape((2,-1))
print(a.shape) #(2,3) 2*3矩阵(二维数组)

### full
a = np.full((3,3),0)

### eye
a = np.eye(3) #单位矩阵

### random.random
a = np.random.random((3,4))

### indexing
a = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])
a[-2:, 1:3] #array[[6,7][10,11]]

### arange
np.arange(3,7)

# 数学运算
a = np.array([[1,2],
              [3,4]])
b = np.array([[5,6],
              [7,8]])
a+b # np.add(a,b)
a*b #对应元素相乘
a.dot(b)  # 真正的矩阵乘法
np.dot(a,b)

# 常用函数
np.sum(a)         # 所有元素求和
np.sum(a,axis=0)  # 每一列求和
np.sum(a,axis=1)  # 每一行求和

np.mean(a)        # 元素和的均值
np.mean(a,axis=0) # 每一列的均值

np.random.uniform(3,4) # 产生[3,4]随机小数

a.T #矩阵转置