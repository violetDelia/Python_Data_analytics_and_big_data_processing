a = "Hello World"
print("a的内存地址是：", id(a))
b = a
print("b的内存地址是：", id(b))
a = "Hello Python"
print("a的内存地址是：", id(a))
del a
'''
a变量已经不存在，因此报错
'''
print("a的内存地址是：", id(a))
