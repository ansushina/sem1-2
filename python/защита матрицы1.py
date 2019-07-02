# Защита матрицы

N = int(input('Введите размер матрицы'))

A = []
for i in range(N):
    A.append([0]*N)
print(A)

k = 0
i = 0
j = 0
M = N

while k <= M*M:
    while j < N-1:
        k += 1
        i = M-N
        A[i][j] = k
        j += 1
        print(A)
        if k == M*M-1:
            break
    while i < N-1:
        k += 1
        j = N-1
        A[i][j] = k
        i += 1
        print(A)
        if k == M*M-1:
            break
    while j > M-N:
        k += 1
        i = N-1
        A[i][j] = k
        j -=1
        print(A)
        if k == M*M-1:
            break
    while i > M-N+1:
        k += 1
        j = M-N
        A[i][j] = k
        i -=1
        print(A)
        if k == M*M-1:
            break
    if k == M*M-1:
         break
    N -= 1 
A[i][j] = M*M

    
for g in A:
    print(g)
