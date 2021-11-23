# -*- coding: UTF-8 -*-

def show(item1, item2):
    print("item1是：%s，item2是：%s" % (item1, item2))


def get(item1, item2):
    return item1 + 5, item2 + 6


print("参数解包：")
p1 = [7, 8]
show(*p1)
p2 = (9, 10)
show(*p2)
p3 = {"item1": 10, "item2": 11}

show(**p3)
print("返回值解包：")
a, b = get(**p3)
print("a是：%s，b是：%s" % (a, b))


