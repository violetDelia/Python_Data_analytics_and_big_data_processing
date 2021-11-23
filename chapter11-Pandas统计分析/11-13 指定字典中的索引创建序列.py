import pandas as pd

init_data = {"name": "Ivy", "age": 10}
'''
没有该索引为NaN
'''
data = pd.Series(init_data, index=["name", "age1"])
print(data)
