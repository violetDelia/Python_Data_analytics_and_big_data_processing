# !/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import numpy as np

#sns.set()
file = "chapter11-Pandas统计分析\成绩明细表.xlsx"
df = pd.read_excel(file, sheet_name='成绩表')
df["总成绩"] = df.iloc[:, 1:13].apply(lambda x: x.sum(), axis=1)
df["平均成绩"] = df.iloc[:, 1:13].apply(lambda x: x.mean(), axis=1)
df.loc["各科目平均成绩"] = df.iloc[0:, 1:13].apply(lambda x: x.mean(), axis=0)
df.fillna("")
print (df[["学号","总成绩","平均成绩"]])
