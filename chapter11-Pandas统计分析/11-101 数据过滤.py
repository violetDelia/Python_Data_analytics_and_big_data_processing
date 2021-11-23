import pandas as pd
import numpy as np

series1 = {"name": pd.Series(["Wilson", "Bruce", "Chelsea", "Wilson", "Bruce", "Chelsea"]),
           "math_score": pd.Series([98, 88, 91, 90, 68, 75]),
           "en_score": pd.Series([92, 68, 94, 92, 99, 82]),
           "term": pd.Series(["第一学期", "第一学期", "第一学期",
                              "第二学期", "第二学期", "第二学期"])}

df1 = pd.DataFrame(series1)
group_data = df1.groupby(["name"])
for group,data in group_data:
    print (group)
    print (data)

def f(item, a):
    if item["math_score"].agg(np.sum) >= a and item["en_score"].agg(np.sum) >= a:
        return True
    else:
        return False

data = group_data.filter(f, a=180)
print(data)

