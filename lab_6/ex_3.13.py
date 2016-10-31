import numpy as np
import random
import matplotlib.pyplot as plt
data = []
with open('img.txt', 'r') as img:
    for line in img:
        p = list(map(float, line.strip().split()))
        data.append(p)
data = np.array(data)
d = [i for i in range(1,200)]
C = []
c = random.sample(d, 100)
for i in range(100):
    C.append(data[c[i]])
plt.subplot(211)
plt.imshow(C, cmap=plt.get_cmap('gray'))
plt.show()