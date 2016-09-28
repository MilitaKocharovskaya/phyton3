import numpy as np
import matplotlib.pyplot as plt
x = []
y = []
b=0.5
a=3
p = 20000
start = -1
finish = 1
d = (finish-start)/p
for i in range (0, p):
    x.append(start+i*d)
    o = 0
    for j in range (0, 200):
        o+=b**j * np.cos(a**j*(start+i*d)*np.pi)
    y.append(o)
plt.plot (x, y)
plt.show()