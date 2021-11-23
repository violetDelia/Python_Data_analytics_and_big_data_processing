import pandas as pd
import numpy as np

series1 = {"name": pd.Series(["Wilson", "Bruce", "Bruce", "Bruce"]),
           "math_score": pd.Series([98, 88, 94, 74]),
           "en_score": pd.Series([92, 68, 78, 69]),
           "school_year": pd.Series(["第一学年", "第一学年", "第一学年", "第一学年"]),
           "term": pd.Series(["第一学期", "第一学期", "第二学期", "第二学期"])}

series2 = {"name": pd.Series(["Wilson", "Bruce", "Wilson", "Bruce"]),
           "math_score": pd.Series([90, 68, 83, 67]),
           "en_score": pd.Series([95, 99, 89, 72]),
           "school_year": pd.Series(["第二学年", "第二学年", "第二学年", "第二学年"]),
           "term": pd.Series(["第一学期", "第一学期", "第二学期", "第二学期"])}

df1 = pd.DataFrame(series1)
df2 = pd.DataFrame(series2)
df3 = df1.append(df2, ignore_index=True)
print(df3["math_score"][1:7:2])

