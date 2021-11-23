import numpy as np

file = "chapter9-NumPy数值计算\订单信息.csv"
order_info = np.loadtxt(file, delimiter=",")
print("创建销售信息的数组：")
print(order_info)
print("获取总销售额：", np.sum(order_info))
print("获取每个商品总销售额：", np.sum(order_info, axis=1))
print("获取每个商品平均销售额：", np.mean(order_info, axis=1))
print("获取大于100的数据：")
tmp = order_info > 100
print(order_info[tmp])


