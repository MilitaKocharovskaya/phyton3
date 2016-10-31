import numpy as np
import matplotlib.pyplot as plt
data = []
with open('img.txt', 'r') as img:
    for line in img:
        p = list(map(float, line.strip().split()))
        data.append(p)
data = np.array(data)
plt.subplot(221)
plt.imshow(data, cmap=plt.get_cmap('gray'))
plt.show()