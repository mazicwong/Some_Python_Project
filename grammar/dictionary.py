# dictionary (the same as map)

d = {'cat':'cute', 'dog':'furry'}
print(d['cat'])
for animal, type in d.items():
    print('A %s is %s' % (animal,type))


nums = list(range(5))
even_num_to_square = {x:x**2 for x in nums if x%2==0}
print(even_num_to_square)