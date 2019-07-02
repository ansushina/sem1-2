# Программа, которая по введенному массиву A создает массив B, который содержит
# все элементы массива A, меньшие среднего арифметического элементов массива A.
# Сушина АД ИУ7-11б

# A - данный массив
# B - полученный массив
# s - сумма элементов массива A
# l - длина массива A
# sr - среднее арифметическое элементов массива A
# i,m,k,a,z - рабочие переменные 

k = 1
while k:
    k = 1
    A = list(input('Введите список через пробел:').split())
    if A == []:
        k = 2
    for i in range (len(A)):
        a = A[i]
        if a[0] == '-':
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
                if len(a)-z == 1 and a[len(a)].isdigit():
                    m = 1
                elif a[z+1:].isdigit():
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
    if k == 1:
        k = 0
    else:
        print()
        print('Неверно! Введите еще раз.')
        print()
if not k:
    for i in range (len(A)):
        A[i] = float(A[i])
    print()
    print('Исходный массив A: ',end='') 
    print(A)
    print()

    B=[]
    s = sum(A)
    l = len(A)
    sr = s/l
    print('Среднее арифметическое:','{:0.4f}'.format(sr))

    for i in range(l):
        if A[i] < sr:
            B.append(A[i])
    print()
    print('Полученный массив B: ',end='')
    print(B)





