# encoding = utf-8

import pandas as pd
pd_data = pd.read_csv("最后5000.csv", low_memory=False, header=0, names=None)

print(pd_data)


