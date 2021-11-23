# -*- coding: UTF-8 -*-


'''
__dict__返回实例的所有实例属性
'''
class WildGoose:

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
wild_goose.name = "鸿雁"
print("wild_goose对象的属性：", wild_goose.__dict__)
del wild_goose.name
print("wild_goose对象的属性：", wild_goose.__dict__)


