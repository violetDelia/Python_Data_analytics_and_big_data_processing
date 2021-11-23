from abc import ABCMeta, abstractmethod


class Chicken:
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def fly(self):
        print("小鸡 {0} 飞起来了".format(self._name))


chicken1 = Chicken("Num1")
chicken1.fly()

chicken2 = Chicken("Num2")
chicken2.fly()


