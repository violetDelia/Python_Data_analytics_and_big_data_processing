a = []
b = []
a.extend(b)
b.extend(a)
del a
del b
'''
详见：
    标记-清除：在各个活动的对象图中寻找到不处于活动状态（没有指向改对象的路径）的对象，并清除他。
        常用于处理容器对象，但有较大的性能消耗
    分代回收：
'''
