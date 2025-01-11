import numpy as np
from fractions import Fraction

arr = np.array([[2, 6, 0, 0, 0, 0],
                [1, 2, 1, 0, 0, 10], 
                [3, 1, 0, 1, 0, 6],
                [1, 3, 0, 0, -1, 7]])

num_of_vars = 2
num_of_fake = 3

C_idx = np.arange(num_of_vars, num_of_vars + num_of_fake)
arr[3] = arr[3] * (-1)

if any(arr[arr < 0]):
    b = np.min(arr)
    ind_of_row = np.where(arr==b)[0][0]
    ind_of_num = np.argmax(np.abs(arr[ind_of_row][:4]))
    max_num = arr[ind_of_row, ind_of_num]

    Fraction.__repr__ = lambda self: f"{self._numerator}/{self._denominator}"
    
    arr = arr + Fraction()
    arr[ind_of_row] = arr[ind_of_row] / (max_num)
    
    rows = np.ones(len(arr))
    rows[ind_of_row] = 0
    rows[0] = 0
    rows = rows.astype('bool')
    arr2 = np.tile(arr[ind_of_row], 2)
    
    arr[rows] = arr[rows] - (arr2.reshape(arr[rows].shape) * arr[rows][:, ind_of_num].reshape(arr[rows].shape[0], 1))
    arr[rows][:, ind_of_num] = 0

C_idx[ind_of_row - 1] = ind_of_num

C = arr[0, C_idx].copy()

delta = (C @ arr[1:] - arr[0]).copy()
print(f"delta = {delta}")

while any(delta < 0):
    ind_of_num = np.argmin(delta)
    Q = (arr[1:, -1] / arr[1:, ind_of_num]).copy()
    Q[Q<0] = np.inf
    ind_of_row = np.argmin(Q) + 1
    C_idx[ind_of_row] = ind_of_num

    C = arr[0, C_idx].copy()
    max_num = arr[ind_of_row, ind_of_num]

    arr[ind_of_row] = arr[ind_of_row] / (max_num)

    rows = np.ones(len(arr))
    rows[ind_of_row] = 0
    rows[0] = 0
    rows = rows.astype('bool')
    arr2 = np.tile(arr[ind_of_row], 2)

    arr[rows] = arr[rows] - (arr2.reshape(arr[rows].shape) * arr[rows][:, ind_of_num].reshape(arr[rows].shape[0], 1))
    arr[rows][:, ind_of_num] = 0

    delta = (C @ arr[1:] - arr[0]).copy()
    print(f"delta = {delta}")

def foo(x):
    return 0 if x not in C_idx else arr[np.where(C_idx==x)[0][0] + 1, -1]

print(f"x1 = {foo(0)}, x2 = {foo(1)}, F = {delta[-1]}")
