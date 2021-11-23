import pandas as pd
import numpy as np

series1 = {"name": pd.Series(["Wilson", "Bruce", "Chelsea"]),
           "age": pd.Series([15, 24, 19]),
           "math_score": pd.Series([98, 88, 80]),
           "en_score": pd.Series([70, 68, 85])}

df1 = pd.DataFrame(series1)


def f(item, p1, p2):
    item["math_score"] = item["math_score"] + p1
    item["en_score"] = item["en_score"] + p2
    return item

print (df1)
df1 = df1.apply(f, axis=1, args=(10, 20))
print(df1)

