# from basicAnalyseML import res
from analysis import w
import numpy as np
import pandas as pd
from pandas import DataFrame
# Matplotlib forms basis for visualization in Python
import matplotlib.pyplot as plt

# the Seaborn library
# import seaborn as sns
# sns.set()

# convert the classified Data into panda dataframes for plotting.
# df = pd.DataFrame()
# for elem in res:
#     df = df.append(elem['classifications'])

# _, axes = plt.subplots(nrows=1, ncols=1, figsize=(12, 4))
# sns.countplot(x='tag_name',data=df, ax=axes)
# print(res)
# print(df)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values(), color=(0.2, 0.4, 0.6, 0.6))
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()