from abc import ABCMeta, abstractmethod

class Chicken(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def fly(self):
        print("小鸡 {0} 飞起来了".format(self._name))

try:
    chicken1 = Chicken("Num1")
    chicken1.fly()
except Exception as e:
    print(e)


