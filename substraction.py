from functools import reduce
lis = [192, 12, 3, 53]
lis1 = reduce(lambda x, y: x - y, lis)
print(lis1)

lis2 = [1298, 23, 12, 5]
print((tuple(filter(lambda x: x % 2 == 0, lis2))))
