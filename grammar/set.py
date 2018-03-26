# set (the same as set in cpp)

from math import sqrt

animals = {'cat', 'dog'}
print('cat' in animals)
animals.add('fish') # not append in list(array)

for idx,animal in enumerate(animals):
    print('#%d %s' % (idx,animal))

nums = {int(sqrt(x)) for x in range(30)}
print(nums)