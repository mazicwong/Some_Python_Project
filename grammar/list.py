## list (the same as array)
nums = list(range(5))
squares = [x**2 for x in nums]
even_squares = [x**2 for x in nums if x%2==0]
print(squares)
print(even_squares)

