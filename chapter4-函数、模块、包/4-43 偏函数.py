# -*- coding: UTF-8 -*-
from functools import partial

'''
既不想修改原函数,也不想创建新函数的时候
'''


def fun(a, b, c, d, e):
    return a + b + c + d + e

partial_fun = partial(fun, b=2, c=3, d=4, e=5)
result = partial_fun(10)
print("调用偏函数：", result)


