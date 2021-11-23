import pandas as pd
import numpy as np
from sqlalchemy import create_engine

'''
详细细节以后用到再补充
'''

'''
主要步骤:
    1.导入create_engine
    2.创建引擎用于连接数据库和发送sql命令
    3.调用读取数据库的方法以及传入sql语句
'''


engine = create_engine("mysql+pymysql://root:root@localhost:3306/test", encoding="utf8")

sql = "SELECT * from mytable limit 100"
df = pd.read_sql(sql, engine)
df = df.groupby(["name"]).agg(np.sum)
print(df)
df.to_sql("mytable1", engine, index=False)


