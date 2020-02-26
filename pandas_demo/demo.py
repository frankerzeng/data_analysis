import pandas as pd
from matplotlib import pyplot as plt

t = pd.Series([2, 3, 4, 4, 4, 2])
print(t)

pf = pd.read_csv("./file-data.csv")

data = pf['time'].values

num_bin = (data.max() - data.min()) // 10
print(data)

plt.figure(figsize=(20, 8), dpi=60)
plt.hist(data, num_bin)
plt.show()
