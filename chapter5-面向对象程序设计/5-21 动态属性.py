# -*- coding: UTF-8 -*-

class Chicken:
    colour = "白色"
    num = "num1"

Chicken.price = "￥150"
print("访问类上的动态属性：", Chicken.price)
chicken1 = Chicken()
print("类上的动态属性会传递给实例：", chicken1.price)
chicken2 = Chicken()
print("chicken1 和 chicken2 共享类上的动态属性 ：", chicken1.price == chicken2.price)
print()
chicken1.weight = "5kg"
chicken2.weight = "5kg"
print("chicken1 和 chicken2 实例上的动态属性是相互独立的：", chicken1.price != chicken2.weight)
print(id(chicken1.weight) ==id( chicken2.weight))

