import pandas as pd
import numpy as np
# 导入机器学习库
from sklearn.cluster import KMeans

file = "chapter11-Pandas统计分析\成绩明细表.xlsx"
df = pd.read_excel(file, sheet_name='成绩表')
df["平均成绩"] = df.iloc[:, 1:13].apply(lambda x: x.mean(), axis=1)

def get_actegory(data, k):
    means_model = KMeans(n_clusters=k)
    train_data = data.values.reshape((len(data), 1))
    means_model.fit(train_data)
    center = pd.DataFrame(means_model.cluster_centers_).sort_values(0)
    mean_data = center.rolling(2).mean().iloc[1:]
    mean_data = [0] + list(mean_data[0]) + [data.max()]
    data = pd.cut(data, mean_data, labels=["差", "中", "良", "优"])
    return data

result = get_actegory(df["平均成绩"], 4)
print(result.value_counts())


