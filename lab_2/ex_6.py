import matplotlib.pyplot as plt
import numpy as np
x = np.array([1., 2., 3., 4., 5., 6.])
y = np.array([1., 1.42, 1.76, 2, 2.24, 2.5])
v1, p1 = np.polyfit(x, y, deg=1, cov=True)
v2, p2 = np.polyfit(x, y, deg=2, cov=True)
p_f1 = np.poly1d(v1)
p_f2 = np.poly1d(v2)
plt.errorbar(x, y, xerr=0.1, yerr=0.1)
def f(x):
    return p_f1(x)
def g(x):
    return p_f2(x)
t=np.arange(1, 5, 0.01)
plt.plot(t, f(t), t, g(t))
plt.grid()
plt.show()
