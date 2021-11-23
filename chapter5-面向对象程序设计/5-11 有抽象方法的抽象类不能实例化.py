# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod


'''
拥有抽象方法的抽象类不能被实例化
'''

class Poultry(metaclass=ABCMeta):
    colour = "白色"
    num = "num1"

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def run(self):
        pass

try:
    poultry = Poultry()
    print("对象地址：", id(poultry))
    print("对象类型：", type(poultry))
except Exception as e:
    print(e)


