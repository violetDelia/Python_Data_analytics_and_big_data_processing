# -*- coding: UTF-8 -*-
tmp_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data = [i for i in tmp_list if i % 2 == 0]
print("使用推导式获取偶数：", data)

data = (i for i in tmp_list if i % 2 == 0)
print("[]变为()得到生成器：", data)


print("获取生成器中第1个值：", next(data))
print("获取生成器中第2个值：", data.__next__())
print("获取生成器中第1个值：", next(data))
print("获取生成器中第1个值：", next(data))
print("获取生成器中第1个值：", next(data))
try:
    print("获取生成器中第1个值：", next(data))
except Exception as e:
    print(e)

