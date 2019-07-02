#метод простых итераций
from math import sin

def f(x):
    return sin(x)

def g(x):
    return f(x)+x

def is_float(a):
    if a.count('-') == 1 and a[0] == '-':
        a.replace('-','')
    if a.count('.') == 1 and a[0] != '.':
        a.replace('.','')

def poisk(a,b,eps,n,i):
    ac = a
    bc = b
    print('[','{:6.1f}'.format(a),',','{:6.1f}'.format(b),']    ',\
          i,'    ',end='' )
    n1 = 0
    x = (a+b)/2
    while abs(x-g(x))>eps and a<x<b and n1<n:
        x = g(x)
        n1+=1
##    while abs(a - g(a)) > eps and a < b and n1 < n:
##        a = g(a)
##        print(a)
##        if a < ac:
##            break
##        n1 += 1
##    if a < ac:
##        n1 = 0
##        while abs(b - g(b))> eps and a < b and n1 < n:
##            b = g(b)
##            print(b)
####        print(a)
##            n1 += 1
##            if b > bc:
##                print('    -            -       -     1')
##                return 0
##        a = b
    if not a<x<b:
        print()
        return 0
    if n1 > n:
        print()
        return 0
    print('{:8.4f}'.format(x),'    ','{:3.0e}'.format(f(a)),'    ',n1,'    0')
    
k = 1
while k:
    a = float(input("Input a:"))
    print()
    b = float(input("Input b:"))
    print()
    h = float(input("Input h:"))
    print()
    eps = float(input("Input eps:"))
    print()
    n = int(input("Input n:"))
    k = 0
i = 0
while a+h <= b:
    if f(a)*f(a+h) <= 0:
        poisk(a,a+h,eps,n,i)
    a += h
    i+=1
if abs(a+h-b)> 0.000001:
    if f(a)*f(a+h) <= 0:
        poisk(a,b,eps,n,i)
    

