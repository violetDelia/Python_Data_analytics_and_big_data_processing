import pandas as pd
import numpy as np

series1 = {"name": pd.Series(["Wilson", "Bruce", "Chelsea"]),
           "math_score": pd.Series([98, 88, 91]),
           "en_score": pd.Series([92, 68, 94]),
           "term": pd.Series(["第一学期", "第一学期", "第一学期"])}

series2 = {"name": pd.Series(["Wilson", "Bruce", "Chelsea"]),
           "math_score": pd.Series([90, 68, 75]),
           "en_score": pd.Series([95, 99, 82]),
           "term": pd.Series(["第二学期", "第二学期", "第二学期"])}

df1 = pd.DataFrame(series1)
df2 = pd.DataFrame(series2)
df3 = df1.merge(df2, on=["name"])
print(df3)

