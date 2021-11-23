import pandas as pd

series1 = {"name": pd.Series(["Wilson", "Bruce", "Chelsea"]),
           "age": pd.Series([15, 24, 19]),
           "math_score": pd.Series([80, 88, 98]),
           "en_score": pd.Series([70, 68, 85])}


df1 = pd.DataFrame(series1)
print(df1)
df1 = df1.sort_index(axis=1)
print(df1)
