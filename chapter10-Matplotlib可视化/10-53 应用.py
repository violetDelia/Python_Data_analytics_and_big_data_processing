# !/usr/bin/python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["SimHei"]
file = "chapter10-Matplotlib可视化\销售数据.CSV"

# 处理数据
sales_info = np.loadtxt(file, dtype=np.str, delimiter=",")
sales_info_1 = sales_info[0:15, :]
sales_info_2 = sales_info[15:-1, :]

plt.figure()
plt.plot(sales_info_1[:, 0], sales_info_1[:, 2].astype(int), color="r", marker="o")
plt.plot(sales_info_2[:, 0], sales_info_2[:, 2].astype(int), color="g", marker="o")
plt.xticks(range(15), sales_info[range(15), 0], rotation=45)

# 2.分别计算门店总营业额，绘制饼图
sales_info_1_sum = sales_info_1[:, 2].astype(int).sum()
sales_info_2_sum = sales_info_2[:, 2].astype(int).sum()

pie_data = np.array([sales_info_1_sum, sales_info_2_sum])
mendian = ["门店1", "门店2"]
colors = ["red", "green"]
explode = [0.05, 0]
plt.pie(pie_data, explode=explode, colors=colors, labels=mendian, labeldistance=1.1,
        shadow=False, startangle=90, pctdistance=0.6)
plt.legend()
plt.show()

# 3.绘制条形图
date_list = sales_info_1[:, 0]
count = date_list.size
mendian_1 = sales_info_1[:, 2].astype(int)
print(mendian_1)
mendian_2 = sales_info_2[:, 2].astype(int)
print(mendian_2)

mendian_bar_1 = plt.bar(range(count), height=mendian_1, width=0.3, alpha=0.8, color="red", label="1店销售额")
mendian_bar_2 = plt.bar([i + 0.3 for i in range(count)], height=mendian_2, width=0.3, color="green", label="2店销售额")

plt.xticks([i + 0.15 for i in range(count)], date_list, rotation=45)
plt.xlabel("销售分析图")

plt.legend()

for m1 in mendian_bar_1:
    height = m1.get_height()
    plt.text(m1.get_x() + m1.get_width() / 2, height + 1, str(height), ha="center", va="bottom", rotation=90)
for m2 in mendian_bar_2:
    height = m2.get_height()
    plt.text(m2.get_x() + m2.get_width() / 2, height + 1, str(height), ha="center", va="bottom", rotation=90)

plt.show()
