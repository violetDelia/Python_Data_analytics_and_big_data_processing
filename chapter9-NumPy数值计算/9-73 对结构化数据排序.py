import numpy as np

data = [("Wilson", 98, 70), ("Bruce", 60, 98), ("Ivy", 98, 92)]
dtype = [("name", "S10"), ("math_score", int), ("en_score", int)]
a = np.array(data, dtype=dtype)
b = np.sort(a,order=["math_score", "en_score"])
print("排序后的结果：")
print(b)


