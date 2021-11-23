# -*- coding: UTF-8 -*-
import time, threading

def get_data_from_db():
    print("当前线程名称：{0}".format(threading.current_thread().name))
    for i in range(5):
        time.sleep(1)

    print("{0} 线程执行完毕！".format(threading.current_thread().name))


if __name__ == "__main__":
    print("{0} 线程开始运行".format(threading.current_thread().name))
    thread = threading.Thread(target=get_data_from_db, name="新线程")
    thread.start()
    '''
    joint()表示当前线程结束才能继续执行
    '''
    thread.join()
    print("{0} 线程执行完毕！".format(threading.current_thread().name))

	
	