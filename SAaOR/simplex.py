def simplex(A:list[list[int]], b:list[int], c:list[int]) -> tuple[float, list[float]]:
    # adding x3, x4, x5
    for i in range(len(A)):
        arr = [0] * len(A)
        arr[i] = 1
        A[i] += arr
    
    # there is a negative number
    if sum(num < 0 for num in b) != 0:
        b_mod = [abs(num) for num in b if num < 0]
        b_max = max(b_mod)
        row = b.index(-b_max)
    
    # TODO: no negative number check
    else:
        pass

    max_num = max(abs(num) for num in A[row])
    try:
        max_col = A.index[max_num]
    except:
        max_col = A.index[-max_num]


    # return F, x

A = [[1, 2],
     [3, 1],
     [-1, -3]]
b = [10, 6, -7]
c = [2, 6]

simplex(A, b, c)