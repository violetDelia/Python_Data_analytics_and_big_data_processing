# -*- coding: UTF-8 -*-
import datetime
import time

'''
扩展功能又不修改原来的代码.
'''
count = 5

def loop():
    time1 = datetime.datetime.now()
    for i in range(count):
        time.sleep(1)
    time2 = datetime.datetime.now()
    print("循环耗时：", (time2 - time1).seconds)

def log(func):
    def decorate(*args, **kw):
        print("被装饰的函数名称:", func.__name__)
        time1 = datetime.datetime.now()
        func(*args, **kw)
        time2 = datetime.datetime.now()
        print("循环耗时：", (time2 - time1).seconds)

    return decorate

@log
def decorated():
    print("decorated函数被装饰后,函数名为：",decorated.__name__)
    for i in range(count):
        time.sleep(1)

decorated()


