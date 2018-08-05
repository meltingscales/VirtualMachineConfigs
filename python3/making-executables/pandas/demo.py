import matplotlib.pyplot as plt
import numpy as np

plt.figure()

x = np.arange(0, 5, 0.1) #0 to 5 with 0.1 increments, e.g. [0.1, 0.2, 0.3, ... 4.9, 5.0]
y = np.sin(x)

plt.plot(x, y)
plt.show()