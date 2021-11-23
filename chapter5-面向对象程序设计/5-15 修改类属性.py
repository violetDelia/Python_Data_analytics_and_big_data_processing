# -*- coding: UTF-8 -*-

'''
类属性修改会影响该类的所有实例
'''
class Chicken:
    colour = "白色"
    num = "num1"

chicken1 = Chicken()
chicken2 = Chicken()
print("chicken1 colour 地址：", id(chicken1.colour))
print("chicken1 num 地址：", id(chicken1.num))
print()
print("chicken2 colour 地址：", id(chicken2.colour))
print("chicken2 num 地址：", id(chicken2.num))
print()
Chicken.colour = "黄色"
Chicken.num = "Num2"
print("实例 chicken1 访问修改后的属性 colour：", chicken1.colour)
print("实例 chicken1 访问修改后的属性 num：", chicken1.num)
print()
print("实例 chicken2 访问修改后的属性 colour：", chicken2.colour)
print("实例 chicken2 访问修改后的属性 num：", chicken2.num)


