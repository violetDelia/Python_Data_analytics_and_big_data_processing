import pandas as pd
import numpy as np

series1 = {"name": pd.Series(["Wilson", "Bruce", "Chelsea", "Wilson", "Bruce", "Chelsea"]),
           "math_score": pd.Series([98, 88, 80, 70, 68, 75]),
           "en_score": pd.Series([70, 68, 85, 61, 99, 82]),
           "term": pd.Series(["第一学期", "第一学期", "第一学期",
                              "第二学期", "第二学期", "第二学期"])}

df1 = pd.DataFrame(series1)
group_data = df1.groupby(["name"])

'''
transform生成和原始数据相同的数据
'''
df1[["en_percent", "math_percent"]] = group_data[["en_score", "math_score"]].transform(np.sum)
print(df1[["en_percent", "math_percent"]])
df1["en_percent"] = df1["en_score"] / df1["en_percent"]
df1["math_percent"] = df1["math_score"] / df1["math_percent"]
print(df1)


