x1 = float(input('Введите начальное значение аргумента:'))
shag = float(input('Введите шаг:'))
x2 = float(input('Введите конечное значение аргумента:'))

x = x1
flag = 1
flag1 = 1
flag2 = 1
k = -1
f = 0
while x <= x2 + 1e-7:
    s = x*x - 36
    if flag:
        ma = s
        flag = 0
    elif s > ma:
        ma = s
    if flag1:
        mi = s
        flag1 = 0
    elif s < mi:
        mi = s
    if s >= 0:
        if flag2:
            k = s
            flag2 = 0
        elif s < k:
            k = s
    if s <= 0:
        f +=1
    x += shag

if k < 0:
    k = ma 

m1 = (k-mi)/(ma-mi)*59+1
m1 = round(m1)

u1 = '\u2500'
u2 = '\u252C'
u3 = '\u253C'
u4 = '\u2502'
u5 = '\u2192'
u6 = '\u2193'

print(' '*6,end='')
h = (ma-mi)/10
h = round(h)
min1 = round(mi)
for i in range (10):
    print('{:6d}'.format(min1),end='')
    min1 += h 
print()

print(' '*10,end='')
k = 0
if f == 0:
    for i in range (1,61):
        if i == 1+6*k:
            print(u3,end='')
            k += 1
        else:
            print(u1,end='')
else:
    for i in range (1,61):
        if i == m1:
            print(u2,end='')
            if i == 2+6*k:
                k += 1
        elif i == 1+6*k:
            print(u3,end='')
            k += 1
        else:
            print(u1,end='')
print(u5)
x = x1
while x <= x2 + 1e-7:
    s = x*x - 36
    m = (s-mi)/(ma-mi)*59+1
    m = round(m)
    print('{:9.4}'.format(x), end='')
    if f == 0:
        print(' '*(m-1),'*')
    elif m == m1:
        print(' '*(m-1),'*')
    elif m == m1-1:
        print(' '*(m-1),'*',end='')
        print(u4)
    elif m < m1:
        print(' '*(m-1),'*',end='')
        print(' '*(m1-m-2),u4)
    elif m > m1:
        print(' '*(m1-1),u4, end='')
        print(' '*(m-m1-2),'*')
    x += shag
if f > 0:
    print(' '*8,' '*(m1-1),u6) 

print()
