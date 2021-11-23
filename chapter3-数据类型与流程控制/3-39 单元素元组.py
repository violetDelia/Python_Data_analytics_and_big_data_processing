# -*- coding: UTF-8 -*-
tmp_str = "123"

'''
创建单元素元组需要加入一个逗号.
'''
tmp_list = [tmp_str]
print("单元素列表：", type(tmp_list))

tmp_tuple = (tmp_str)
print("单元素元组：", type(tmp_tuple))

tmp_tuple = (tmp_str,)
print("单元素元组：", type(tmp_tuple))

tmp_tuple = (tmp_list)
print("单元素元组：", type(tmp_tuple))

tmp_tuple = (tmp_list,)
print("单元素元组：", type(tmp_tuple))


