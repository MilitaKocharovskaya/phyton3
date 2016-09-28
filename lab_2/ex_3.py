import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#import math
x = np.arange(-10, 10.01, 0.01)
y = np.log((x**2+1)*np.e**(-abs(x)/10.))/np.log(1+np.tan(1./(1+(np.sin(x))**2)))
plt.plot(x, y)
plt.title(r'$f(x)$')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.grid(True)
plt.show()