# -*- coding: UTF-8 -*-

class WildGoose:
    def fly(self):
        print("WildGoose中的方法")

'''
eval()将字符串参数转化为代码
'''
wild_goose = eval("WildGoose()")
'''
getattr()获取实例的属性
'''
fly = getattr(wild_goose, "fly")
fly()


