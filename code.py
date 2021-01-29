import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

x = [1, 2, 3]
y = [1.2, 1.9, 3.2]


plt.scatter(x, y,color = 'r',label = 'target points')

xd = np.arange(0,10,1)

yd = (2.21*xd) - 2.32
plt.plot(xd, yd, '-b', label='2.21*xd - 2.32')
plt.title('Likelihood function')
plt.xlabel('xdata')
plt.ylabel('ydata')
plt.legend(loc='upper left')

plt.savefig('line')

plt.show()

