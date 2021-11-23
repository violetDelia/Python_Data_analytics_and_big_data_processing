# -*- coding: UTF-8 -*-
import time


async def get_data_from_db(counter):
    data = []
    print("参数counter：", counter)
    for i in range(counter):
        time.sleep(1)
        data.append(i)
    return data

coroutine_obj = get_data_from_db(5)
print("异步函数返回值：",coroutine_obj)
try:
    '''
    send()之后才会执行
    '''
    coroutine_obj.send(None)
except Exception as e:
    print(e)
