# -*- coding: UTF-8 -*-

val_int = 5555555555555555555555
print("将整形转为布尔型：", bool(val_int))
print("将整形(0)转为布尔型：", bool(0))
strs = "Hello,world"
print("将字符串转为布尔型：", bool(strs))
tmp_list = []
print("将空列表转为布尔型：", bool(tmp_list))
tmp_list = [1, 2, 3]
print("将列表转为布尔型：", bool(tmp_list))
val = True if 5 > 6 else False
print("将True或False转为布尔型：", bool(val))

'''
值为0或长度为0的容器转换成bool是fasle
'''
