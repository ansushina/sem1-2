# Реализован метод сортировки расческой. Программа проверяет корректную работу
# на случайном массиве малой размерности, а затем выводит таблицу замеров
# времени сортировки массивов трех разных размерностей.
# Сушина АД ИУ7-21б

# root - окно
# c1 - канвас основы
# l1-l9,l,la,ld - надписи 
# e1-e3 - окна ввода 
# v1-v3 - текстовые переменные
# arr - массив entry
# d1,d2,d - время и массив значений времени 
# del1-del3 - время выполнения
# m1-m3,a - массивы
# n1-n3 - длины массивов
# t,n,k,i,gap - рабочие переменные

from tkinter import *
from tkinter import messagebox as mb
from random import randint
import time

def primer():
    # Вывод примера работы сортировки
    d1 = time.time()
    l = 7
    a = [randint(0,50) for i in range(l)]
    t = str(a)
    l = Label(root,text=t)
    l.place(x=170,y=40)
    a = sort(a)
    t = str(a)
    la = Label(root,text=t)
    la.place(y=70, x= 170)
    d2 = time.time()
    d = d2-d1
    t = str(d)
    ld =Label(root, text=t)
    ld.place(x=170, y= 100)
    
def sort(a):
    # Сортировка
    l = len(a)
    gap = int(l/1.247) if l > 1 else 0
    while gap:
        for i in range(l - gap):
            if a[i + gap] < a[i]:
                a[i], a[i + gap] = a[i + gap], a[i]
        gap = int(gap/1.247) 
    return a

def proverka():
    # Проверка, что все N - числа
    v1 = e1.get()
    v2 = e2.get()
    v3 = e3.get()
    if v1.isdigit() and v2.isdigit() and v3.isdigit():
        return 1
    elif not v1.isdigit():
        e1.delete(0,END)
        mb.showerror('Невозможно выполнить','Некорректный ввод N1')
        return 0
    elif not v2.isdigit():
        e2.delete(0,END)
        mb.showerror('Невозможно выполнить','Некорректный ввод N2')
        return 0
    else:
        e3.delete(0,END)
        mb.showerror('Невозможно выполнить','Некорректный ввод N3')
        return 0
    
def mass(n):
    # Получение данных о времени сортировки
    m1 = [i for i in range(n)]
    m2 = [randint(0,99) for i in range(n)]
    m3 = [i for i in range(n,-1,-1)]
    d1 = time.time()
    m1 = sort(m1)
    d2 = time.time()
    del1 = d2-d1
    
    d1 = time.time()
    m2 = sort(m2)
    d2 = time.time()
    del2 = d2-d1
    
    d1 = time.time()
    m3 = sort(m3)
    d2 = time.time()
    del3 = d2-d1

    return del1,del2,del3

def btn1clicked():
    # Нажатие кнопки "Решить"
    for i in range(9):
        arr[i].delete(0,END)
    if proverka():
        n1 = int(e1.get())
        d = []
        d.append(mass(n1))
        n2 = int(e2.get())
        d.append(mass(n2))
        n3 = int(e3.get())
        d.append(mass(n3))
        for i in range(len(d)):
            for j in range(len(d[i])):
                t = '{:0.7f}'.format(d[i][j])
                arr[i+j*3].insert(END,t)
        
    

def btn2clicked():
    #Очистка всех entry
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    for i in range(9):
        arr[i].delete(0,END)

# Создание окна
root = Tk()
root.title('Сортировка расческой')

c1 = Canvas(width = 310, height = 400)
c1.pack()

l1 = Label(root,text='Пример работы:')
l2 = Label(root,text='Исходный массив:')
l3 = Label(root,text='Отсортированный массив:')
l4 = Label(root,text='Время:')

l1.place(x=120,y=10)
l2.place(x=56,y=40)
l3.place(x=10,y=70)
l4.place(x=120,y=100)

# Ввод значений N
l5 = Label(root,text='N1:')
l6 = Label(root,text='N2:')
l7 = Label(root,text='N3:')
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
e1 = Entry(root, textvariable = v1,justify=RIGHT,width = 7)
e2 = Entry(root, textvariable = v2,justify=RIGHT,width = 7)
e3 = Entry(root, textvariable = v3,justify=RIGHT,width = 7)

l5.place(x=30,y=150)
e1.place(x=60,y=150)
l6.place(x=110,y=150)
e2.place(x=140,y=150)
l7.place(x=190,y=150)
e3.place(x=220,y=150)

# Кнопки
btn1 = Button(root,text ='Решить',command = btn1clicked)
btn1.place(x = 135, y=190)

btn2= Button(root,text = 'Очистить все', command = btn2clicked)
btn2.place(x=120,y=350)

# Таблица
l8 = Label(root, text ='N1                 N2                N3')
l8.place(x=95, y=230)
l9 = Label(root, text = '\u2191\n\nrand\n\n\u2193')
l9.place(x=35, y= 250)
arr = []
k = 220
for i in range(9):
    arr.append(Entry(root,width = 9))
    n = i%3
    if n == 0:
        k+=30
    arr[i].place(x=70+70*n,y=k)

primer()
root.mainloop()

