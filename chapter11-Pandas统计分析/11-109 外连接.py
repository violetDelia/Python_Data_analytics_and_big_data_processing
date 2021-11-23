import pandas as pd
import numpy as np

series1 = {"name": pd.Series(["Wilson", "Bruce", "Chelsea", "Warren", "Ivy"]),
           "math_score": pd.Series([98, 88, 91, 94, 74]),
           "en_score": pd.Series([92, 68, 94, 78, 69]),
           "term": pd.Series(["第一学期", "第一学期", "第一学期", "第一学期", "第一学期"])}

series2 = {"name": pd.Series(["Wilson", "Bruce", "Chelsea", "Lucy", "Edith"]),
           "math_score": pd.Series([90, 68, 75, 83, 67]),
           "en_score": pd.Series([95, 99, 82, 89, 72]),
           "term": pd.Series(["第二学期", "第二学期", "第二学期", "第二学期", "第二学期"])}

df1 = pd.DataFrame(series1)
df2 = pd.DataFrame(series2)
df3 = df1.merge(df2, on="name", how="outer")
print(df3)


