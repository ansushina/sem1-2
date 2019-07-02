# Дано множество точек на плоскости. Найти треугольник, для которого разность
# площадей треугольников, образованных делением одной из биссектрис, будет
# минимальна.
# Сушина АД иу7-11б

# v - переменная ввода строки
# h - массив точек
# t1,t2,t3 - искомый треугольник
# l1,l2,l3 - стороны
# kol,kol1,flag,flag1,flag2,k1,k,tg,o1,o2,o3 - рабочие переменные
# xm,minx,ym,miny - минимумы и максимумы
# mi,m -минимум и максимум
# d - переменная для масштабирования
# btn1,btn2,btn3 - кнопки
# c - canvas
# l1 - listbox
# lb,lb1 -label
# od - entry

from tkinter import *
from math import sqrt
from tkinter import messagebox as mb

def btn1clicked():
    v = od.get()
    if v.count(' ') == 1:
        k1 = v.split()
        for i in range(len(k1)):
            if k1[i][0] == '-' and k1[i].count('-') == 1:
                k1[i] = k1[i].replace('-','')
            if k1[i].count('.') == 1 and k1[i][0] != '.':
                k1[i] = k1[i].replace('.','')
        if k1[0].isdigit() and k1[1].isdigit():
            l1.insert(END,v)
            k = v.split()
            for i in range (len(k)):
                k[i] = float(k[i])
            h.append(k)
            od.delete(0,END)
        else:
            mb.showerror('Некорректный ввод','Вы неверно ввели кординаты точки!')
            od.delete(0,END)
    else:
        mb.showerror('Некорректный ввод','Вы неверно ввели кординаты точки!')
        od.delete(0,END)

def btn2clicked():
    kol = 0
    kol1 = 0 
    flag1 = 1
    flag2 = 1
    for i in range(len(h)):
        if h[i] != h[0]:
            kol += 1
            if flag1 and h[i][0]-h[0][0] != 0:
                tg = (h[i][1]-h[0][1])/(h[i][0]-h[0][0])
                flag1 = 0
                kol1+=1
            elif h[i][0]-h[0][0] != 0:
                if tg != (h[i][1]-h[0][1])/(h[i][0]-h[0][0]):
                    kol1 += 1
            elif flag2:
                kol1 += 1
                flag2 = 0
    if len(h) < 3:
        mb.showerror('Неостаточно данных','Недостаточно точек для решения\
 задачи.')
    elif kol < 2:
        mb.showerror('Неверные данные ','Некоторые точки совпадают. Невозможно\
 построить треугольник.')
    elif kol1 < 2:
        mb.showerror('Неверные данные ','Некоторые точки лежат на одной прямой\
. Невозможно построить треугольник.')
    else:
        c.delete('all')
        print(h)
        flag = 1
        for i in range(len(h)):
            for j in range(i+1,len(h)):
                for u in range(j+1,len(h)):
                    o1 = h[i]
                    o2 = h[j]
                    o3 = h[u]
                    if (o3[0]-o1[0])*(o2[1]-o1[1])!=\
                       (o3[1]-o1[1])*(o2[0]-o1[0]):
                        l1 = sqrt((o1[0]-o2[0])**2+(o1[1]-o2[1])**2)
                        l2 = sqrt((o1[0]-o3[0])**2+(o1[1]-o3[1])**2)
                        l3 = sqrt((o3[0]-o2[0])**2+(o3[1]-o2[1])**2)
##                        print(i,j,u)
##                        print(l1,l2,l3)
                        if flag:
                            e = abs(l1-l2)
                            t1 = o1
                            t2 = o2
                            t3 = o3
                            flag = 0
                        if abs(l1-l2) < e:
                            e = abs(l1-l2)
                            t1 = o1
                            t2 = o2
                            t3 = o3
                        if abs(l2-l3) < e:
                            e = abs(l2-l3)
                            t1 = o1
                            t2 = o2
                            t3 = o3
                        if abs(l3-l1) < e:
                            e = abs(l3-l1)
                            t1 = o1
                            t2 = o2
                            t3 = o3
        print(t1,t2,t3)
        xm = h[0][0]
        ym = h[0][1]
        minx = h[0][0]
        miny = h[0][1]
        for i in range(len(h)):
            if h[i][0] < minx:
                minx = h[i][0]
            if h[i][1] < miny:
                miny = h[i][1]
            if h[i][0] > xm:
                xm = h[i][0]
            if h[i][1] > ym:
                ym = h[i][1]
        mi = min(minx,miny)
        if mi<0:
            m = max(xm-mi,ym-mi)
            d = 600/(m+1)
            for i in range(len(h)):
                o = h[i]
                t = c.create_oval((o[0]-mi+1)*d-1.5,(o[1]-mi+1)*d-1.5,\
                                 (o[0]-mi+1)*d +1.5,(o[1]-mi+1)*d+1.5,
                                  fill='black')
            print(t1,t2,t3)
            s1 = c.create_line((t1[0]-mi+1)*d,(t1[1]-mi+1)*d,(t2[0]-mi+1)*d,\
                               (t2[1]-mi+1)*d)
            s2 = c.create_line((t2[0]-mi+1)*d,(t2[1]-mi+1)*d,(t3[0]-mi+1)*d,\
                               (t3[1]-mi+1)*d)
            s3 = c.create_line((t1[0]-mi+1)*d,(t1[1]-mi+1)*d,(t3[0]-mi+1)*d,\
                               (t3[1]-mi+1)*d)
        else:
            m = max(xm,ym)
            d = 600/(m+1)
            for i in range(len(h)):
                o = h[i]
                t = c.create_oval(o[0]*d-1.5,o[1]*d-1.5,\
                                 o[0]*d +1.5,o[1]*d+1.5,
                                  fill='black')
            s1 = c.create_line(t1[0]*d,t1[1]*d,t2[0]*d,t2[1]*d)
            s2 = c.create_line(t2[0]*d,t2[1]*d,t3[0]*d,t3[1]*d)
            s3 = c.create_line(t1[0]*d,t1[1]*d,t3[0]*d,t3[1]*d)
                
def btn3clicked():
    h.clear()
    l1.delete(0,END)
    c.delete('all') 
    

root = Tk()
root.title('Треугольники и их биссектрисы')
h = [] 

c1 = Canvas(width=800,height=700)
c1.pack()

lb = Label(root,text ='Введите координаты точки:')
lb.place(x = 635,y = 20)

lb1 = Label(root,text = 'Формат ввода: x y')
lb1.place(x = 655, y = 40)

v = StringVar()
od = Entry(root,textvariable=v)
od.place(x = 650,y = 70)
btn1 = Button(root,text='Добавить',command=btn1clicked)
btn1.place(x = 680,y = 100)

l1 = Listbox(root,height = 20)
l1.place(x = 650, y = 150) 

c = Canvas(width=600,height=600,bg ='gray80')
##oval =c.create_oval(30,10,130,80)
##t = c.create_rectangle(49,49,51,51)
c.place(x = 20,y = 20)

btn2 = Button(root, text = 'Решить',command=btn2clicked)
btn2.place(x = 685, y = 640)

btn3 = Button(root, text = 'Очистить все',command=btn3clicked)
btn3.place( x = 20, y = 640)

root.mainloop()


