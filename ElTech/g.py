import matplotlib.pyplot as plt
import numpy as np
from numpy import cos, sin, exp
from math import pi, e, sqrt


U = 3

T = 20e-3

tt = 2e-3

w = 2 * pi / T

R1 = 20
R2 = 250
R3 = 750
Rn = 100
L = 95e-3
Ln = 105e-3
C = 10e-6
Cn = 20e-6


def f(x):
    return (
        2
        * np.exp(-97.465887 * x)
        * (-0.0000006 * cos(1021.3383 * x) - 0.181316 * sin(1021.3383 * x))
    )


def achh(x):
    return abs(A(x) / B1(x))


def A(p):
    return 25e7 + 95000 * p


def B1(p):
    return 19 * 3 * p**2 + 145000 * p * 2 + 27e7


def g(x):
    p1 = -3225.4157
    p2 = -4407.1633
    p3 = 0
    return A(p1) * exp(p1 * x) / B1(p1) + A(p2) * exp(p2 * x) / B1(p2) + A(p3) / B1(p3)


def g_new(x):
    p1 = -3225.4157
    p2 = -4407.1633
    print(p1 * 0.7772523)
    return 25 / 27 + 0.7772523 * exp(p1 * x) - 1.703178142216918 * exp(p2 * x)


def h(x):
    p1 = -3225.4157
    p2 = -4407.1633
    return p1 * 0.7772523 * exp(p1 * x) + p2 * (-1.703178142216918) * exp(p2 * x)


def f3(x):
    p1 = -97.465887 + 1021.3383j
    p2 = -97.465887 - 1021.3383j
    return A(p1) * exp(p1 * x) / B1(p1) + A(p2) * exp(p2 * x) / B1(p2)


x = np.arange(0, T, 1e-6)
# g = np.array(list(map(f2, x)))


def f_s(t):
    if t <= tt:
        return U * (g(t))
    if t <= 3 * tt:
        return U * (g(t) - 2 * g(t - tt))
    if t <= 4 * tt:
        return U * (g(t) - 2 * g(t - tt) + 2 * g(t - 3 * tt))
    if t <= 5 * tt:
        return U * (g(t) - 2 * g(t - tt) + 2 * g(t - 3 * tt) - 2 * g(t - 4 * tt))
    if t <= 6 * tt:
        return U * (
            g(t)
            - 2 * g(t - tt)
            + 2 * g(t - 3 * tt)
            - 2 * g(t - 4 * tt)
            + 2 * g(t - 5 * tt)
        )
    return U * (
        g(t)
        - 2 * g(t - tt)
        + 2 * g(t - 3 * tt)
        - 2 * g(t - 4 * tt)
        + 2 * g(t - 5 * tt)
        - g(t - 6 * tt)
    )


"""
f = 100
w = 2 * pi * f
x = np.arange(0, 0.02, 0.0001)
Um = 100


def C(k):
    return abs(Um*((1 if k % 2 == 0 else -1) + 1) / (2*pi*(k ** 2 - 1)))


c = [(C(k), k) for k in range(2, 100)]
print(c)

def func(t):
    return Um/pi + +Um*sin(w*t)/2 - 2*sum(c_k * cos(k * w * t) for c_k, k in c)"""
"""
U = 3В.
tи = 2 мс;
T = 20 мс.
"""
x = np.arange(-2e4, 2e4, 1)


def S1_c(w):
    if w == 0:
        return 0
    rr = (
        U
        * (
            -1
            + 2 * e ** complex(0, -2 * w * tt)
            - 2 * e ** complex(0, -4 * w * tt)
            + 2 * e ** complex(0, -5 * w * tt)
            - e ** complex(0, -6 * w * tt)
        )
    ) / (complex(0, -w))
    return rr
    # return sqrt(rr.real ** 2 + rr.imag ** 2)


def H_c(w):
    if w == 0:
        return 1
    a = R3
    b = 750 + (R2 * (complex(0, w * L) + 1 / complex(0, w * C))) / (
        R2 + complex(0, w * L) + 1 / complex(0, w * C)
    )
    rr = a / b
    return rr


# def S2(w):
#    return H(w)*S1(w)
def S2(w):
    if w == 0:
        return (2 * tt * U * R2) / (R1 + R2)
    a = (
        U
        * (
            2 * e ** complex(0, -2 * tt * w)
            - 1
            - 2 * e ** complex(0, -4 * tt * w)
            + e ** complex(0, -6 * tt * w)
        )
    ) * complex(R2 * R1, R2 * w * L - R2 / (w * C))
    b = complex(0, w) * complex(
        R2 * R1, R2 * w * L - R2 / (w * C) + R1 * w * L - R1 / (w * C)
    )
    rr = a / b
    return sqrt(rr.real**2 + rr.imag**2)


def C1_c(k):
    return calc(S1_c(k * w) / T)


def calc(g):
    return np.absolute(g), np.angle(g)


def C2_c(k):
    return calc(S1_c(k * w) * H_c(k * w) / T)


def spec_1(k):
    return C1_c(k)[0]


def spec_2(k):
    return C2_c(k)[0]


k = np.arange(0, 100, 1)

harm = np.array(list(map(C2_c, k)))


def f(t):
    return harm[0][0] + 2 * sum(
        [harm[i][0] * cos(w * i * t + harm[i][1]) for i in k[1:]]
    )


# значения для графика
# x = [0, 0.002, 0.004, 0.004, 0.006, 0.008, 0.008, 0.01, 0.01, 0.012, 0.012, 0.014, 0.016, 0.018, 0.02]
# y = [3, 3, 3, -3, -3, -3, 3, 3, -3, -3, 0, 0, 0, 0, 0]
"""
k = np.arange(-50, 50, 1)
harm = np.array(list(map(spec_2, k)))


fig, ax = plt.subplots()
ax.stem(k, harm)
ax.set_xlabel('k')
ax.set_ylabel('C2(k)')
plt.show()
exit()
"""

x = np.arange(0, T, 1e-4)
y = np.array(list(map(f, x)))

fig, ax = plt.subplots()

ax.plot(x, y, color="r", linewidth=1)

# ax.stem(k,harm)
ax.set_xlabel("t, с")
ax.set_ylabel("u2, В")
ax.grid()
"""


# major - шаг сетки
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.002))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.001))
ax.yaxis.set_major_locator(ticker.MultipleLocator(3))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))

ax.grid(which='major',
        color='k')

ax.minorticks_on()
ax.grid(which='minor',
        color='gray',
        linestyle=':')

# размер окна вывода
fig.set_figwidth(10)
fig.set_figheight(6)
"""
plt.show()
