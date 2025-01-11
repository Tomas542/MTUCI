import math as m
import numpy as np
import matplotlib.pyplot as plt

p2 = complex(-986.8421053, -280.6674870)
p3 = complex(-986.8421053, 280.6674870)

def func(p):
    return (57 * p * p + 150000 * p + 60000000) / (228 * p * p + 300000 * p + 80000000)

t = np.arange(0, 0.02, 0.0001)
#y = np.array(3/4 + func(p2) * m.e ** (p2 * t) + func(p3) * m.e ** (p3 * t))
y = np.array(func(p2) * p2 * m.e ** (p2 * t) + func(p3) * p3 * m.e ** (p3 * t))

t = np.append(0, t)
y = np.append(0.75, y)
fig, ax = plt.subplots()
#ax.plot(t, y, label = 'g(t)', color = 'r')
ax.plot(t, y, label = 'h(t)', color = 'r')
ax.legend()
ax.set_xlabel("t, c")
#ax.set_ylabel("g")
ax.set_ylabel("h")

ax.grid(which='major',
        color = 'k')

ax.minorticks_on()
ax.grid(which='minor',
        color = 'gray',
        linestyle = ':')

fig.set_figheight(5)
fig.set_figwidth(8)

plt.show()