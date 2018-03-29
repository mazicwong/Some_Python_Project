# 创建交互式会话
import tensorflow as tf

sess = tf.InteractiveSession()
a = tf.Variable([1.0,2.0])    # 变量数组
b = tf.constant([3.0,4.0])    # 常量数组
sess.run(tf.global_variables_initializer())
ans = tf.add(a,b)
print(ans.eval())