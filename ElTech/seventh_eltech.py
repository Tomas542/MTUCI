import numpy as np
import matplotlib.pyplot as plt
import math as m

k = np.arange(-50, 50, 1)
U = 3
T = 20 * 10 ** (-3)
tt = 2 * 10 ** (-3)
w = 2 * m.pi / T
e = m.e


def func(w):
    if (w == 0):
        return 0
    rr = (U * (-1 + 2 * e ** complex(0, -2 * w *tt) - 2 * e ** complex(0, -4 * w * tt) + 2 * e ** complex(0, -5 * w * tt) - e ** complex(0, -6 * w * tt))) / (
             complex(0, -w))
    return abs(rr)

def calc(k):
    return func(k*w)/T


y = np.array(list(map(calc, k)))
fig, ax = plt.subplots()

ax.bar(k, y, color='r', linewidth=1, width=0.4)
ax.set_xlabel('k')
ax.set_ylabel('C1')
ax.set_title("График спектра амплитуд сигнала.")

ax.grid(which='major',
        color = 'k')

ax.minorticks_on()
ax.grid(which='minor',
        color = 'gray',
        linestyle = ':')

fig.set_figheight(5)
fig.set_figwidth(8)

plt.show()
