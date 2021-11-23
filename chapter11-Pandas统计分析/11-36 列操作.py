import pandas as pd

series = {"name": pd.Series(["Wilson", "Bruce", "Chelsea"]),
          "age": pd.Series([15, 24, 19]),
          "gender": pd.Series(["man", "man", "woman"])}

df = pd.DataFrame(series)
'''
访问列
'''
print(df["name"])
'''
添加列
'''
df["height"] = pd.DataFrame(pd.Series(["180cm", "165cm", "172cm"]))
print(df)
'''
删除列
'''
df.pop("name")
print(df)

