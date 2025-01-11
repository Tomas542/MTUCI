import matplotlib.pyplot as plt
import numpy as np
import math as m

Zr2 = 250
Zr3 = 750
Zrn = 100
Um = 1
L = 95 * 10** (-3)
C = 10 * 10 ** (-6)
Ln = 105 * 10 ** (-3)

omega = np.arange(1, 6002, 100, dtype=np.int16)
omega_plus = np.array(0)
H1 = []
H1.append(0)
H2 = []

for i in range(len(omega)):
    Zc = complex(0, 1/(omega[i] * C))
    Zl = complex(0, omega[i] * L)
    Z1 = Zl + Zc
    Z2 = (Z1 * Zr2)/(Z1 + Zr2)
    x = Zr3/(Z2 + Zr3)
    H2.append(m.atan(x.imag/x.real))
    H1.append(abs(x))

omega_plus = np.append(omega_plus, omega)

fig, ax = plt.subplots()

#График АЧХ. Если выглядит странно, убери 16 строчку и поменяй omega_plus на omega на 33 строчке.
#ax.plot(omega_plus, H1, label = '|H(jω)|', color = 'r')

#график ФЧХ
ax.plot(omega, H2, label = 'arg⁡(H(jω))', color = 'r')
ax.legend()
ax.set_xlabel("ω")
ax.set_ylabel("H")

#название для графика АЧХ.
#ax.set_title("График амплитудно-частотных характеристик цепи (АЧХ).")

#название для графика ФЧХ
ax.set_title("График фазо-частотных характеристик цепи (ФЧХ).")

ax.grid(which='major',
        color = 'k')

ax.minorticks_on()
ax.grid(which='minor',
        color = 'gray',
        linestyle = ':')

fig.set_figheight(5)
fig.set_figwidth(8)

plt.show()
