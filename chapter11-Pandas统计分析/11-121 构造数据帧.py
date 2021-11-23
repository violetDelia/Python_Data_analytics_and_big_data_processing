import pandas as pd

date = pd.Series(pd.date_range(pd.datetime.now().date(), periods=5, freq='D'))
print(date)
day = pd.Series([pd.Timedelta(days=i) for i in range(1, 6)])
print(day)
df = pd.DataFrame({"日期": date, "间隔时间": day})
print(df)


