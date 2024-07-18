import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

x = np.linspace(-1, 1, 100)

degrees = range(1, 8)

fig, ax = plt.subplots()

for n in degrees:
    y = legendre(n)(x)

    ax.plot(x, y, label=f'n = {n}')

ax.set_title("Полиномы Лежандра")
ax.set_xlabel("x")
ax.set_ylabel("P(x)")
ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

plt.show()
plt.show()
