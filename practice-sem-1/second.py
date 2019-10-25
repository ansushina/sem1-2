# Учебно-вычислительный практикум. 1 курс 1 сесместр.
# Скругление углов
# Сушина АД Иу7 - 11 б

from tkinter import *
from math import sqrt, acos, pi
from tkinter import messagebox as mb

def new(x,y,cosn,sinn,dx,dy):
    Y = cosn*y - x*sinn
    X = (Y*sinn+x)/cosn
    Y -= dy
    X -= dx
    return X,Y

def past(X,Y,cosn,sinn,dx,dy):
    x = (X+dx)*cosn-(Y+dy)*sinn
    y = (X+dx)*sinn+(Y+dy)*cosn
    return x,y

def pr(x,k,b):
    return k*x+b

def res(t1,t2,t3,r):
    # Нахождение уравнений прямых 1 и 2.
    g1 = False
    g2 = False
    g3 = False
    if t1[0] != t3[0]:
        k1 = (t1[1] - t3[1])/(t1[0] - t3[0])
        b1 = t1[1] - k1*t1[0]
    else:
        g1 = True
    if t2[0] != t3[0]:
        k2 = (t2[1] - t3[1])/(t2[0] - t3[0])
        b2 = t2[1] - k2*t2[0]
    else:
        g2 = True
    if not g1 and not g2:
        xp = (b2-b1)/(k1-k2)
        yp = k1*xp + b1
    elif g1:
        xp = t1[0]
        yp = k2*xp + b2
    elif g2:
        xp = t2[0]
        yp = k1*xp+b1
    # Наождение точек, находящихся на необходимом расстоянии от вершины угла
    if not g1: 
        d1 = (xp-k1*b1+k1*yp)**2 - (1+k1*k1)*(xp*xp + (b1-yp)**2 - r*r)

##        print(d1)
        x11 = ((xp-k1*b1+k1*yp) + sqrt(d1)) / (1+k1*k1)
        y11 = k1*x11 + b1
        x12 = ((xp-k1*b1+k1*yp) - sqrt(d1)) / (1+k1*k1)
        y12 = k1*x12 + b1
    else:
        x11 = t1[0]
        y11 = yp + r
        x12 = t1[0]
        y12 = yp-r
        
    if not g2:
        d2 = (xp-k2*b2+k2*yp)**2 - (1+k2*k2)*(xp*xp + (b2-yp)**2 - r*r)

##        print(d2)
        x21 = ((xp-k2*b2+k2*yp) + sqrt(d2)) / (1+k2*k2)
        y21 = k2*x21 + b2
        x22 = ((xp-k2*b2+k2*yp) - sqrt(d2)) / (1+k2*k2)
        y22 = k2*x22 + b2
    else:
        x21 = t2[0]
        y21 = yp + r
        x22 = t2[0]
        y22 = yp - r
    # Выбор точек лежащих на сторонах угла
    h=[]
    
    if t1[0]<t3[0]:
        if x11<t3[0]:
            t = []
            t.append(x11)
            t.append(y11)
            h.append(t)
        else:
            t = []
            t.append(x12)
            t.append(y12)
            h.append(t)
    elif t1[0] == x11 == t3[0]:
        if t1[1]<t3[1]:
            if y11<t3[1]:
                t = []
                t.append(x11)
                t.append(y11)
                h.append(t)
            else:
                t = []
                t.append(x12)
                t.append(y12)
                h.append(t)
        elif t1[1]>t3[1]:
            if y11 > t3[1]:
                t = []
                t.append(x11)
                t.append(y11)
                h.append(t)
            else:
                t = []
                t.append(x12)
                t.append(y12)
                h.append(t)
        else:
            t = []
            t.append(x12)
            t.append(y12)
            h.append(t)
    else:
        if x11>t3[0]:
            t = []
            t.append(x11)
            t.append(y11)
            h.append(t)
        else:
            t = []
            t.append(x12)
            t.append(y12)
            h.append(t)
        
    if t2[0]<t3[0]:
        if x21<t3[0]:
            t = []
            t.append(x21)
            t.append(y21)
            h.append(t)
        else:
            t = []
            t.append(x22)
            t.append(y22)
            h.append(t)
    elif t2[0] == x21 == t3[0]:
        if t2[1]<t3[1]:
            if y21<t3[1]:
                t = []
                t.append(x21)
                t.append(y21)
                h.append(t)
            else:
                t = []
                t.append(x22)
                t.append(y22)
                h.append(t)
        elif t2[1]>t3[1]:
            if y21 > t3[1]:
                t = []
                t.append(x21)
                t.append(y21)
                h.append(t)
            else:
                t = []
                t.append(x22)
                t.append(y22)
                h.append(t)
    else:
        if x21>t3[0]:
            t = []
            t.append(x21)
            t.append(y21)
            h.append(t)
        else:
            t = []
            t.append(x22)
            t.append(y22)
            h.append(t)
    return(h)

def proverka():
    c.delete('all')
    text.delete('1.0',END)
    u1 = e1.get()
    u2 = e2.get()
    u3 = e3.get()
    r = e4.get()

    err1 = False
    err2 = False
    err3 = False
    err4 = False
    err5 = False
    # Проверка на верный ввод координат точек, расстояния, выбор варианта.
    if u1.count(' ') == 1:
        o = u1.split()
        for i in range(len(o)):
            if o[i][0] == '-' and o[i].count('-') ==1:
                o[i] = o[i].replace('-','')
            if o[i].count('.') == 1 and o[i][0] != '.':
                o[i] = o[i].replace('.','')
        if o[0].isdigit() and o[1].isdigit():
            t1 = u1.split()
            for i in range(len(t1)):
                t1[i] = float(t1[i])
        else:
            err1 = True
    else:
        err1 = True

    if u2.count(' ') == 1:
        o = u2.split()
        for i in range(len(o)):
            if o[i][0] == '-' and o[i].count('-') ==1:
                o[i] = o[i].replace('-','')
            if o[i].count('.') == 1 and o[i][0] != '.':
                o[i] = o[i].replace('.','')
        if o[0].isdigit() and o[1].isdigit():
            t2 = u2.split()
            for i in range(len(t2)):
                t2[i] = float(t2[i])
        else:
            err2 = True
    else:
        err2 = True
        
    if u3.count(' ') == 1:
        o = u3.split()
        for i in range(len(o)):
            if o[i][0] == '-' and o[i].count('-') ==1:
                o[i] = o[i].replace('-','')
            if o[i].count('.') == 1 and o[i][0] != '.':
                o[i] = o[i].replace('.','')
        if o[0].isdigit() and o[1].isdigit():
            t3 = u3.split()
            for i in range(len(t3)):
                t3[i] = float(t3[i])
        else:
            err3 = True
    else:
        err3 = True

    r1 = r
    if r1.count('.') == 1 and r1[0] != '.':
        r1 = r1.replace('.','')
    if r1.isdigit():
        if float(r1) != 0:
            r = float(r)
        else:
            err4 = True
    else:
        err4 = True

    v1 = int(v.get())
    if v1 == 0:
        err5 = True
    if not err1 and not err2 and not err3 and not err4 and not err5:
        proverka2(t1,t2,t3,r,v1)
    elif err1:
        mb.showerror('Некорректный ввод','Вы неверно ввели кординаты первой \
точки!')
        e1.delete(0,END)
    elif err2:
        mb.showerror('Некорректный ввод','Вы неверно ввели кординаты второй \
точки!')
        e2.delete(0,END)
    elif err3:
        mb.showerror('Некорректный ввод','Вы неверно ввели кординаты вершины \
угла!')
        e3.delete(0,END)
    elif err4:
        mb.showerror('Некорректный ввод','Вы неверно ввели расстояние для \
скругления!')
        e4.delete(0,END)
    elif err5:
        mb.showerror('Невозможно выполнить','Не выбран способ решения!')

def proverka2(t1,t2,t3,r,v1):
    # Проверка на совпадение, а так же расположение точек на одной прямой
    err6 = False
    err7 = False
    f1 = False
    f2 = False
    if t1 == t3 or t2 == t3 or t1 == t3:
        err6 = True
    if t2[0] != t3[0] and t1[0] != t3[0]:
        if t1[0] != t3[0]:
            k1 = (t1[1] - t3[1])/(t1[0] - t3[0])
        else:
            f1 = True
        if t1[0] != t2[0]:
            k2 = (t1[1] - t2[1])/(t1[0] - t2[0])
        else:
            f2 = True
        if f1 and f2:
            err7 = True
        elif f1:
            pass
        elif f2:
            pass
        elif k1 == k2:
            err7 = True
    elif t1[0] == t3[0] and t2[0] != t3[0]:
        pass
    elif t1[0] != t3[0] and t2[0] == t3[0]:
        pass
    else:
        err7 = True

    if not err6 and not err7:
        btn1clicked(t1,t2,t3,r,v1)
    elif err6:
        mb.showerror('Невозможно выполнить','Некоторые точки совпадают. \
Невозможно построить угол.')
    elif err7:
        mb.showerror('Невозможно выполнить','Некоторые точки лежит на одной\
 прямой. Невозможно построить угол.')
        
def btn1clicked(t1,t2,t3,r,v1):
    g1 = False
    g2 = False
    g3 = False
    g4 = False
    g5 = False
    g6 = False
    g7 = False
    g8 = False

    h = res(t1,t2,t3,r)
##    print(v1)
    
    mt1 = max(t1)
    mt2 = max(t2)
    mt3 = max(t3)
    mh0 = max(h[0])
    mh1 = max(h[1])
    nt1 = min(t1)
    nt2 = min(t2)
    nt3 = min(t3)
    nh0 = min(h[0])
    nh1 = min(h[1])
    M = max(mt1,mt2,mt3,mh1,mh0)
##    print(M)
    
    mi = min(nt1,nt2,nt3,nh0,nh1)
##    print('mi',mi)
    mi -=1 
    M -= mi
    d = 500/(M+2)
##    print(M, d)
    if t1[0] != t3[0]:
        k1 = (t1[1] - t3[1])/(t1[0] - t3[0])
        b1 = t1[1] - k1*t1[0]
    else:
        g1 = True
    if t2[0] != t3[0]:
        k2 = (t2[1] - t3[1])/(t2[0] - t3[0])
        b2 = t2[1] - k2*t2[0]
    else:
        g2 = True
    if not g1 and not g2:
        xp = (b2-b1)/(k1-k2)
        yp = k1*xp + b1
    elif g1:
        xp = t1[0]
        yp = k2*xp + b2
    elif g2:
        xp = t2[0]
        yp = k1*xp+b1
        
    if not g1:
        l1 = c.create_line(0,(pr(mi,k1,b1)-mi)*d,\
                           500*d,(pr(500+mi,k1,b1)-mi)*d,fill ='gray90')
    else:
        l1 = c.create_line((t1[0]-mi)*d,0,(t1[0]-mi)*d,500*d,\
                           fill ='gray90')
    if not g2:
        l2 = c.create_line(0,(pr(mi,k2,b2)-mi)*d,500*d,\
                           (pr(500+mi,k2,b2)-mi)*d,\
                           fill = 'gray90')
    else:
        l2 = c.create_line((t2[0]-mi)*d,0,(t2[0]-mi)*d,500*d,fill = 'gray90')
    if h[0][0] < t1[0] <t3[0]:
        l3 = c.create_line((h[0][0]-t1[0]-mi)*d,(pr(h[0][0]-t1[0],k1,b1)-mi)*d,\
                       (h[0][0]-mi)*d,(h[0][1]-mi)*d, fill = 'blue')
    elif h[0][0] > t1[0] > t3[0]:
        l3 = c.create_line((h[0][0]+t1[0]-mi)*d,(pr(h[0][0]+t1[0],k1,b1)-mi)*d,\
                       (h[0][0]-mi)*d,(h[0][1]-mi)*d, fill = 'blue')
    elif h[0][0] == t1[0] == t3[0]:
        if h[0][1] > t1[1] > t3[1] or h[0][1] < t1[1] < t3[1]:
            l3 = c.create_line((h[0][0]-mi)*d,(2*h[0][1]-t1[1]-mi)*d,\
                               (h[0][0]-mi)*d,(h[0][1]-mi)*d, fill = 'blue')
        else:
            l3 = c.create_line((t1[0]-mi)*d,(t1[1]-mi)*d,\
                       (h[0][0]-mi)*d,(h[0][1]-mi)*d, fill = 'blue')
    else:  
        l3 = c.create_line((t1[0]-mi)*d,(t1[1]-mi)*d,\
                       (h[0][0]-mi)*d,(h[0][1]-mi)*d, fill = 'blue')
    if h[1][0] < t2[0] <t3[0]:
        l4= c.create_line((h[1][0]-t2[0]-mi)*d,(pr(h[1][0]-t2[0],k2,b2)-mi)*d,\
                       (h[1][0]-mi)*d,(h[1][1]-mi)*d, fill = 'blue')
    elif h[1][0] > t2[0] > t3[0]:
        l4= c.create_line((h[1][0]+t2[0]-mi)*d,(pr(h[1][0]+t2[0],k2,b2)-mi)*d,\
                       (h[1][0]-mi)*d,(h[1][1]-mi)*d, fill = 'blue')
    elif h[1][0] == t2[0] == t3[0]:
        if h[1][1] > t2[1] > t3[1] or h[1][1] < t2[1] < t3[1]:
            l3 = c.create_line((h[1][0]-mi)*d,(2*h[1][1]-t2[1]-mi)*d,\
                               (h[1][0]-mi)*d,(h[1][1]-mi)*d, fill = 'blue')
        else:
            l4= c.create_line((t2[0]-mi)*d,(t2[1]-mi)*d,\
                       (h[1][0]-mi)*d,(h[1][1]-mi)*d, fill = 'blue')
    else:
        l4= c.create_line((t2[0]-mi)*d,(t2[1]-mi)*d,\
                       (h[1][0]-mi)*d,(h[1][1]-mi)*d, fill = 'blue')

    if v1 == 1:
        # Скругление прямой
        if h[0][0] != h[1][0]:
            k = (h[0][1] - h[1][1])/(h[0][0]-h[1][0])
            b = h[1][1] - k * h[1][0]
##            print(k,b)
##            print(h)
            l3 = c.create_line((h[0][0]-mi)*d,(h[0][1]-mi)*d,\
                               (h[1][0]-mi)*d,(h[1][1]-mi)*d,\
                               fill='blue')
            text1 = 'y = '+str(k)+'*x + '+str(b)
            text.insert(END,text1) 
        else:
            text1 = 'x = '+str(h[0][0])
            text.insert(END,text1)
            l3 = c.create_line((h[0][0]-mi)*d,(h[0][1]-mi)*d,\
                               (h[1][0]-mi)*d,(h[1][1]-mi)*d,\
                               fill='blue')
    if v1 == 2:
        # Скругление окружностью
##        print(h)
        p = []
        t = []
        if g1:
            kp1 = 0
        elif k1 == 0:
            g5 = True
        else:
            kp1 = -1/k1
        if not g5:
            bp1 = h[0][1]-kp1*h[0][0]
            t.append(kp1)
            t.append(bp1)
            p.append(t)

        t =[]
        if g2:
            kp2 = 0
        elif k2 == 0:
            g6 = True
        else:
            kp2 = -1/k2
        if not g6:
            bp2 = h[1][1]-kp2*h[1][0]
            t.append(kp2)
            t.append(bp2)
            p.append(t)
        if not g5 and not g6:
            xo = (p[1][1]-p[0][1])/(p[0][0]-p[1][0])
            yo = p[1][0]*xo + p[1][1]
        elif g5:
            xo = h[0][0]
            yo = kp2*xo + bp2
        elif g6:
            xo = h[1][0]
            yo = kp1*xo + bp1

        R = sqrt((xo-h[0][0])**2+(yo-h[0][1])**2)

##        print(R,xo,yo)

        text1 = '(x-('+str(xo)+'))**2 + (y-('+str(yo)+'))**2 = '+\
                str(R*R)
        text.insert(END,text1)

        o = c.create_oval((xo-R-mi)*d,(yo+R-mi)*d,(xo+R-mi)*d,(yo-R-mi)*d,\
                          outline = 'gray90')

        if h[0][0] != xo:
            w1 = (h[0][1]-yo)/(h[0][0]-xo)
##            print(w1,h[0][1],h[0][0])
        else:
            g7 = True
        if g7:
            w1 = 90
        elif w1 > 0:
            w1 = 180-acos(sqrt(1/(1+w1*w1)))*360/2/pi
        else:
            w1 = 180-acos(-sqrt(1/(1+w1*w1)))*360/2/pi

        if h[1][0] != xo:
            w2 = (h[1][1]-yo)/(h[1][0]-xo)
##            print(w2)
        else:
            g8 = True
        if g8:
            w2 = 90
        elif w2>0:
            w2 = 180-acos(sqrt(1/(1+w2*w2)))*360/2/pi
        else:
            w2 = 180-acos(-sqrt(1/(1+w2*w2)))*360/2/pi

        w3 = max(w1,w2)
        w4 = min(w1,w2)
##        print(w1,w2)

        if h[0][1] > yo and h[1][1] > yo:
##            print('<')
##            print(w4+180,180+w3)
            ar = c.create_arc((xo-R-mi)*d,(yo+R-mi)*d,(xo+R-mi)*d,(yo-R-mi)*d,\
                              start=w4+180,extent=w3-w4,\
                              outline='blue',style = ARC)
        elif h[0][1] < yo and h[1][1] < yo:
##            print('>')
            ar = c.create_arc((xo-R-mi)*d,(yo+R-mi)*d,(xo+R-mi)*d,(yo-R-mi)*d,\
                              start=w4,extent=w3-w4,\
                              outline='blue',style = ARC)
        elif xp < xo:
            ar = c.create_arc((xo-R-mi)*d,(yo+R-mi)*d,(xo+R-mi)*d,(yo-R-mi)*d,\
                              start=w3,extent=180+w4-w3,\
                              outline='blue',style = ARC)
        else:
            ar = c.create_arc((xo-R-mi)*d,(yo+R-mi)*d,(xo+R-mi)*d,(yo-R-mi)*d,\
                              start=w3+180,extent=180+w4-w3,\
                              outline='blue',style = ARC)
        
    if v1 == 3:
        # Скругление параболой
        p = []
        t = []
        if g1:
            kp1 = 0
        elif k1 == 0:
            g5 = True
        else:
            kp1 = -1/k1
        if not g5:
            bp1 = h[0][1]-kp1*h[0][0]
            t.append(kp1)
            t.append(bp1)
            p.append(t)

        t =[]
        if g2:
            kp2 = 0
        elif k2 == 0:
            g6 = True
        else:
            kp2 = -1/k2
        if not g6:
            bp2 = h[1][1]-kp2*h[1][0]
            t.append(kp2)
            t.append(bp2)
            p.append(t)
        if not g5 and not g6:
            xo = (p[1][1]-p[0][1])/(p[0][0]-p[1][0])
            yo = p[1][0]*xo + p[1][1]
        elif g5:
            xo = h[0][0]
            yo = kp2*xo + bp2
        elif g6:
            xo = h[1][0]
            yo = kp1*xo + bp1

        R = sqrt((xo-h[0][0])**2+(yo-h[0][1])**2)

##        print(R,xo,yo)

        if xo != xp:
            kz = (yo - yp)/(xo-xp)
            bz = yo - kz*xo
        else:
            g3 = True
        if g3:
            kn = 0
            bn = yp
        elif kz == 0:
            g4 = True
        elif not g3:
            kn = -1/kz
            bn = yp - kn*xp

            
        if not g4:
            if kn>= 0:
                cosn = sqrt(1/(1+kn*kn))
                sinn = sqrt(1 - cosn*cosn)
            else:
                cosn = -sqrt(1/(1+kn*kn))
                sinn = sqrt(1 - cosn*cosn)

            dy = yp*cosn-xp*sinn
            dx = (dy*sinn+xp)/cosn
##            print('dxdy=',dx,dy)
            
            X1,Y1 = new(h[0][0],h[0][1],cosn,sinn,dx,dy)
            X2,Y2 = new(h[1][0],h[1][1],cosn,sinn,dx,dy)

            Xp,Yp = new(xp,yp,cosn,sinn,dx,dy)
        else:
            X1,Y1 = h[0][1],-h[0][0]
            X2,Y2 = h[1][1], -h[1][0]
            Xp,Yp = yp, -xp

        K2 = (Y2-Yp)/(X2-Xp)
        K1 = (Y1-Yp)/(X1-Xp)

        a0 = (K1-K2)/(2*X1-2*X2)
        b0 = K1 - 2*a0*X1
        c0 = Y1 - a0*X1*X1 - b0*X1
        text1 = 'Y = '+str(a0)+'*X*X + '+str(b0)+'*X + '+str(c0)
        text.insert(END,text1)
        if not g4:
            text2 = '\n' +'Y = ' + str(cosn)+'*y - x*'+str(sinn)
            text3 = '\n' + 'X = ( Y*'+str(sinn)+'+ x) / '+str(cosn)
        else:
            text2 = '\n' + 'Y = -x'
            text3 = '\n' + 'X = y'
        text.insert(END,text2)
        text.insert(END,text3)

##        print (X2,X1)
        if not g4:
            if X1<X2:
                X = X1
                flag = 1
                while X < X2:
##                    print(X)
                    Y = a0*X*X+b0*X+c0
                    x,y = past(X,Y,cosn,sinn,dx,dy)
##                    print(x,y)
                    t = c.create_oval((x-mi)*d-0.5,(y-mi)*d-0.5,(x-mi)*d+0.5,\
                                      (y-mi)*d+0.5,fill = 'blue',outline='blue')
                    if X2-X1 >10:
                        X +=1
                    else:
                        X += (X2-X1+1)/d
                    if flag:
                        n1 = x
                        n2 = y
                        flag = 0
                    else:
                        N = c.create_line((n1-mi)*d,(n2-mi)*d,\
                                            (x-mi)*d,(y-mi)*d,width=2,fill='blue')
                        n1 = x
                        n2 = y 
                    if X > X2:
                        break
            else:
                X = X1
                flag = 1
                while X > X2:
##                    print(X)
                    Y = a0*X*X+b0*X+c0
                    x,y = past(X,Y,cosn,sinn,dx,dy)
##                    print(x,y)
                    t = c.create_oval((x-mi)*d-0.5,(y-mi)*d-0.5,\
                                      (x-mi)*d+0.5,\
                                      (y-mi)*d+0.5,fill = 'blue',outline='blue')
                    if X1-X2 > 10:
                        X -=1
                    else:
                        X -= (X1-X2+1)/d
                
                    if flag:
                        n1 = x
                        n2 = y
                        flag = 0
                    else:
                        N = c.create_line((n1-mi)*d,(n2-mi)*d,\
                                        (x-mi)*d,(y-mi)*d,width=2,fill='blue')
                        n1 = x
                        n2 = y 
                    if X < X2:
                        break
            Y = a0*X2*X2+b0*X2+c0
            x,y = past(X2,Y,cosn,sinn,dx,dy)
            N = c.create_line((n1-mi)*d,(n2-mi)*d,\
                                (x-mi)*d,(y-mi)*d,width=2,fill='blue')
        else:
            X = X1
            flag = 1
            while X < X2:
##                print(X)
                Y = a0*X*X+b0*X+c0
                x,y = -Y,X 
##                print(x,y)
                t = c.create_oval((x-mi)*d-0.5,(y-mi)*d-0.5,\
                                  (x-mi)*d+0.5,(y-mi)*d+0.5,\
                                    fill = 'blue',outline='blue')
                if X2-X1 >10:
                    X +=1
                else:
                    X += (X2-X1+1)/d
                if flag:
                    n1 = x
                    n2 = y
                    flag = 0
                else:
                    N = c.create_line((n1-mi)*d,(n2-mi)*d,\
                                        (x-mi)*d,(y-mi)*d,width=2,fill='blue')
                    n1 = x
                    n2 = y 
            X = X1
            flag = 1
            while X > X2:
##                print(X)
                Y = a0*X*X+b0*X+c0
                x,y = -Y,X
##                print(x,y)
                t = c.create_oval((x-mi)*d-0.5,(y-mi)*d-0.5,(x-mi)*d+0.5,(y-mi)*d+0.5,\
                                    fill = 'blue',outline='blue')
                if X1-X2 > 10:
                    X -=1
                else:
                    X -= (X1-X2+1)/d
            
                if flag:
                    n1 = x
                    n2 = y
                    flag = 0
                else:
                    N = c.create_line((n1-mi)*d,(n2-mi)*d,\
                                    (x-mi)*d,(y-mi)*d,width=2,fill='blue')
                    n1 = x
                    n2 = y 
            Y = a0*X2*X2+b0*X2+c0
            x,y = -Y,X2
            N = c.create_line((n1-mi)*d,(n2-mi)*d,\
                                (x-mi)*d,(y-mi)*d,width=2,fill='blue')
        
            
def btn2clicked():
    c.delete('all')
    text.delete('1.0',END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
        
root = Tk()

c1 = Canvas(root, width = 780, height=630)
c1.pack()

l1 = Label(root, text = 'Введите координаты точек:\n Формат ввода: x y')
l1.place( x = 565, y = 10)

l2 = Label(root, text= ' 1:')
l2.place(x = 540, y = 50)
t1 = StringVar()
e1 = Entry(root, textvariable = t1)
e1.place(x = 580, y = 50)

l3 = Label(root, text = ' 2:')
l3.place(x = 540, y = 80)
t2 = StringVar()
e2 = Entry(root,textvariable = t2)
e2. place(x = 580, y = 80)

l4 = Label(root, text = 'Вершина:')
l4.place(x = 520, y = 110)
t3 = StringVar()
e3 = Entry(root, textvariable = t3)
e3.place(x = 580,y = 110 )

l5 = Label(root, text = 'Введите расстрояние от точки пересечения\n до \
начала скругления:')
l5.place(x = 520, y = 140)
r = StringVar()
e4 = Entry(root, textvariable = r)
e4.place(x = 580, y = 180)

v = IntVar()
l6 = Label (root, text = 'Выберите способ скругления:')
l6.place(x = 550, y = 210)

rb1 = Radiobutton(root,text ='скруглить с помощью прямой', variable = v,\
                  value=1)
rb2 = Radiobutton(root,text = 'скруглить с помощью окружности',variable = v,\
                  value = 2)
rb3 = Radiobutton(root,text = 'скруглить с помощью параболы',variable = v,\
                  value = 3)
rb1.place(x = 550, y = 230)
rb2.place(x = 550, y = 250)
rb3.place(x = 550, y = 270)

btn1 = Button(root, text = 'Решить', command = proverka)
btn1.place(x = 625, y = 310)

text = Text(root,width=94, height = 5)
text.place(x = 10, y = 520)


btn2 = Button(root,text = 'Очистить все', command = btn2clicked)
btn2.place(x = 610, y = 470)
c = Canvas(root,width=500,height=500,bg ='gray80')
c.place(x = 10, y = 10)

root.mainloop()

