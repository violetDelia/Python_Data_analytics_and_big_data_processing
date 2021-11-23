# -*- coding: UTF-8 -*-

'''
Global()可以获取当前的全局变量
'''

def fun():
    global var1, var2, var3
    var1 = 100
    var2 = 200
    var3 = 300
    var4 = 400
    print("fun中的局部变量var1：%s，var2：%s，var3：%s，var4：%s：" % (var1, var2, var3, var4))

fun()
print("全局变量var1：%s，var2：%s，var3：%s：" % (var1, var2, var3))
try:
    print("输出变量var4：%s" % (var4))
except Exception as e:
    print(e)


