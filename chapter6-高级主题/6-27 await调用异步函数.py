# -*- coding: UTF-8 -*-

import time

async def get_data_from_db(counter):
    data = []
    print("参数counter：", counter)
    for i in range(counter):
        time.sleep(1)
        data.append(i)
    return data

'''
在一个协程中可以用await阻塞自己调用另一个协程
'''
async def await_get_data(counter):
    result = await get_data_from_db(counter)
    return result

try:
    coroutine_obj = await_get_data(5)
    coroutine_obj.send(None)
except StopIteration as e:
    print(e.value)

	
	