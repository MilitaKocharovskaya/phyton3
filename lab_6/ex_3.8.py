import numpy as np
import matplotlib.pyplot as plt
data = []
with open('img.txt', 'r') as img:
    for line in img:
        p = list(map(float, line.strip().split()))
        data.append(p)
data = np.array(data)
plt.subplot(222)
values = [data.flatten()]
plt.hist(values, bins=10)
plt.show()