# Программа, которая определяет в матрице столбец с наибольшим количеством
# положительнх элементов. Если такого нет, выводит информацию об этом.
# Сушина АД ИУ7-11б

# A - матрица 
# N - размер матрицы
# i,j,k,m,z,q - рабочие переменные
# y - искомый столбец
# B - искомый массив

k = 0
while k == 0: 
    N = input('Введите размер матрицы:')
    if N.isdigit():
        k = 1
        N = int(N)
    
A = [[0]*N for i in range(N)]

for i in range(N):
    for j in range(N):
        k = 1
        while k:
            print('A[',i,'][',j,']=',sep='',end='')
            A[i][j] = input()
            a = A[i][j]
            if a == '':
                m = 0
            elif a[0] == '-':
                if a.count('.') == 1 and a[1] != '.':
                    z = a.find('.')
                    if z == 2 and a[1].isdigit():
                        if len(a)-z == 1 and a[len(a)].isdigit():
                            m = 1
                        elif a[z+1:].isdigit():
                            m = 1
                        else:
                            m = 0
                    elif len(a)-z == 1 and a[len(a)].isdigit():
                        if a[1:z-1].isdigit():
                            m = 1
                        else:
                            m = 0
                    elif a[1:z-1].isdigit() and a[z+1:].isdigit():
                        m = 1
                    else:
                        m = 0
                elif a[1:].isdigit():
                    m = 1
                else:
                    m = 0
            elif a.count('.') == 1 and a[0] != '.':
                z = a.find('.')
                if z == 1 and a[0].isdigit():
                    if a[z+1:].isdigit():
                        m = 1
                    else:
                        m = 0
                elif len(a)-z == 1 and a[len(a)].isdigit():
                    if a[:z-1].isdigit():
                        m = 1
                    else:
                        m = 0
                elif a[:z-1].isdigit() and a[z+1:].isdigit():
                    m = 1
                else:
                    m = 0
            elif a.isdigit():
                m = 1  
            else:
                m = 0
            if m == 0:
                k += 1
            if m == 1:
                k = 0
    print()

for i in range(N):
    for j in range(N):
        A[i][j] = float(A[i][j])
print('Исходная матрица:')
for q in A:
    print(q)
print()

kmax = 0
n = 0
y = -1
for j in range(N):
    k = 0
    for i in range(N):
        if A[i][j] > 0:
            k +=1
    if k > kmax:
        kmax = k
        y = j
        n = 1
    elif k == kmax:
        n +=1
        
if n > 1 or n == 0:
    print('Искомых стоблцов несколько.')
elif y == -1:
    print('В массиве нет положительных элементов')
else:
    print('Столбец с наибольшим количеством положительных элементов:',y)

B=[]
for i in range (N):
    for j in range(i+1,N):
        B.append(A[i][j])
print()
print('Массив из элементов матрицы, находящихся над главной диагональю:')
print(B) 
    
