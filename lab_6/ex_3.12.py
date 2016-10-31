import numpy as np
import random
import matplotlib.pyplot as plt
data = []
with open('img.txt', 'r') as img:
    for line in img:
        p = list(map(float, line.strip().split()))
        data.append(p)
data = np.array(data)
A = []
for i in range(100):
    a = random.choice(data)
    A.append(a)
plt.subplot(211)
plt.imshow(A, cmap=plt.get_cmap('gray'))
plt.show()