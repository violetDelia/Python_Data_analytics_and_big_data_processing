import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).reshape(2, 3, 2)
for row in a:
    print("当前行数据：")
    print(row)

for el in a.flat:
    print("当前元素：", el)

for row in a:
    for col in row:
        print("当前数据：")
        print(col) 

	
	