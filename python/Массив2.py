# Сформировать массив случайно сгенерированных чисел.
# Сушина АД ИУ7-11б

# A - массив
# t - число
# l - длина массива 
# m,i,j,k - рабочие переменные

from random import random

k = 1
while k == 1:
    l = input('Введите длину массива:')
    if not l.isdigit():
        k = 1
        print('Неверно! Введите снова.')
    else:
        k = 0
k = 1
while k == 1:
    b = input('Введите начальную границу:')
    if not b.isdigit():
        k = 1
        print()
        print('Неверно! Введите снова.')
        print()
        continue
    else:
        k = 0
    c = input('Введите конечную границу:')
    if not c.isdigit():
        k = 1
        print()
        print('Неверно! Введите снова.')
        print()
        continue
    if int(b) > int(c):
        k = 1
        print()
        print('Неверно! Введите снова.')
        print()

if k == 0:
    l = int(l)
    b = int(b)
    c = int(c) 
    A = [0]*l
    
    for i in range(l):
        k = 1
        while k:
             t = random()*(c-b) + b
             t = round(t)
             m = 0
             for j in range(2,t):
                 if t%j == 0:
                    m += 1
             if m == 0:
                A[i] = t
                k = 0
print() 
print(A) 
