import pandas as pd

series = {"name": pd.Series(["Wilson", "Bruce", "Chelsea"]),
          "age": pd.Series([15, 24, 19]),
          "gender": pd.Series(["man", "man", "woman"])}

df = pd.DataFrame(series)
df1 = pd.DataFrame({"name": ["Lucy"], "age": [27], "gender": ["woman"]},index=[len(df.index)])
df = df.append(df1)
print(df)
