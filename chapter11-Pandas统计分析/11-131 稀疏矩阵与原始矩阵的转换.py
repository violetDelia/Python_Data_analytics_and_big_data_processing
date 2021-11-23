import pandas as pd
import numpy as np

series1 = {"name": pd.Series(["Wilson", "Bruce", "Chelsea", "Warren", "Ivy"]),
           "math_score": pd.Series([198, np.nan, np.nan, np.nan, 74]),
           "en_score": pd.Series([92, np.nan, 94, np.nan, np.nan]),
           "term": pd.Series(["第一学期", "第一学期", "第一学期", "第一学期", "第一学期"])}

df1 = pd.DataFrame(series1)
'''
该功能被移除
'''
sparse = df1.to_sparse()
print(sparse.density)
df1 = sparse.to_dense()


