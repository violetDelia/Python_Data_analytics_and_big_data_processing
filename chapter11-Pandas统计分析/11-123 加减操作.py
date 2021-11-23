import pandas as pd
import datetime


date = pd.Series(pd.date_range(datetime.datetime.now().date(), periods=5, freq='D'))
day = pd.Series([datetime.timedelta(days=i) for i in range(1, 6)])
df = pd.DataFrame({"日期": date, "间隔时间": day})
df["加上间隔时间"] = df["日期"] + df["间隔时间"]
df["减去间隔时间"] = df["日期"] - df["间隔时间"]
print(df)


