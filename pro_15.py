# Reduce function
from functools import reduce


def sum_num(a, b):
    return a+b
list_1 = reduce(sum_num, [1,5,7,3])
print(list_1)
