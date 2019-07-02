# Работа с бинарными файлами. Программа работает с файлом, выводит для
# пользователя меню. Дает возможность создать файл, открыть файл, посмотреть
# все элементы файла, добавить новую запись в файл, найти элемент в базе данных,
# удалить элемент из базы данных.

# Сушина АД ИУ7-11б

# mass - массив названий
# li,di - переменные для сохранения названий файлов
# filename - имя файла 
# a - массив словарей из файла
# i,j,o,h,k,fl,d,p,b,num,h1,h2,r,key -рабочие переменные 

import pickle
import os.path
import os

li = os.listdir()
di = []
for i in range(len(li)):
    if not '.' in li[i]: 
        di.append(li[i])


def file():
    li = os.listdir()
    di = []
    for i in range(len(li)):
        if not '.' in li[i]: 
            di.append(li[i])
    for i in range (len(di)):
        print(di[i])
    return di
    

mass = ['фильм','режиссер','год выпуска','жанр']


filename = ''

def menu():
    print()
    print('Что вы хотите сделать?')
    print(' 1. Создать новый файл.\n',\
          '2. Открыть имеющийся файл.\n',\
          '3. Просмотреть все элементы файла.\n',\
          '4. Добавить новую запись в файл.\n',\
          '5. Найти элемент в базе данных.\n',\
          '6. Удалить элемент из базы данных.\n',\
          '7. Выйти из программы.')
    
def sozdat(mass):
    k = 1
    while True:
        filename = input('Введите название файла:')
        if filename in di:
            print()
            fl = input('Такой файл уже существует. Введите "y" чтобы заменить.')
            if fl == 'y' or fl == 'у':
                break
            else:
                print('Введите название другого файла.')
        else:
            break
    f = open(filename,'wb')
    m = []
    pickle.dump(m,f)
    f.close()
    print()
    print('Хотите заполнить файл?')
    print()
    g = input('Введите "y", чтоб заполнить.')
    if g == 'y' or g == 'у':
        while k:
            d = dict()
            print(mass[0],':',sep='',end='')
            d[mass[0]] = input()
            while True:
                print(mass[1],':',sep='',end='')
                d1 = input()
                if d1.isalpha():
                    d[mass[1]] = d1
                    break
                print()
                print('Неверно! Введите еще раз.')
            while True:
                print(mass[2],':',sep='',end='')
                d1 = input()
                if d1.isdigit():
                    if 0 < int(d1) < 2018:
                        d[mass[2]] = d1
                        break
                print()
                print('Неверно! Введите еще раз.')
            while True:
                print(mass[3],':',sep='',end='')
                d1 = input()
                if d1.isalpha():
                    d[mass[3]] = d1
                    break
                print()
                print('Неверно! Введите еще раз.')
            m.append(d)
            p = input('Введите "y", чтобы закончить:')
            if p == 'у' or p == 'y':
                break
        f = open(filename,'wb')
        pickle.dump(m,f)
        f.close()

def o(filename):
    b = []
    f = open(filename,'rb')
    b = pickle.load(f)
    f.close()
    return(b)

def smotret(a,mass):
    for j in range(len(mass)):
        print('{:20}'.format(mass[j]),end='')
    print()
    print()
    for i in range(len(a)):
        for j in range(len(a[i])):
            print('{:20}'.format(a[i][mass[j]]),end='')
        print()
    print()

def zapisat(a,filename):
    f = open(filename,'wb')
    d = dict()
    print(mass[0],':',sep='',end='')
    d[mass[0]] = input()
    while True:
        print(mass[1],':',sep='',end='')
        d1 = input()
        if d1.isalpha():
            d[mass[1]] = d1
            break
        print('Неверно! Введите еще раз.')
    while True:
        print(mass[2],':',sep='',end='')
        d1 = input()
        if d1.isdigit():
            if 0 < int(d1) < 2018:
                d[mass[2]] = d1
                break
        print('Неверно! Введите еще раз.')
    while True:
        print(mass[3],':',sep='',end='')
        d1 = input()
        if d1.isalpha():
            d[mass[3]] = d1
            break
        print('Неверно! Введите еще раз.')
    
    a.append(d)
    pickle.dump(a,f)
    f.close()

def naiti(a,mass):
    print('По какому критерию хотите искать?\n',\
          '1.',mass[0],'\n',\
          '2.',mass[1],'\n',\
          '3.',mass[0],'и', mass[1],'\n')
    while True:
       num = input('Введите номер критерия:')
       if num in ['1','2','3']:
           break
       else:
            print()
            print('Неверно! Введите еще раз.')
            print() 
    if num == '1':
        while True:     
            print(mass[0],':',sep='',end='')
            h = input()
            h = h.lower()
            o = 0
            for i in range(len(a)):
                if a[i][mass[0]].lower() == h:
                    o +=1
            if o:
                break
            print()
            print('Нет таких элементов. Введите еще раз.')
            print()
        print()
        for j in range(len(mass)):
            print('{:20}'.format(mass[j]),end='')
        print()
        for i in range(len(a)):
            if a[i][mass[0]].lower() == h:
                print()
                for j in range(len(a[i])):
                    print('{:20}'.format(a[i][mass[j]]),end='')
    elif num == '2':
        while True:
            print(mass[1],':',sep='',end='')
            h = input()
            h = h.lower()
            o=0
            for i in range(len(a)):
                if a[i][mass[1]].lower() == h:
                    o+=1
            if o:
                break
            print()
            print('Нет таких элементов. Введите еще раз.')
            print()
        print()
        for j in range(len(mass)):
            print('{:20}'.format(mass[j]),end='')
        print()
        for i in range(len(a)):
            if a[i][mass[1]].lower() == h:
                print()
                for j in range(len(a[i])):
                    print('{:20}'.format(a[i][mass[j]]),end='')
    elif num == '3':
        while True:
            print(mass[0],':',sep='',end='')
            h1 = input()
            h1 = h1.lower()
            o=0
            for i in range(len(a)):
                if a[i][mass[0]].lower() == h1:
                    o+=1
            if o:
                break
            print()
            print('Нет таких элементов. Введите еще раз.')
            print()
        while True:
            print(mass[1],':',sep='',end='')
            h2 = input()
            h2 = h2.lower()
            o = 0
            for i in range(len(a)):
                if a[i][mass[1]].lower() == h2 and\
                   a[i][mass[0]].lower() == h1 :
                    o += 1
            if o:
                break
            print()
            print('Нет таких элементов. Введите еще раз.')
            print()
        print()
        for j in range(len(mass)):
            print('{:20}'.format(mass[j]),end='')
        print()
        for i in range(len(a)):
            if a[i][mass[0]].lower() == h1 and\
               a[i][mass[1]].lower() == h2:
                for j in range(len(a[i])):
                    print('{:20}'.format(a[i][mass[j]]),end='')
                print()
def udalit(filename,b):
    print('По какому критерию хотите удалять?\n',\
          '1.',mass[0],'\n',\
          '2.',mass[1],'\n',\
          '3.',mass[0],'и', mass[1],'\n')
    while True:
       num = input('Введите номер критерия:')
       if num in ['1','2','3']:
           break
       else:
            print()
            print('Нет таких элементов. Введите еще раз.')
            print() 
    if num == '1':
        while True:
            print(mass[0],':',sep='',end='')
            h = input()
            h = h.lower()
            o = 0
            for i in range(len(a)):
                if a[i][mass[0]].lower() == h:
                    o +=1
            if o:
                break
            print()
            print('Нет таких элементов. Введите еще раз.')
            print() 
        r = []
        for i in range(len(b)):
            if b[i][mass[0]].lower() != h:
                r.append(b[i])
        f = open(filename,'wb')
        pickle.dump(r,f)
        f.close()
    elif num == '2':
        while True:
            print(mass[1],':',sep='',end='')
            h = input()
            h = h.lower()
            o = 0
            for i in range(len(a)):
                if a[i][mass[1]].lower() == h:
                    o +=1
            if o:
                break
            print()
            print('Нет таких элементов. Введите еще раз.')
            print()
        r = []
        for i in range(len(b)):
            if b[i][mass[1]].lower() != h:
                r.append(b[i])
        f = open(filename,'wb')
        pickle.dump(r,f)
        f.close()
    elif num == '3':
        while True:
            print(mass[0],':',sep='',end='')
            h1 = input()
            h1 = h1.lower()
            o = 0
            for i in range(len(a)):
                if a[i][mass[0]].lower() == h1:
                    o+=1
            if o:
                break
            print()
            print('Нет таких элементов. Введите еще раз.')
            print()
        while True:
            print(mass[1],':',sep='',end='')
            h2 = input()
            h2 = h2.lower()
            o = 0
            for i in range(len(a)):
                if a[i][mass[1]].lower() == h2 and\
                   a[i][mass[0]].lower() == h1 :
                    o +=1
            if o:
                break
            print()
            print('Нет таких элементов. Введите еще раз.')
            print()
        r = [] 
        for i in range(len(a)):
            if a[i][mass[0]].lower() != h1 or\
               a[i][mass[1]].lower() != h2:
                r.append(b[i])
        f = open(filename,'wb')
        pickle.dump(r,f)
        f.close()

while True:
    menu()
    while True:
        print()
        key = input('Введите номер команды:')
        print()
        if key in ['1','2','3','4','5','6','7']:
            break
        else:
            print('Неверно! Введите еще раз.')
    if key == '1':
        sozdat(mass)
    elif key == '2':
        di = file()
        print()
        while True:
            filename = input('Введите название файла:')
            if os.path.isfile(filename) and filename in di:
                break
            else:
                print()
                print('Неверно! Введите еще раз.')
                print()
        print()
        print('Файл',filename,'открыт.') 
    elif key == '3':
        if filename != '':
            a = o(filename)
            if a != []:
                smotret(a,mass)
            else:
                print('Файл', filename, 'пуст.')
        else:
            print('Файл не открыт. Откройте файл.')
    elif key == '4':
        if filename != '':
            a = o(filename)
            zapisat(a,filename)
            print()
            print('Запись добавлена!')
        else:
            print('Файл не открыт. Откройте файл.')
    elif key == '5':
        if filename != '':
            a = o(filename)
            naiti(a,mass)
            print()
        else:
            print('Файл не открыт. Откройте файл.')
    elif key == '6':
        if filename != '':
            a = o(filename)
            udalit(filename,a)
            print()
            a = o(filename)
            smotret(a,mass) 
        else:
            print('Файл не открыт. Откройте файл.')
    elif key == '7':
        break
    
    



