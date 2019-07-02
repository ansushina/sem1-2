# Программа решения квадратного уравнения
# Сушина АД ИУ7-11б

# a, b, c - коэфиценты квадратного уравнения
# d - дискременант
# x, x1, x2 - корни квадратного уравнения

from math import sqrt
a = float(input('Введите a:'))
b = float(input('Введите b:'))
c = float(input('Введите c:'))

if a == 0:
    if  b == 0:
        if c == 0:
            print('Бесконечно много корней.')
        else:
            print('Нет корней.')
    else:
        x = -c/b
        print('Линейное уравнение. Корень: x =',':{:10.3f}'.format(x))
else:
    d = b*b - 4*a*c
    if d < 0:
        print('Нет действительных корней.')
    elif d == 0:
        x = -b/2/a
        print('Корень кратности 2: x =',':{:10.3f}'.format(x))
    else:
        x1 = (-b + sqrt(d)) / (2*a)
        x2 = (-b - sqrt(d)) / (2*a)

        print('x1 =',':{:10.3f}'.format(x1))
        print('x2 =',':{:10.3f}'.format(x2))
        
