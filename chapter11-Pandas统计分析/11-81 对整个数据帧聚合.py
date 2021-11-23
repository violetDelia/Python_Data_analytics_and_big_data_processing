import pandas as pd
import numpy as np

series1 = {"math_score": pd.Series([98, 88, 80]),
           "en_score": pd.Series([70, 68, 85]),
           "sum_score": pd.Series([168, 156, 165])}

df1 = pd.DataFrame(series1)
print(df1)
print(df1.aggregate(np.sum))
print(df1.aggregate(np.mean))
