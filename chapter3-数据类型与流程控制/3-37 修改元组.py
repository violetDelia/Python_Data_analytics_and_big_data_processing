# -*- coding: UTF-8 -*-

'''
元组的元素不能直接修改
'''
tuple1 = ("hello", "world", "python", "spark", "hadoop")
try:
    tuple1[0] = "hello world"
except Exception as e:
    print("修改元组数据触发异常：", e)

tuple4 = ([1, 2], [3, 4], [5, 6, 7, 8], [9, 10, 11, 12, 13, 14])
tuple4[1][0] = ("hello", "world")
print("修改元组中的列表：", tuple4)



