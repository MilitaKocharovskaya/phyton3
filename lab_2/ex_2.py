import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-3, 4.01, 0.01)
plt.plot(x, x**2-x-6)
plt.title(r'$y(x)=x^2-x-6$')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.grid(True)
plt.show()