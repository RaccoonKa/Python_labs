import numpy as np
import matplotlib.pyplot as plt


def lissajous(a, b, phi):

  z = np.linspace(0, 2*np.pi, 500)
  x = np.sin(a*z)
  y = np.sin(b*z + phi)
  return x, y


fig, axes = plt.subplots(2, 2, figsize=(10, 8))


axes[0, 0].plot(*lissajous(3, 2, 0), 'r')
axes[0, 0].set_title('3:2')
axes[0, 1].plot(*lissajous(3, 4, 0), 'g')
axes[0, 1].set_title('3:4')
axes[1, 0].plot(*lissajous(5, 4, 0), 'b')
axes[1, 0].set_title('5:4')
axes[1, 1].plot(*lissajous(5, 6, 0), 'm')
axes[1, 1].set_title('5:6')


for ax in axes.flat:
  ax.set_aspect('equal')
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.grid(True)


plt.tight_layout()
plt.show()
