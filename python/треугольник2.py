# Программа для исселодавния треугольника по известным координатам.
# Проверяет существование треугольника. Находит длины сторон и длину высоты
# треугольника, проведенную из наименьшего угла. Проверяет, является ли
# треугольник равносторонним. Проверяет, находится ли произвольная точка
# внутри треугольника и, если находится, то выводит расстояние от этой точки
# до наиболее удаленной стороны треугольника.
# Сушина АД ИУ7-11б

# A(xa,ya) - первая вершина треугольника 
# B(xb,yb) - вторая вершина треугольника
# C(xc,yc) - третья вершина треугольника
# AB, BC, CA - стороны треугольника
# D(x,y) - произвольная точка 
# h - высота треугольника, проведенная из наименьшего угла треугольника
# m - длина наименьшей стороны
# p, p1, p2, p3 - полупериметры треугольников ABC, DAB, DBC, DCA соответсвенно
# k1, k2, k3 - рабочие переменные
# flag, flag1 - рабочие переменные
# r1, r2, r3 - расстояния от точки D до сторон AB,BC и CA соответсвенно
# rd - расстояние до наиболее удаленной стороны 
# DA, DB, DC - отрезки, соединяющие точку D  и вершины треугольника

from math import sqrt
xa,ya = map(float,input('Введите координаты точки A через пробел:').split())
xb,yb = map(float,input('Введите координаты точки B через пробел:').split())
xc,yc = map(float,input('Введите координаты точки C через пробел:').split())
print()

if xa == xb == xc and ya == yb == yc:
    print('Треугольник не существует. Все точки совпадают.')
    flag = 0
elif xa == xb and ya == yb or xa == xc and ya == yc or xb == xc and yb == yc:
    print('Треугольник не сущетсвует. Две точки совпадают.')
    flag = 0
elif xa == xb == xc or ya == yb == yc:
    print('Треугольник не существует. Все точки лежат на одной прямой.')
    flag = 0
elif xa != xb and xc != xa:
    if (yb-ya)/(xb-xa) == (yc-ya)/(xc-xa):
        print('Треугольник не существует. Все точки лежат на одной прямой.')
        #Проверяем совпадение тангенсов уголов между прямыми AB,CA и осью х
        flag = 0
    else: flag = 1
else: flag = 1

if flag:
    AB = sqrt((xa-xb)**2 + (ya-yb)**2)
    BC = sqrt((xb-xc)**2 + (yb-yc)**2)
    CA = sqrt((xc-xa)**2 + (ya-yc)**2)
    
    print('AB =','{:7.4f}'.format(AB))
    print('BC =','{:7.4f}'.format(BC))
    print('CA =','{:7.4f}'.format(CA))
    print()
    
    p = (AB+BC+CA)/2
    # Находим наименьшую сторону треугольника, так как против нее лежит
    # наименьший угол. Считаем высоту, проведенную к этой стороне.
    m = min(AB, BC, CA)
    h = sqrt(p*(p-AB)*(p-BC)*(p-CA))*2/m
    
    print('Высота, проведенная из наименьшего угла: h =','{:7.4f}'.format(h))
    print()

    if AB == BC == CA:
        print('Треугольник равносторонний.')
    else:
        print('Треугольник не равносторонний.')
    print()

    x,y = map(float,input('Введите координаты точки D через пробел:').split())
    print()
    
    # Определяем лежит ли точка внутри треугольника
    k1 = (xa-x)*(yb-ya) - (xb-xa)*(ya-y)
    k2 = (xb-x)*(yc-yb) - (xc-xb)*(yb-y)
    k3 = (xc-x)*(ya-yc) - (xa-xc)*(yc-y)
    
    # Если все значения одного знака или равны нулю, то точка находится 
    # внутри треугольника.
    if k1 <= 0 and k2 <= 0 and k3 <= 0:
        print('Точка D находится внутри треугольника.')
        flag1 = 1
    elif k1 >= 0 and k2 >= 0 and k3 >= 0:
        print('Точка D находится внутри треугольника.')
        flag1 = 1
    else:
        print('Точка D лежит вне треугольника.')
        flag1 = 0
    print()

    if flag1:
        # Находим длины отрезков, соединяющих точку D с вершинами
        # треугольника. Через площади полученных треугольников находим 
        # расстояния от точки D до всех сторон треугольника ABC.
        DA = sqrt((x-xa)**2 + (y-ya)**2)
        DB = sqrt((x-xb)**2 + (y-yb)**2)
        DC = sqrt((x-xc)**2 + (y-yc)**2)
        p1 = (DA+DB+AB)/2
        p2 = (DB+DC+BC)/2
        p3 = (DC+DA+CA)/2
        r1 = sqrt(p1*(p1-AB)*(p1-DB)*(p1-DA))*2/AB
        r2 = sqrt(p2*(p2-DB)*(p2-DC)*(p2-BC))*2/BC
        r3 = sqrt(p3*(p3-DC)*(p3-DA)*(p3-CA))*2/CA

        rd = max(r1,r2,r3)
        print('Расстояние до наиболее удаленной стороны','{:7.4}'.format(rd))
        
    

    
    
