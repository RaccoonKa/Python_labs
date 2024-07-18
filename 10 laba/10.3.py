import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def lissajous(a, b, phi):

  t = np.linspace(0, 2*np.pi, 500)
  x = np.sin(a*t)
  y = np.sin(b*t + phi)
  return x, y

fig, ax = plt.subplots()
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)

line, = ax.plot([], [], 'r')


def animate(i):

  frequency = i / 50
  x, y = lissajous(1, frequency, 0)
  line.set_data(x, y)
  return line,

ani = animation.FuncAnimation(fig, animate, frames=50, interval=50, blit=True)

plt.show()
