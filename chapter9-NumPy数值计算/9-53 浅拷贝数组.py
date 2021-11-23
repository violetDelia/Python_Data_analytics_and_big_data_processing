import numpy as np

a = np.arange(16)
b = a.view()
if b is a:
    print("b和a是同一个对象")
else:
    print("b和a不是同一个对象")

print("判断b的base是否和a一样：", b.base is a)
print("判断b是否存在独立的一份数据拷贝：", b.flags.owndata)
print("修改b的形状：", (4, 4))
b.shape = 4, 4
print("输出a的形状", a.shape)
print("修改b的数据:b[0,2] = 100")
b[0, 2] = 100
print("查看a的数据：", a)
print("数组切片：")
c = a[1:3]
c[1] = 200
print("修改切片后的数组，然后查看对a的影响：", a)

