# 做矩阵乘法
import tensorflow as tf

mat1 = tf.constant([[3.,3.]])    # 1*2矩阵
mat2 = tf.constant([[2.],[2.]])  # 2*1矩阵
product = tf.matmul(mat1,mat2)   # 创建op执行两个矩阵的乘法

sess = tf.Session()              # 在Session中执行图
ans = sess.run(product)          # 在图中执行op操作

print(ans)
sess.close()