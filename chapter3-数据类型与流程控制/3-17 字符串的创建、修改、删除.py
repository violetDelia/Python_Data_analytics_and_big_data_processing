# -*- coding: UTF-8 -*-

a = "Hello"
print("原始字符串对象a：", id(a))
'''
生成新的字符串对象
'''
a = a + " World"
print("修改后的对象a：", id(a))
try:
    del a
    print(id(a))
except Exception as e:
    print("访问删除后的对象，触发异常：", e)

a = "Hello World"
print("这里相当于重新创建了对象a：", id(a))


