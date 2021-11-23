import numpy as np

a = np.floor(10 * np.random.random((2, 20)))
print(a)
print("水平方向拆分：")
data = np.hsplit(a, 2)
for item in data:
    print(item)
print("水平方向拆分：")
data1 = np.vsplit(data[1], 2)
for item in data1:
    print(item)
print("拆分成指定的数组")
data2 = np.array_split(data,1)
for item in data2:
    print(item)
	
	