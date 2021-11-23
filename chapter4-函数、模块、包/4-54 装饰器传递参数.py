# -*- coding: UTF-8 -*-
import datetime
import time

count = 5

def log_comment(content):
    def log(func):
        def decorate(*args, **kw):
            print("被装饰的函数名称:%s,当前业务是：%s" % (func.__name__,content))
            time1 = datetime.datetime.now()
            func(*args, **kw)
            time2 = datetime.datetime.now()
            print("循环耗时：", (time2 - time1).seconds)

        return decorate

    return log

@log_comment("测试循环耗时")
def decorated():
    print("decorated函数被装饰后,函数名为：", decorated.__name__)
    for i in range(count):
        time.sleep(1)

decorated()


