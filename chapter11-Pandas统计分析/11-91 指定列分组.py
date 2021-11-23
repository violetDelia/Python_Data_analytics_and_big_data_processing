import pandas as pd
import numpy as np

series1 = {"name": pd.Series(["Wilson", "Bruce", "Chelsea", "Wilson", "Bruce", "Chelsea"]),
           "math_score": pd.Series([98, 88, 80, 70, 68, 75]),
           "en_score": pd.Series([70, 68, 85, 61, 99, 82]),
           "term": pd.Series(["第一学期", "第一学期", "第一学期",
                              "第二学期", "第二学期", "第二学期"]),
           "test": pd.Series(["1", "0", "1", "0", "1", "1"])}

df1 = pd.DataFrame(series1)
print(df1)
print("按学期分组：", df1.groupby("term").groups)

print(df1.groupby(["term", "test"]).groups)
print(df1.groupby(["test", "term"]).groups)
