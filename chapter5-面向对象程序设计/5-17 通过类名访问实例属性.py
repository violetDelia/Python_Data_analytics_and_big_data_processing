# -*- coding: UTF-8 -*-


class Chicken:
    colour = "白色"
    num = "num1"

    def __init__(self, weight, price):
        self.weight = weight
        self.price = price


chicken1 = Chicken("2.5kg", "￥80")
chicken2 = Chicken("3kg", "￥100")
try:
    print(Chicken.price)
except Exception as e:
    print("通过类名访问实例属性，触发异常：", e)
print(chicken2.price)