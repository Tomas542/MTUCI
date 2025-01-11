import matplotlib.pyplot as plt
import numpy as np
from math import pi, e

x = np.arange(-8120, 8120, 1, dtype=np.int16)
U = 3
T = 20 * 10 ** (-3)
tt = 2 * 10 ** (-3)
w = 2 * pi / T
Zr2 = 250
Zr3 = 750
Zrn = 100
L = 95 * 10** (-3)
C = 10 * 10 ** (-6)
Ln = 105 * 10 ** (-3)
H1 = []

for i in range(len(x)):
    if (x[i] == 0):
        H1.append(0)
    else:
        Zc = complex(0, 1/(x[i] * C))
        Zl = complex(0, x[i] * L)
        Z1 = Zl + Zc
        Z2 = (Z1 * Zr2)/(Z1 + Zr2)
        H1.append(Zr3/(Z2 + Zr3))

H = np.array(H1)

def func(w):
    if (w == 0):
        return 0
    rr = (U * (-1 + 2 * e ** complex(0, -2 * w *tt) - 2 * e ** complex(0, -4 * w * tt) + 2 * e ** complex(0, -5 * w * tt) - e ** complex(0, -6 * w * tt))) / (
             complex(0, -w))
    return rr

y = np.array(list(map(func, x)))
y *= H
y = abs(y)
fig, ax = plt.subplots()

ax.plot(x, y, color='r', linewidth=1, label = "|S2(ω)|")
ax.legend()
ax.set_xlabel('ω')
ax.set_ylabel('S2')
ax.set_title("График модуля спектральной плотности фрагмента сигнала на выходе схемы.")

ax.grid(which='major',
        color = 'k')

ax.minorticks_on()
ax.grid(which='minor',
        color = 'gray',
        linestyle = ':')

fig.set_figheight(5)
fig.set_figwidth(8)

plt.show()
