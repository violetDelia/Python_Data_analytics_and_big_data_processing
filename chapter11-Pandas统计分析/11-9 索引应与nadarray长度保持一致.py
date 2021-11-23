import pandas as pd
import numpy as np

init_data = np.array(['hello', 'world', 'python'])
try:
    data = pd.Series(init_data, index=[1, 2])
    print(data)
except Exception as e:
    print(e)
