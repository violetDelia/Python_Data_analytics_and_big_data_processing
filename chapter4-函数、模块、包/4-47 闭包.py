# -*- coding: UTF-8 -*-

'''
在内部函数引用外部函数的变量
'''
def fun1():
    local_val = [0]

    def fun2():
        local_val[0] += 1
        return local_val[0]

    return fun2


count = fun1()
for i in range(10):
    print("第%s次调用计数器，记录值为：%s" % (i, count()))

	
	