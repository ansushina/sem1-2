# Программа для вычисления интегралов различными методами.
# Сушина АД Иу7-11б

# f- функция
# n1,n2 - количество разбиений
# a,b - границы отрезка
# k,b1,b2,b,e1,h,x,d- рабочие переменные
# e - точность
# u1,u2,u3,u4,u5,u6,u7,u8,u9,u10,u11 - символы юникода
# I11,I12,I22,I21 - значения интегралов
# n - количество разбиений 

from math import sin

def f(x):
    y = sin(x)
    return(y)

k = 1
while k:
    n1 = input('Введите первое значение N:')
    if n1.isdigit():
        n1 = int(n1)
        break
    else:
        print('Неверно! Введите еще раз.')
while k:
    n2 = input('Введите второе знаниче N:')
    if n2.isdigit():
        n2 = int(n2)
        break
    else:
        print('Неверно! Введите еще раз.')
print()
while k:
    a = input('Введите начальную границу отрезка:')
    b1 = a
    if a[0] == '-':
        if a.count('.') == 1 and a.index('.') != 0:
             b1 = a.replace('.','')
        if b1[1:].isdigit():
             a = float(a)
             break
        else:
            print('Неверно! Введите еще раз.')
    else:
        if a.count('.') and a.index('.') != 0:
             b1 = a.replace('.','')
        if b1.isdigit():
             a = float(a)
             break
        else:
            print('Неверно! Введите еще раз.')
    
while k:
    b = input('Введите конечную границу отрезка:')
    b2 = b
    if b[0] == '-':
        if b.count('.') == 1 and b.index('.') != 0:
             b2 = b.replace('.','')
        if b2[1:].isdigit():
             b = float(b)
             break
        else:
            print('Неверно! Введите еще раз.')
    else:
        if b.count('.') == 1 and b.index('.') != 0:
             b2 = b.replace('.','')
        if b2.isdigit():
             b = float(b)
             break
        else:
            print('Неверно! Введите еще раз.')
print()
while k:
    e = input('Введите точность:')
    e1 = e
    if e1.count('e') == 1 and e1.index('e') != 0:
        e1 = e.replace('e','')
        if e1.count('-') == 1 and e1.index('-') == 1:
            e1 = e1.replace('-','')
            if e1.isdigit():
                e = float(e)
                break
            else:
                print('Неверно! Введите еще раз1.')
        elif e1.count('+') == 1 and e1.index('+') == 1:
            e1 = e1.replace('+','')
            if e1.isdigit():
                e = float(e)
                break
            else:
                print('Неверно! Введите еще раз.')
        else:
            print('Неверно! Введите еще раз2.')
    else:
        if e1.count('.') == 1 and e1.index('.') != 0:
            e1 = e.replace('.','')
        if e1.isdigit():
            e = float(e)
            break
        else:
            print('Неверно! Введите еще раз.')

u1 = '\u250C'
u2 = '\u2500'
u3 = '\u252C'
u4 = '\u2502'
u5 = '\u2534'
u6 = '\u2510'
u7 = '\u2514'
u8 = '\u2518'
u9 = '\u251C'
u10 = '\u2524'
u11 = '\u253C'

def pravie(n,a,b):
    h = (b-a)/n
    x = a + h
    d = 0
    for i in range(n):
        d += f(x)
        x += h
    I = d * h
    return(I)
 

def tri(n,a,b):
    I = 0
    delta = (b-a)/n
    x = a
    for i in range(n+1):
        if i == 0 or i == n:
            k = 0
        elif i%3 == 0:
            k = 2
        else:
            k = 3
        I += k*f(x)
        x += delta
    I *= delta*3/8
    return(I)

I11 = pravie(n1,a,b) 
I12 = pravie(n2,a,b)

I21 = tri(n1,a,b)
I22 = tri(n2,a,b)

print() 
print(u1+30*u2+u3+20*u2+u3+20*u2+u6)
print(u4,'           Метод            ',u4,'         N1       ',\
      u4,'       N2         ',u4)
print(u9+30*u2+u11+20*u2+u11+20*u2+u10)
print(u4,'Метод правых прямоугольников',u4,'{:19.8f}'.format(I11),end=u4)
print('{:19.8f}'.format(I12),u4)
print(u9+30*u2+u11+20*u2+u11+20*u2+u10)
print(u4,'         Метод 3/8          ',u4,'{:19.8f}'.format(I21),end=u4)
print('{:19.8f}'.format(I22),u4)
print(u7+u2*30+u5+u2*20+u5+20*u2+u8)

nm = max(n1,n2)
nm = 2
I1 = pravie(nm,a,b)
I2 = pravie(nm*2,a,b)

while abs(I2-I1) > e:
    nm = 2*nm
    I1 = pravie(nm,a,b)
    I2 = pravie(nm*2,a,b)

print('N, при котором достигается точность:',2*nm)
print('Значение интеграла:',pravie(nm*2,a,b))

##nm = 2
##I1 = tri(nm,a,b)
##I2 = tri(nm*2,a,b)
##
##while abs(I2-I1) > e:
##    nm = 2*nm
##    I1 = tri(nm,a,b)
##    I2 = tri(nm*2,a,b)
##
##print('N, при котором достигается точность:',2*nm)
##print('Значение интеграла:',tri(nm*2,a,b))
