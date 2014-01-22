import numpy as np
from matplotlib import pyplot as plt

import sys, os
sys.path.append(os.getcwd()+'/..')

import gridpts
import lgrng

x = gridpts.cheb(20)
y = np.sin(np.sin(x))
plt.plot(x, y, 'ro')

xx = gridpts.unif(200)
xx = xx*0.999 + 1e-6
yy = lgrng.interp(x, y, xx)
plt.plot(xx, yy, 'k')
plt.axis('tight')
plt.show()
