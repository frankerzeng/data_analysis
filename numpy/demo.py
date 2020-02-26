import numpy as np

t1 = np.arange(12).reshape((3, 4)).astype('float')
t1[2, 2:] = np.nan

print(t1)

t2 = t1[[1, 2], [0, 1]]

print(t2)
