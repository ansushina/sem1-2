# Программа для вычисления суммы элементов заданного ряда с точностью eps,
# для построения таблицы с заданным шагом. Если за N итераций ряд не сходится,
# программа выводит информацию об этом. 
# Сушина АД ИУ7-11б

# x - переменная
# eps - точность
# nmax - максимальное количество итераций
# step - шаг
# t - текущий член ряда 
# s - текущая сумма
# k - номер элемента
# u1,u2,u3,u4,u5,u6,u7,u8,u9 - рабочая переменная
# n - рабочая переменная
# z - рабочая переменная
from math import fabs

x = float(input('Введите x:'))
eps = float(input('Введите точность:'))
nmax = int(input('Введите максимальное количесвто итераций:'))
step = float(input('Введите шаг:'))

u1 = '\u250C'
u2 = '\u2500'
u3 = '\u252C'
u4 = '\u2502'
u5 = '\u2534'
u6 = '\u2510'
u7 = '\u2514'
u8 = '\u2518'
u9 = '\u253C'
z = u1+5*u2+u3+12*u2+u3+17*u2+u3+17*u2+u6
print(z)
print(u4,end='')
print('  №  ',end=u4)
print(' Текущий x  ',end=u4)
print('Текущий член ряда',end=u4)
print('        S        ',end=u4)
print()

n = 0
t = 1
s = 1
k = 1
print(u4,end='')
print('{:5d}'.format(k),end=u4)
print('{:12.4f}'.format(x),end=u4)
print('{:17.11f}'.format(t),end=u4)
print('{:17.11f}'.format(s),end=u4)
print()
k = 2
while fabs(t) > eps:
    if k > nmax:
        z = u7+5*u2+u5+12*u2+u5+17*u2+u5+17*u2+u8
        print(z) 
        print('Ряд не сошелся за',nmax,'итераций.')
        break
    n +=2
    t *= (-1)*x*x/(n-1)/n
    s +=t
    if k%step == 0:
        print(u4,end='')
        print('{:5d}'.format(k),end=u4)
        print('{:12.4f}'.format(x),end=u4)
        if fabs(t) >= 10000 or fabs(t) <= 0.000001:
            print('{:17.7e}'.format(t),end=u4)
        else:
            print('{:17.11f}'.format(t),end=u4)
        if fabs(s) >= 10000 or fabs(s) <= 0.000001:
            print('{:17.7e}'.format(s),end=u4)
        else:
            print('{:17.11f}'.format(s),end=u4)
        print()
    k +=1
else:
    if (k-1)%step != 0:
        print(u4,end='')
        print('{:5d}'.format(k-1),end=u4)
        print('{:12.4f}'.format(x),end=u4)
        if fabs(t) >= 10000 or fabs(t) <= 0.000001:
            print('{:17.7e}'.format(t),end=u4)
        else:
            print('{:17.11f}'.format(t),end=u4)
        if fabs(s) >= 10000 or fabs(s) <= 0.000001:
            print('{:17.7e}'.format(s),end=u4)
        else:
            print('{:17.11f}'.format(s),end=u4)
        print()
    z = u7+5*u2+u5+12*u2+u5+17*u2+u5+17*u2+u8
    print(z)
    if  (k-1)%10 == 2 or (k-1)%10 == 3 or (k-1)%10 == 4:
        print('Ряд сошелся за',k-1,'итерации.')
    elif (k-1)%10 == 1:
        print('Ряд сошелся за',k-1,'итерацию.')
    else:
        print('Ряд сошелся за',k-1,'итераций.')
    print('s =','{:0.20e}'.format(s))
