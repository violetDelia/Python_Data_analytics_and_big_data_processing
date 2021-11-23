import pandas as pd
import numpy as np

series1 = {"name": pd.Series(["Wilson", "Bruce", "Chelsea"]),
           "age": pd.Series([15, 24, 19]),
           "math_score": pd.Series([98, 88, 80]),
           "en_score": pd.Series([70, 68, 85]),
           "sum_score": pd.Series([168, 156, 165])}

df1 = pd.DataFrame(series1)
'''
协方差用于衡量两个数据集间的整体误差,若结果大于0,那么表明这两个数据集是正相关的.
'''
data = df1["sum_score"].cov(df1["math_score"])
print(data)
