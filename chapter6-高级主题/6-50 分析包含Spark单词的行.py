
from multiprocessing import Process, Queue
import time

def set_data(q):
    file = open("chapter6-高级主题//readme1.md", encoding='UTF-8')
    for line in file:
        if "spark" in line:
            q.put(1)
            time.sleep(1)

def get_data(q):
    count = 0
    while True:
        value = q.get(True)
        count += value
        print("包含 Spark 的行：", count)

if __name__ == "__main__":
    que = Queue()
    process1 = Process(target=set_data, args=(que,))
    process2 = Process(target=get_data, args=(que,))
    process1.start()
    process2.start()
    process1.join()

	
	