# -*- coding: UTF-8 -*-

'''
类中只能有__slots__所记录的属性
'''
class WildGoose:
    __slots__ = ["direction", "colour", "weight"]

    def __init__(self):
        self.direction = []
        self.colour = "白色"
        self.weight = "12kg"

    def __call__(self, direction):
        self.direction.append(direction)
        print("大雁正往 {0} 方向飞".format(direction))

    def __str__(self):
        return str.join("--->", self.direction)


wild_goose = WildGoose()
print("wild_goose对象的属性：", wild_goose.__slots__)
try:
    wild_goose.name = "鸿雁"
except Exception as e:
    print(e)


