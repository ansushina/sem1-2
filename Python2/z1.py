# Защита систем счисления
# Сушина АД Иу7-11б

#a,b,c - коэффиценты
# e1-e3 -поля ввода
# t - поле вывода
# l,l1-l3 - надписи
# btn1,btn2 - кнопки
# с1 - канвас
# root - окно
# x,x1,x2 - корни
# t1 - рабочая переменная

from tkinter import *
from math import sqrt

def btn1clicked():
    t.delete('1.0',END)
    a = float(e1.get())
    b = float(e2.get())
    c = float(e3.get())

    if a == 0:
        if b == 0:
            if c == 0:
                t.insert(END,'Бесконечное множество \nкорней')
            else:
                t.insert(END,'Нет корней')
        else:
            x = - c/b
            t1 = 'Один корень:\n'+'x = ' + str(x)
            t.insert(END,t1)
    else:         
        d = b*b - 4*a*c
        if d < 0:
            t.insert(END,'Нет действительных корней')
        elif d == 0:
            x = -b/2/a
            t1 ='Два совпадающих корня:\n'+'x = '+str(x)
            t.insert(END,t1)
        else:
            d = sqrt(d)
            x1 = (-b+d)/2/a
            x2 = (-b-d)/2/a
            t1 = 'Два корня:\n'+'x1 = '+str(x1)+'\nx2 = '+str(x2)
            t.insert(END,t1)
            
def btn2clicked():
    t.delete('1.0',END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)

#Окно
root = Tk()
root.title('Квадратное уравнение')
c1 = Canvas(width = 270,height = 180)
c1.pack()

l = Label(root, text = 'Введите коэфиценты квадратного уравнения:')
l.place(x=10,y=10)

# Поля ввода и надписи
v1 = StringVar
e1 = Entry(root, textvariable = v1,width = 7)
v2 = StringVar
e2 = Entry(root,textvariable = v2,width = 7)
v3 = StringVar
e3 = Entry(root,textvariable = v3,width = 7)

l1 = Label(root,text = '*x*x +')
l2 = Label(root,text = '*x +')
l3 = Label(root,text = '=0')

e1.place(x=10,y=40)
l1.place(x=60,y=40)
e2.place(x=100,y=40)
l2.place(x=150,y=40)
e3.place(x=180,y=40)
l3.place(x=230,y=40)

# Кнопки
btn1 = Button(root,text ='Решить',command = btn1clicked)
btn1.place(x = 50, y=80)

btn2= Button(root,text = 'Очистить все', command = btn2clicked)
btn2.place(x=150,y=80)

t = Text(root,width = 25,height= 3)
t.place( x= 25,y = 120)
root.mainloop()
