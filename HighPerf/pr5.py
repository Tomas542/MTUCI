import numpy as np
# import networkx as nx
# import matplotlib.pyplot as plt

# Вероятности
P_A = 4 / 5
P_not_A = 1 - P_A
P_B = 3 / 5
P_not_B = 1 - P_B
p21 = (P_A**4) * (P_A * P_not_A * P_not_B**2)
p12 = (P_A**4) * (P_A**2 * P_not_A * P_B)
p10 = (P_A**2 * P_not_A * P_not_B) * (P_A * P_not_A * P_not_B**2)
p01 = (P_A**2 * P_not_A * P_B) * (P_A * P_not_A * P_not_B**2)
p22 = p12 - p21
p11 = p21 + p01 - p12 - p10
p00 = p10 - p01

A3 = np.array([[-p21, p12, 0], [p21, -(p10 + p12), p01], [1, 1, 1]])

A3_1 = np.linalg.inv(A3)
print(np.array2string(A3_1, precision=3, suppress_small=True))


P_A = 4 / 5  # вероятность, что ничего не сломается
P_not_A = 1 - P_A
P_B = 3 / 5  # вероятность, что всё будет чиниться
P_not_B = 1 - P_B

p32 = (
    (P_A * P_A * P_A * P_A) * (P_A * P_A * P_A * P_A) * (P_not_A * P_B * P_A * P_not_A)
)
p23 = (
    3
    * (P_A * P_A * P_A * P_A)
    * (P_A * P_A * P_A * P_A)
    * (P_not_A * P_B * P_not_A * P_B)
)
p21 = (
    (P_A * P_A * P_A * P_A)
    * (P_A * P_not_A * P_not_B * P_not_B)
    * (P_not_A * P_not_B * P_B * P_not_A)
)
p12 = (
    (P_A * P_A * P_A * P_A)
    * (P_A * P_not_A * P_B * P_A)
    * (P_not_A * P_not_B * P_B * P_not_A)
)
p10 = (
    (P_A * P_A * P_A * P_not_A)
    * (P_A * P_A * P_not_A * P_not_B)
    * (P_not_A * P_not_B * P_B * P_not_A)
)
p01 = (
    (P_A * P_A * P_not_A * P_B)
    * (P_A * P_A * P_A * P_not_A)
    * ((1 / 5) * P_not_B * P_not_B * P_not_B)
)
print(p21)

A1 = np.array(
    [
        [-p32, p23, 0, 0],
        [p32, -(p21 + p23), p12, 0],
        [0, p21, -(p10 + p12), p01],
        [1, 1, 1, 1],
    ]
)

A1_1 = np.linalg.inv(A1)
last_column = A1_1[:, -1]
print(np.array2string(last_column, precision=3, suppress_small=True))
