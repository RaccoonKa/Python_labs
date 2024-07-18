import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 6))
fig.suptitle("Сложение двух волн")

x = np.linspace(0, 10, 500)

wave1 = np.sin(2 * np.pi * x)
wave2 = np.sin(4 * np.pi * x)

line1, = ax1.plot(x, wave1, 'r', label="Волна 1")
line2, = ax2.plot(x, wave2, 'b', label="Волна 2")
line3, = ax3.plot(x, wave1 + wave2, 'g', label="Сумма")

ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_title("Волна 1")
ax1.legend()
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_title("Волна 2")
ax2.legend()
ax3.set_xlabel("x")
ax3.set_ylabel("y")
ax3.set_title("Сумма волн")
ax3.legend()

axfreq1 = plt.axes([0.25, 0.1, 0.65, 0.03])
axamp1 = plt.axes([0.25, 0.05, 0.65, 0.03])
axfreq2 = plt.axes([0.25, 0.9, 0.65, 0.03])
axamp2 = plt.axes([0.25, 0.85, 0.65, 0.03])

freq_slider1 = Slider(axfreq1, "Частота 1", 1, 10, valinit=2, valstep=0.1)
amp_slider1 = Slider(axamp1, "Амплитуда 1", 0, 2, valinit=1, valstep=0.1)
freq_slider2 = Slider(axfreq2, "Частота 2", 1, 10, valinit=4, valstep=0.1)
amp_slider2 = Slider(axamp2, "Амплитуда 2", 0, 2, valinit=1, valstep=0.1)


def update(val):
  freq1 = freq_slider1.val
  amp1 = amp_slider1.val
  freq2 = freq_slider2.val
  amp2 = amp_slider2.val

  wave1 = amp1 * np.sin(2 * np.pi * freq1 * x)
  wave2 = amp2 * np.sin(2 * np.pi * freq2 * x)

  line1.set_ydata(wave1)
  line2.set_ydata(wave2)
  line3.set_ydata(wave1 + wave2)

  fig.canvas.draw_idle()

freq_slider1.on_changed(update)
amp_slider1.on_changed(update)
freq_slider2.on_changed(update)
amp_slider2.on_changed(update)

plt.show()
