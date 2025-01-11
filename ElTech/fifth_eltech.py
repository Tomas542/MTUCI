import matplotlib.pyplot as plt
import numpy as np
from math import pi, e

x = np.arange(-8120, 8120, 1)
U = 3
T = 20 * 10 ** (-3)
tt = 2 * 10 ** (-3)
w = 2 * pi / T


def func(w):
    if (w == 0):
        return 0
    rr = (U * (-1 + 2 * e ** complex(0, -2 * w *tt) - 2 * e ** complex(0, -4 * w * tt) + 2 * e ** complex(0, -5 * w * tt) - e ** complex(0, -6 * w * tt))) / (
             complex(0, -w))
    return abs(rr)


y = np.array(list(map(func, x)))
fig, ax = plt.subplots()

ax.plot(x, y, color='r', linewidth=1, label = "|S1(ω)|")
ax.legend()
ax.set_xlabel('ω')
ax.set_ylabel('S1')
ax.set_title("График модуля спектральной плотности фрагмента сигнала.")

ax.grid(which='major',
        color = 'k')

ax.minorticks_on()
ax.grid(which='minor',
        color = 'gray',
        linestyle = ':')

fig.set_figheight(5)
fig.set_figwidth(8)

plt.show()
