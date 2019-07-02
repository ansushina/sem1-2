#Работа с бинарными файлами. Программа работает с файлом, выводит для
# пользователя меню. Дает возможность создать файл, открыть файл, посмотреть
# все элементы файла, добавить новую запись в файл, найти элемент в базе данных,
# удалить элемент из базы данных.

# Сушина АД ИУ7-11б

#
#
#
#
#
#
#

import pickle

mass = ['фильм','режиссер','год выпуска','жанр']

kolvo = dict()
kolvo['text.txt'] = 6

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
        if filename[-4:] == '.txt':
            break
        else:
            print('Неверно! Введите еще раз.')
    f = open(filename,'wb')
    u = 0
    while k:
        d = dict()
        for i in range(len(mass)):
            print('Введите ',mass[i],':',sep='',end='')
            d[mass[i]] = input()    
        pickle.dump(d,f)
        p = input('y/n:')
        u += 1 
        if p == 'n':
            break
    kolvo[filename] = u
    f.close()

def o(kolvo,filename):
    b = []
    f = open(filename,'rb')
    for i in range(kolvo[filename]):
        fn = pickle.load(f)
        b.append(fn)
    f.close()
    return(b)

def smotret(a):
    for j in range(len(a[0])):
        print('{:20}'.format(mass[j]),end='')
    for i in range(len(a)):
        for j in range(len(a[i])):
            print('{:20}'.format(a[i][mass[j]]),end='')
    print()

##def ishodn(kolvo):
##    b = []
##    f = open('text.txt','rb')
##    for i in range(kolvo['text.txt']):
##        fn = pickle.load(f)
##        b.append(fn)
##    f.close()
##    smotret(b)

def zapisat(kolvo,filename):
    f = open(filename,'ab')
    d = dict()
    for i in range(len(mass)):
        print('Введите ',mass[i],':',sep='',end='')
        d[mass[i]] = input()
    pickle.dump(d,f)
    kolvo[filename] +=1
    f.close()
    o(kolvo,filename)
    

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
            print('Введите',mass[0],'для поиска:',end='')
            h = input()
            o = 0
            for i in range(len(a)):
                if a[i][mass[0]] == h:
                    o +=1
            if o:
                break
            print()
            print('Неверно! Введите еще раз.')
            print() 
        for i in range(len(a)):
            if a[i][mass[0]] == h:
                print()
                for j in range(len(a[i])):
                    print('{:20}'.format(a[i][mass[j]]),end='')
    elif num == '2':
        while True:
            print('Введите',mass[1],'для поиска:',end='')
            h = input()
            o=0
            for i in range(len(a)):
                if a[i][mass[1]] == h:
                    o+=1
            if o:
                break
            print()
            print('Неверно! Введите еще раз.')
            print() 
        for i in range(len(a)):
            if a[i][mass[1]] == h:
                print()
                for j in range(len(a[i])):
                    print('{:20}'.format(a[i][mass[j]]),end='')
    elif num == '3':
        while True:
            print('Введите ',mass[0],':',sep='',end='')
            h1 = input()
            o=0
            for i in range(len(a)):
                if a[i][mass[0]] == h1:
                    o+=1
            if o:
                break
            print()
            print('Неверно! Введите еще раз.')
            print()
        while True:
            print('Введите ',mass[1],':',sep='',end='')
            h2 = input()
            o = 0
            for i in range(len(a)):
                if a[i][mass[1]] == h2 and a[i][mass[0]] == h1 :
                    o += 1
            if o:
                break
            print()
            print('Неверно! Введите еще раз.')
            print() 
        for i in range(len(a)):
            if a[i][mass[0]] == h1 and a[i][mass[1]] == h2:
                print()
                for j in range(len(a[i])):
                    print('{:20}'.format(a[i][mass[j]]),end='')
def udalit(kolvo,filename,b):
    print('По какому критерию хотите удалять?\n',\
          '1.',mass[0],'\n',\
          '2.',mass[1],'\n',\
          '3.',mass[0],'и', mass[1],'\n')
    num = input('Введите номер критерия:')
    if num == '1':
        while True:
            print('Введите',mass[0],'для удаления:',end='')
            h = input()
            o = 0
            for i in range(len(a)):
                if a[i][mass[0]] == h:
                    o +=1
            if o:
                break
            print()
            print('Неверно! Введите еще раз.')
            print() 
        r = []
        for i in range(len(b)):
            if b[i][mass[0]] != h:
                r.append(b[i])
            else:
                kolvo[filename] -= 1
        f = open(filename,'wb')
        for i in range(len(r)):
            pickle.dump(r[i],f)
        f.close()
    elif num == '2':
        while True:
            print('Введите',mass[1],'для удаления:',end='')
            h = input()
            o = 0
            for i in range(len(a)):
                if a[i][mass[1]] == h:
                    o +=1
            if o:
                break
            print()
            print('Неверно! Введите еще раз.')
            print()
        r = []
        for i in range(len(b)):
            if b[i][mass[1]] != h:
                r.append(b[i])
            else:
                kolvo[filename] -= 1
        f = open(filename,'wb')
        for i in range(len(r)):
            pickle.dump(r[i],f)
        f.close()
    elif num == '3':
        while True:
            print('Введите ',mass[0],':',sep='',end='')
            h1 = input()
            o = 0
            for i in range(len(a)):
                if a[i][mass[0]] == h1:
                    o+=1
            if o:
                break
            print()
            print('Неверно! Введите еще раз.')
            print()
        while True:
            print('Введите ',mass[1],':',sep='',end='')
            h2 = input()
            o = 0
            for i in range(len(a)):
                if a[i][mass[1]] == h2 and a[i][mass[0]] == h1 :
                    o +=1
            if o:
                break
            print()
            print('Неверно! Введите еще раз.')
            print()
        r = [] 
        for i in range(len(a)):
            if a[i][mass[0]] == h1 and a[i][mass[1]] == h2:
                kolvo[filename] -= 1
            else:
                r.append(b[i])
        f = open(filename,'wb')
        for i in range(len(r)):
            pickle.dump(r[i],f)
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
        while True:
            filename = input('Введите название файла:')
            if filename[-4:] == '.txt':
                break
            else:
                print()
                print('Неверно! Введите еще раз.')
                print()

        a = o(kolvo,filename)
        print('Файл',filename,'открыт.') 
    elif key == '3':
        if filename != '':
            smotret(a)
        else:
            print('Файл не открыт. Откройте файл.')
    elif key == '4':
        if filename != '':
            zapisat(kolvo,filename)
        else:
            print('Файл не открыт. Откройте файл.')
    elif key == '5':
        if filename != '':
            naiti(a,mass)
        else:
            print('Файл не открыт. Откройте файл.')
    elif key == '6':
        if filename != '':
            udalit(kolvo,filename,b)
        else:
            print('Файл не открыт. Откройте файл.')
    elif key == '7':
        break
    
    



