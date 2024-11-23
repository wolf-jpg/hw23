# i got this from https://matplotlib.org/stable/users/getting_started/

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 200)
y = np.sin(2*x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()