# С использованием смешанного метода найти все приближенные корни функции на
# отрезке [a,b] с шагом h с точностью eps. На каждом элементарном отрезке
# находится 1 или 0 корней. Кол-во итераций ограничено. Все выводится в таблицу
# Выводится также графическая интерпретация полученного решения.
# Сушина А Иу7-21б

# root - окно
# c1 - канвас
# l1-l5 - надписи 
# e1-e4 - окна ввода
# v1-v4 - переменные ввода
# btn1, btn2 - кнопки
# arr - матрица entry вывода
# a,b - границы отрезка
# a1,b1 - новые границы отрезка
# h - шаг
# eps - точность
# nmax -максимальное количество итераций
# y - значение функции
# x - значение корня
# x1,x2,x3,y1,y2 - корни производной, первой производной и сответсвующие им f(x)
# t,i,j,k,n - рабочие переменные
# graf, grid, graf1,fig - переменные графика

from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox as mb
from math import sqrt, sin, cos

# Функция
def f(x):
    #y = x*x-4
    y = sin(x)
    return y

# Производная
def fp(x):
    #y = 2*x
    y = cos(x)
    return y

# Вторая производная
def fpp(x):
    #y = 2
    y = -sin(x)
    return y

def extremum(a,b):
    eps = float(e3.get())
    nmax = int(e4.get())
    if fp(b)*fpp(b) < 0:
        a1 = a - fp(a)*(b-a)/(fp(b)-fp(a))
        b1 = b - fp(b)/fpp(b)
        n = 1
        while abs(b1-a1)>eps and n <= nmax:
            a = a1
            b = b1
            a1 = a - fp(a)*(b-a)/(fp(b)-fp(a))
            b1 = b - fp(b)/fpp(b)
            n+=1
    elif fpp(a) == 0:
        n = 1
        a1 = a
        b1 = b - fp(b)*(b-a)/(fp(b)-fp(a))
        while abs(b1-a)>eps and n <= nmax:
            b = b1
            b1 = b - fp(b)*(b-a)/(fp(b)-fp(a))
            n+=1
    else:
        b1 = b - fp(b)*(b-a)/(fp(b)-fp(a))
        a1 = a - fp(a)/fpp(a)
        n = 1
        while abs(b1-a1)>eps and n <= nmax:
            a = a1
            b = b1
            b1 = b - fp(b)*(b-a)/(fp(b)-fp(a))
            a1 = a - fp(a)/fpp(a)
            n+=1
    x = (a1+b1)/2
    return x
    

def proverka():
    # Проверка ввода всех чисел
    v1 = e1.get()
    v1 = v1.split()
    if len(v1) == 2:
        for i in range(2):
            k = v1[i]
            if k.count('-') == 1 and k[0] == '-':
                k = k.replace('-','')
            if k.count('.') == 1:
                k = k.replace('.','')
            if not k.isdigit():
                e1.delete(0,END)
                mb.showerror('Невозможно выполнить','Некорректный ввод границ\
 отрезка.')
                return 0
    else:
        e1.delete(0,END)
        mb.showerror('Невозможно выполнить','Некорректный ввод границ\
 отрезка.')
        return 0
    v1[0] = float(v1[0])
    v1[1] = float(v1[1])
    if v1[0] > v1[1]:
        e1.delete(0,END)
        mb.showerror('Невозможно выполнить','Некорректный ввод границ\
 отрезка.')
        return 0
    v2 = e2.get()
    if v2.count('.') == 1:
        v2 = v2.replace('.','')
    if not v2.isdigit():
        e2.delete(0,END)
        mb.showerror('Невозможно выполнить','Некорректный ввод шага.')
        return 0
    v3 = e3.get()
    if v3.count('.') == 1:
        v3 = v3.replace('.','')
    if v3.count('-') == 1:
        v3 = v3.replace('-','')
    if v3.count('1e') == 1:
        v3 = v3.replace('1e','')
    if not v3.isdigit():
        e3.delete(0,END)
        mb.showerror('Невозможно выполнить','Некорректный ввод eps.')
        return 0
    v3 = float(e3.get())
    if not 0 < v3 < 1:
        e3.delete(0,END)
        mb.showerror('Невозможно выполнить','Некорректный ввод eps.\n 0<eps<1')
        return 0
    if v3 < 0.0000000000000002:
        e3.delete(0,END)
        mb.showerror('Невозможно выполнить','Eps слишком маленькое!.\n')
        return 0
    v4 = e4.get()
    if not v4.isdigit():
        e4.delete(0,END)
        mb.showerror('Невозможно выполнить','Некорректный ввод количества\
 итераций')
        return 0
    v2 = float(e2.get())
    if v2<v3:
        e2.delete(0,END)
        e3.delete(0,END)
        mb.showerror('Невозможно выполнить','Шаг не может быть меньше eps!')
    v2 = float(v2)
    return 1

def poisk(a,b,n1,i):
##    print(a,b)
    # Поиск корней уравнения и заполнение таблицы
    arr.append([])
    for j in range(6):
        arr[i].append(Entry(root,width=12))
        arr[i][j].place(x = 320+j*80,y = 50+i*30)
    x3 = 1
    t = str('{:3d}'.format(n1))
    arr[i][0].insert(END,t)
    t = '['+str('{:6.2f}'.format(a))+';'+\
        str('{:6.2f}'.format(b))+']'
    arr[i][1].insert(END,t)
    ac = a
    bc = b
    eps = float(e3.get())
    nmax = int(e4.get())
    if fp(b)*fpp(b) < 0 or fp(a) == 0:
        a1 = a - f(a)*(b-a)/(f(b)-f(a))
        b1 = b - f(b)/fp(b)
        n = 1
        while abs(b1-a1) > eps and n <= nmax:
            print("a1b1",a1,b1)
            a = a1
            b = b1
            if a < ac or b>bc or b < ac or a > bc:
                t = '-'
                arr[i][2].insert(END,t)
                arr[i][3].insert(END,t)
                arr[i][4].insert(END,t)
                arr[i][5].insert(END,'2')
                return ''
            a1 = a - f(a)*(b-a)/(f(b)-f(a))
            b1 = b - f(b)/fp(b)
            n+=1
    else:
        b1 = b - f(b)*(b-a)/(f(b)-f(a))
        a1 = a - f(a)/fp(a)
        n = 1
        while abs(b1-a1)>eps and n <= nmax:
            print("a1b1",a1,b1)
            a = a1
            b = b1
            if a < ac or b > bc or b < ac or a > bc:
                t = '-'
                arr[i][2].insert(END,t)
                arr[i][3].insert(END,t)
                arr[i][4].insert(END,t)
                arr[i][5].insert(END,'2')
                return ''
            b1 = b - f(b)*(b-a)/(f(b)-f(a))
            a1 = a - f(a)/fp(a)
            n+=1
    if n == nmax+1:
        t = '-'
        arr[i][2].insert(END,t)
        arr[i][3].insert(END,t)
        arr[i][4].insert(END,t)
        arr[i][5].insert(END,'1')
        return ''
    else:
        x = (b1+a1)/2
        t = str('{:12.6f}'.format(x))
        arr[i][2].insert(END,t)
        t = str('{:.0e}'.format(f(x)))
        arr[i][3].insert(END,t)
        t = str(n)
        arr[i][4].insert(END,t)
        arr[i][5].insert(END,'0')
        return str(x)

def pol_del(a,b):
    eps = float(e3.get())
    if abs(f(a)) < 0.00000001:
        return a
    while abs(a-b) > eps:
        x = (a+b)/2
        if f(a)*f(x) < 0:
            b = x
        elif abs(f(x)) < 0.0000001:
            return x
        else:
            a = x
    x = (a+b)/2
    return x

def poisk2(a,b,n1,i):
##    print(a,b)
    # Поиск корней уравнения и заполнение таблицы
    arr.append([])
    for j in range(6):
        arr[i].append(Entry(root,width=12))
        arr[i][j].place(x = 320+j*80,y = 50+i*30)
    x3 = 1
    t = str('{:3d}'.format(n1))
    arr[i][0].insert(END,t)
    t = '['+str('{:6.2f}'.format(a))+';'+\
        str('{:6.2f}'.format(b))+']'
    arr[i][1].insert(END,t)
    ac = a
    bc = b
    eps = float(e3.get())
    nmax = int(e4.get())
    if fp(b)*fpp(b) <= 0 or fp(a) == 0:
        a1 = a - f(a)*(b-a)/(f(b)-f(a))
        b1 = b - f(b)/fp(b)
        n = 1
    else:
        b1 = b - f(b)*(b-a)/(f(b)-f(a))
        a1 = a - f(a)/fp(a)
        n = 1    
    while abs(b1-a1) > eps and n <= nmax:
####        print("a1b1",a1,b1)
        a = a1
        b = b1
        if a < ac or b > bc or b < ac or a > bc:
            if fp(a) != 0:
                b1 = b - f(b)*(b-a)/(f(b)-f(a))
                a1 = a - f(a)/fp(a)
                n = 1
                if a < ac or b > bc or b < ac or a > bc:
                    t = '-'
                    arr[i][2].insert(END,t)
                    arr[i][3].insert(END,t)
                    arr[i][4].insert(END,t)
                    arr[i][5].insert(END,'2')
                    return ''
            else:
                t = '-'
                arr[i][2].insert(END,t)
                arr[i][3].insert(END,t)
                arr[i][4].insert(END,t)
                arr[i][5].insert(END,'2')
                return ''
        a = a1
        b = b1
        if fp(b)*fpp(b) < 0 or fp(a) == 0:
            a1 = a - f(a)*(b-a)/(f(b)-f(a))
            b1 = b - f(b)/fp(b)
        else:
            b1 = b - f(b)*(b-a)/(f(b)-f(a))
            a1 = a - f(a)/fp(a)
        n+=1
    if n == nmax+1:
        t = '-'
        arr[i][2].insert(END,t)
        arr[i][3].insert(END,t)
        arr[i][4].insert(END,t)
        arr[i][5].insert(END,'1')
        return ''
    else:
        x = (b1+a1)/2
        t = str('{:12.5f}'.format(x))
        arr[i][2].insert(END,t)
        t = str('{:.0e}'.format(f(x)))
        arr[i][3].insert(END,t)
        t = str(n)
        arr[i][4].insert(END,t)
        arr[i][5].insert(END,'0')
        return str(x)

def btn1clicked():
    # Нажатие на кнопку "Решить"
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j].destroy()
    c = Canvas(width = 200, height = 200)
    c.place(x = 450, y =60)
    n = len(arr)
    for i in range(n):
        arr.pop()
    if proverka():
        arr1 = []
        v1 = e1.get()
        v1 = v1.split()
        h = float(e2.get())
        for i in range(2):
            v1[i] = float(v1[i])
        a = v1[0]
        n = 0
        k = 0
        while a+h <= v1[1]:
            if f(a)*f(a+h) <= 0 and (f(a+h) != 0 or a+h == v1[1]) :
                poisk2(a,a+h,n,k)
                k+=1
            a += h
            n+=1
        if abs(a-v1[1]) > 0.00000001:
            if f(a)*f(v1[1]) <= 0:
                poisk2(a,v1[1],n,k)
                k+=1
        if k == 0:
            ln = Label(root,text = 'Нет корней!',fg ='#a32', font = 'Arial 20')
            ln.place(x = 450,y = 60)
        # Рисование графика
        ar = []
        arx = []
        ary = []
        fig = plt.figure()
        plt.title('y = sin(x) ')
        newh = (v1[1]-v1[0])/100
        a = v1[0]
        while a<v1[1]:
            ar.append(a)
            if f(a)*f(a+newh) <= 0:
                arx.append(pol_del(a,a+newh))
                ary.append(0)
            a+=newh
        br = []
        for i in range(len(ar)):
            br.append(f(ar[i]))
            
        graf1 = plt.plot([v1[0],v1[1]],[0,0])
        graf = plt.plot(ar,br)
        grid = plt.grid(True)

        for i in range(len(arx)):
            if v1[0] <= arx[i] <= v1[1]:
                plt.scatter(arx[i],ary[i])

        #Точки экстремума
        arr2 =[]
        a = v1[0]
        while a+1 <= v1[1]:
            if fp(a)*fp(a+1) <= 0:
                arr2.append(extremum(a,a+1))
            a+=1
        arr3 =[]
        for i in range(len(arr2)):
            arr3.append(f(arr2[i]))
        for i in range(len(arr2)):
            if v1[0] <= arr2[i] <= v1[1]:
                plt.scatter(arr2[i],arr3[i], c = "red")
        plt.text(v1[0],1.2,'red is extremum\n black is koren')
        plt.show()

def btn2clicked():
    # Очистка
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j].destroy()
    

# Создание окна
root = Tk()
root.title('Смешанный метод уточнения корней')

c1 = Canvas(width = 820, height = 350)
c1.pack()

# Виджеты ввода данных
l1 = Label(root,text='Введите отезок:\n(Формат: a b)')
l2 = Label(root,text='Введите шаг:')
l3 = Label(root,text='Введите точность eps:')
l4 = Label(root,text='Введите кол-во итераций:')

l1.place(x=70,y=10)
l2.place(x=82,y=50)
l3.place(x=32,y=80)
l4.place(x=10,y=110)

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
e1 = Entry(root, textvariable = v1)
e2 = Entry(root, textvariable = v2)
e3 = Entry(root, textvariable = v3)
e4 = Entry(root, textvariable = v4)

e1.place(x=160,y=12)
e2.place(x=160,y=50)
e3.place(x=160,y=80)
e4.place(x=160,y=110)

btn1 = Button(root,text ='Решить',command = btn1clicked)
btn1.place(x = 135, y=140)

btn2= Button(root,text = 'Очистить все', command = btn2clicked)
btn2.place(x=120,y=180)

l5 = Label(root,text='Код ошибки:\n0-верная работа программы\n1-превышено \
количество итераций\n2-касательная выходит за границы отрезка')

l5.place(x=60,y = 230)

l6 = Label(root,text = 'Функция: y = sin(x)')
l6.place(x = 450, y =5)

# Таблица
t = '           №              Интервал                  x                    \
f(x)                          \
n                 Ошибка'
l5 = Label(root,text=t)
l5.place(x=320,y=30)
arr = []

            
root.mainloop()
