# -*- coding: UTF-8 -*-
class Person:
    def __init__(self, ID, name, age, height, weight, address):
        self._ID = ID
        self._name = name
        self._age = age
        self._height = height
        self._weight = weight
        self._address = address

p1 = Person("18888888", "Obama", 20, 150, 52, "Beijing Wangfujing")
print("p1的信息：\n", p1.__dict__)
print()
p2 = Person("19999999", "Trump", 40, 180, 83, "Washington")
print("p2的信息：\n", p2.__dict__)
print()
property_list = ["_ID", "_age", "_address"]
def set_property():
    for i in property_list:
        '''
        hasattr()用于检测实例p2中有没有i属性
        '''
        if hasattr(p2, i):
            val = getattr(p1, i)
            '''
            setattr()用于给实例p2的i属性赋值val
            '''
            setattr(p2, i, val)

    print("p2修改后的信息：", p2.__dict__)

set_property()

