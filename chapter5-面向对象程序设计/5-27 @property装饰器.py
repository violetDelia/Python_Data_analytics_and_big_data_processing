# -*- coding: UTF-8 -*-

class Chicken:
    def __init__(self):
        self._weight = None


    '''
    get方法的注解
    '''
    @property
    def weight(self):
        return self._weight


    '''
    set方法的注解
    '''
    @weight.setter
    def weight(self, val):
        if not isinstance(val, float):
            raise ValueError("请传递一个整数或浮点数！")
        if 0.1 > val or val > 12:
            raise ValueError("请确保参数范围在0.1到12之间！")

        self._weight = val

chicken = Chicken()
chicken.weight = 11.0
print("获取正常的weight：", chicken.weight)


