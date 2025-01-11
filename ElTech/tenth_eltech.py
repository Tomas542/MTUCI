import math as m
import numpy as np
import matplotlib.pyplot as plt

p2 = complex(-986.8421053, -280.6674870)
p3 = complex(-986.8421053, 280.6674870)
T = 20 * 10 ** (-3)
tt = 2 * 10 ** (-3)
U = 3

def func(p):
    return (57 * p * p + 150000 * p + 60000000) / (228 * p * p + 300000 * p + 80000000)

def g(t):
    return 3/4 + func(p2) * m.e ** (p2 * t) + func(p3) * m.e ** (p3 * t)

def u(t):
    if t <= 2 * tt:
        return U * g(t)
    if t <= 4 * tt:
        return U * (g(t) - 2 * g(t - 2 * tt))
    if t <= 5 * tt:
        return U * (g(t) - 2 * g(t - 2 * tt) + 2 * g(t - 4 * tt))
    if t <= 6 * tt:
        return U * (g(t) - 2 * g(t - 2 * tt) + 2 * g(t - 4 * tt) - 2 * g (t - 5 * tt))
    return U * (g(t) - 2 * g(t - 2 * tt) + 2 * g(t - 4 * tt) - 2 * g (t - 5 * tt) + g(t - 6 * tt))

t = np.arange(0, 0.02, 0.0001)

y = np.array(list(map(u, t)))
#y = np.array(func(p2) * p2 * m.e ** (p2 * t) + func(p3) * p3 * m.e ** (p3 * t))

x = [0, 0.002, 0.004, 0.004, 0.006, 0.008, 0.008, 0.01, 0.01, 0.012, 0.012, 0.014, 0.016, 0.018, 0.02]
y1 = [3, 3, 3, -3, -3, -3, 3, 3, -3, -3, 0, 0, 0, 0, 0]

fig, ax = plt.subplots()
ax.plot(t, y, color = 'r')
ax.plot(x, y1, color = 'b')
#ax.plot(t, y, label = 'h(t)', color = 'r')
ax.set_xlabel("t, c")
ax.set_ylabel("g")
#ax.set_ylabel("h")
#ax.set_title("")

ax.grid(which='major',
        color = 'k')

ax.minorticks_on()
ax.grid(which='minor',
        color = 'gray',
        linestyle = ':')

fig.set_figheight(5)
fig.set_figwidth(8)

plt.show()