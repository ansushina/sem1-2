# Быстрая сортировка
# Сушина АД ИУ7-11б

# A - исходный массив
# M - итоговый массив
# l - длина массива
# k,m,z,a,i - рабочие переменные
# a,B,C - аргументы функции

from random import random

k = 0
while k == 0:
    l = input('Введите длину массива:')
    if l == 0:
        pass
    elif l.isdigit():
        k = 1
        l = int(l)
A = [0]*l
for i in range(l):
    k = 1
    while k:
        print('A[',i,']=',sep='',end='')
        A[i] = input()
        a = A[i]
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
##for i in range(l):
##    k = 1
##    while k:
##        print('A[',i,']=',sep='',end='')
##        A[i] = input()
##        a = A[i]
##        if a == '':
##            continue
##        if a[0] == '-' and a.count('-') == 1:
##            a.replace('-','')
##            print(a)
##        if a.count('.') == 1 and a[1] != '.':
##            a.replace('.','')
##            print(a)
##        if a.isdigit():
##            k = 0
        

for i in range (l):
    A[i] = float(A[i])
    
#сортировка
r = random()*(l-1)
r = round(r)
def sort(a,B):
    C =[]
    for i in range (len(B)):
        if B[i] < B[a]:
            C.append(B[i])
    if len(C) == 0:
        return B[a]
    elif len(C) == 1:
        return C[0]
    else:
        r = random()*(len(C)-1)
        r = round(r)
        return sort(r,C)
o = 0
M = []
while o < l:
    k = sort(r,A)
    M.append(k)
    g = A.index(k)
    A.pop(g)
    r = random()*(len(A)-1)
    r = round(r)
    o +=1
print()
print('M =',M) 
    
    
