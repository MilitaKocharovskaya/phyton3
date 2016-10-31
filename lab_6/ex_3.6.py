import numpy as np
data = []
with open('img.txt', 'r') as img:
    for line in img:
        p = list(map(float, line.strip().split()))
        data.append(p)
data = np.array(data)