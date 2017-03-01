#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# this is a simple PYTHON bubble sort

array = [1, 2, 3, 5, 4, 6, 9, 8, 7]
for i in range(len(array) - 1, 0, -1):
    for j in range(0, i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)
