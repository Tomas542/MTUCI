import math as m

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

Zn = (Zln * Zrn)/(Zln + Zrn)
print("Zn ", Zn)

Z1 = Zl + Zc
print("Z1 ", Z1)
Z2 = (Z1 * Zr2)/(Z1 + Zr2)
print("Z2 ", Z2)

Z3 = (Zln * Zrn * Zr3)/(Zln*Zrn + Zln*Zr3 + Zrn*Zr3)
print("Z3", Z3)

Zinter = Z2 + Z3
print("Zвх", Zinter)

Im1 = Um / Zinter
print("Im1 ", Im1)

Im2 = (Im1 * (Zl + Zc)) / (Zl + Zc + Zr2)
print("Im2 ", Im2)

Im3 = Im1 - Im2
print("Im3 ", Im3)

Im4 = (Im1 * Zn)/(Zr3 + Zn)
print("Im4 ", Im4)

Im5 = (Im1 * ((Zr3 * Zln)/(Zln + Zr3)))/(((Zr3 * Zln)/(Zln + Zr3)) + Zrn)
print("Im5 ", Im5)

Im6 = Im1 - Im4 - Im5 #-Im4
print("Im6 ", Im6)

print(f"i1 = {abs(Im1)} * cos({omega}t + {m.atan(Im1.imag/Im1.real)})")
print(f"i2 = {abs(Im2)} * cos({omega}t + {m.atan(Im2.imag/Im2.real)})")
print(f"i3 = {abs(Im3)} * cos({omega}t + {m.atan(Im3.imag/Im3.real)})")
print(f"i4 = {abs(Im4)} * cos({omega}t + {m.atan(Im4.imag/Im4.real)})")
print(f"i5 = {abs(Im5)} * cos({omega}t + {m.atan(Im5.imag/Im5.real)})")
print(f"i6 = {abs(Im6)} * cos({omega}t + {m.atan(Im6.imag/Im6.real)})")

print(f"Un = {(Im5 + Im6) * Zn}")

U = Um/m.sqrt(2)
print(f"U = {U}")

I = U/abs(Zinter)
print(f"I = {I}")

print(f"P1 = {I * U * m.cos(m.atan(Zinter.imag/Zinter.real))}")
print(f"Q1 = {I * U * m.sin(m.atan(Zinter.imag/Zinter.real))}")

print(f"P2 = {((abs(Im2)/m.sqrt(2)) **2) * Zr2 + ((abs(Im4)/m.sqrt(2)) ** 2) * Zr3 + ((abs(Im5)/m.sqrt(2)) ** 2) * Zrn}")
print(f"Q2 = {((abs(Im1)/m.sqrt(2)) ** 2) * omega * L - ((abs(Im3)/m.sqrt(2)) ** 2) / (omega * C) + ((abs(Im6)/m.sqrt(2))  ** 2) * omega * Ln}")
