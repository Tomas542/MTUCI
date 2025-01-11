import math as m
import matplotlib.pyplot as plt
import numpy as np

omega = 900
Zr2 = 250
Zr3 = 750
Zrn = 100
Um = 1
L = 95 * 10** (-3)
C = 10 * 10 ** (-6)
Ln = 105 * 10 ** (-3)
Zl = complex(0, omega*L)
Zc = complex(0, -1/(omega * C))
Zln = complex(0, omega * Ln)
Z1 = Zl + Zc
Z2 = (Z1 * Zr2)/(Z1 + Zr2)

r_eq = (Z2 * Zr3)/(Z2 + Zr3)
print(r_eq)
Z_eq = Zr3 + Z2
print("Zэкв = ", Z_eq)
Im1 = Um / Z_eq
print("Im1 = ", Im1)
I1 = Im1/m.sqrt(2)
print("I1 = ", I1)
Uxx = I1 * Zr2
print("Uxx = ", Uxx)

R = np.arange(0, 200, 0.01)
P = []
max_R = 0

for i in range(len(R)):
    I = (Uxx)/(r_eq + R[i])
    x = abs((I**2) * R[i])
    if x == 0.0009564553652530139:
        max_R = R[i]
    P.append(x)

print(max(P))
print(max_R)

fig, ax = plt.subplots()

ax.plot(R, P, label = 'P(R)', color = 'r')
ax.legend()
ax.set_xlabel("R")
ax.set_ylabel("P")
ax.set_title("График зависимости мощности от сопротивления.")

ax.grid(which='major',
        color = 'k')

ax.minorticks_on()
ax.grid(which='minor',
        color = 'gray',
        linestyle = ':')

fig.set_figheight(5)
fig.set_figwidth(8)
plt.show()
