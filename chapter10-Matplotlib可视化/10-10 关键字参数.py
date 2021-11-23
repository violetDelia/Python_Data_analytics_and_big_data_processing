import matplotlib.pyplot as plt
import numpy as np

data = {"a": np.arange(20),
        "b": np.random.randint(0, 20, 20)}
print(data["a"])
print(data["b"])
plt.scatter("a", "b", data=data)
plt.xlabel("x 序列", fontproperties="SimHei")
plt.ylabel("y 序列", fontproperties="SimHei")
plt.show()

