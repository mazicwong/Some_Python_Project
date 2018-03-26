import numpy as np

a = np.array([1,2,3])
print(type(a))  # all is same type
print(a.shape)  # the shape of an array is a tuple of integers giving the size of the array along each dimension.
print(a[0],a[1])

b = np.array([[1,2,3],[4,5,6]])
print(b.shape)

# functions to create array
c = np.zeros((2,2))
d = np.ones((1,2))
e = np.full((2,2), 7)
f = np.eye(2) # identity matrix
g = np.random.rand((2,2))  #random value    