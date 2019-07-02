# Дан текст массивом строк. Ни одна из строк,кроме последней,
# не заканчивается точкой. Ни одна из строк не является полным предложением.
# Программа удаляет заданное слово из всего текста, заменяет одно слово
# на другое и выравнивает текст по правому, левому краю и по ширине.
# Так же находит предложение, которое содержит максимальное число слов,
# в которых каждая буква повторяется не менее двух раз.
# Сушина АД ИУ7-11б

# alf,alf1 - алфавиты
# text - текст
# key - номер команды
# r - текст как матрица слов
# mass - текст как массив предложений
# i,w,t,st,w2,w3,h,f - рабочие переменные

alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alf1 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТВУФХЦЧШЩЪЫЬЭЮЯ'
alf2 = 'abcdefghijklmnopqrstuvwxyz'
alf3 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

##text = ['q q','zzzzzzzzzzz']
##text = ['а а','бббббббббб']


text =['Ваня встретил своих друзей по дороге домой. Он рассказал им,',\
    'что его мама запретила ему гулять. Это случилось, потому что он',\
    'получил двойку за последнюю контрольную по математике. Он не подготовился,',\
    'потому что он гулял с друзьями и пришел домой слишком поздно. За это',\
    'мама и папа его наказали.']

def pr(text):
    print()
    for t in range(len(text)):
        print(text[t])          
    print()
    print('Что вы хотите сделать с текстом?')
    print(' 1. Удалить слово \n',\
            '2. Заменить слово \n',\
            '3. Выровнять по левому краю \n',\
            '4. Выровнять по правому краю \n',\
            '5. Выровнять по ширине \n',\
            '6. Найти предложение, содержащее максимальное количество слов,\n\
 в которых каждая буква входит не менее двух раз\n',\
            '7. Выйти из программы')
    print()

def udalit(text,r):
    k = 1
    while k:
        count = 0
        print()
        w = input('Введите слово, которое необходимо удалить:')
        if w.isalpha():
            w2 = w.lower()
            for i in range(len(text)):
                for j in range(len(r[i])):
                    if len(w2) == len(r[i][j]):
                        o = 1
                        e = r[i][j].lower() 
                        for t in range(len(w2)):
                            if e[t] == w2[t]:
                                p = 1
                            else:
                                o = 0
                        if o:
                            count+=1
            if count == 0:
                print('Такого слова нет в тексте. Введите другое слово.')
            else:
                break
        else:
            print()
            print('Некорректный ввод.Введите еще раз.')
    w = w.lower() 
    print()
    for i in range(len(r)):
        for j in range(len(r[i])):
            if len(w) == len(r[i][j]):
                o = 1
                e = r[i][j].lower() 
                for t in range(len(w)):
                    if e[t] == w[t]:
                        p = 1
                    else:
                        o = 0
                if o:
                    r[i][j] = ''

    print()
    for i in range(len(r)):
        for j in range(len(r[i])):
            print(r[i][j],end='')
        print()
    for i in range(len(text)):
        text[i] = ''
        for j in range(len(r[i])):
            text[i] += r[i][j]

def zamenit(text,r):
    k = 1
    l = 0
    while k:
        count = 0
        print()
        w2 = input('Введите слово, которое необходимо заменить:')
        if w2.isalpha():
            w = w2.lower()
            for i in range(len(text)):
                for j in range(len(r[i])):
                    if len(w) == len(r[i][j]):
                        o = 1
                        e = r[i][j].lower() 
                        for t in range(len(w)):
                            if e[t] == w[t]:
                                p = 1
                            else:
                                o = 0
                        if o:
                            count+=1
            if count == 0:
                  print('Такого слова нет в тексте. Введите другое слово.')
                  l += 1
                  if l == 7:
                      l = 0
                      pr(text)
            else:
                break
        else:
            print('Некорректный ввод. Введите еще раз.')
            l +=1
            if l == 7:
                l = 0
                pr(text)
    w2 = w2.lower()
    while k:
        w3 = input('Введите слово, на которое необходимо заменить:')
        if w3.isalpha():
            break
        else:
            print('Некорректный ввод. Введите еще раз.')
            l +=1
            if l == 7:
                l = 0
                pr(text)
    print()
    w3 = w3.lower() 
    for i in range(len(r)):
        for j in range(len(r[i])):
            if len(w2) == len(r[i][j]):
                o = 1
                e = r[i][j].lower() 
                for t in range(len(w2)):
                    if e[t] == w2[t]:
                        p = 1
                    else:
                        o = 0
                if o:
                    if r[i][j][0] in alf1:
                        r[i][j] = w3[0].upper()+w3[1:]
                    else:
                        r[i][j] = w3

    print()
    for i in range(len(r)):
        for j in range(len(r[i])):
            print(r[i][j],end='')
        print()
    for i in range(len(text)):
        text[i] = ''
        for j in range(len(r[i])):
            text[i] += r[i][j]
    
def levo(text):
    print()
    print('По левому краю:')
    for i in range(len(text)):
        while text[i][0] == ' ':
            text[i] = text[i][1:]
        print(text[i])

def pravo(text):
    print()
    print('По правому краю:')
    for i in range(len(text)):
        while text[i][len(text[i])-1] == ' ':
            text[i] = text[i][:-1]
        f = 79-len(text[i])
        print(' '*f,text[i])
    print()

def shir(r,text):
    m = len(text[0])
    for i in range(len(text)):
        if len(text[i]) > m:
            m = len(text[i])
    print()
    print('По ширине:')
    for i in range(len(r)):
        if len(r[i])>1 and r[i][0] !='':
            co = text[i].count(' ')
            d = m - len(text[i]) + co-1
            j = 0
            s = 0
            l = 0
            while s <= d:
                r[i][j] += ' '
                s += 1
                l += 1
                j = l%(len(r[i])-1)
        for a in range(len(r[i])-1):
            print(r[i][a], end='')
        print(r[i][len(r[i])-1])
        
def poisk(text):
    mass = []
    c = ''
    for i in range(len(text)):
        j = 0
        while j < len(text[i]) :
            c += text[i][j]
            if text[i][j] in ['.','?','!']:
                mass.append(c)
                c = ''
            j+=1
        c += ' '
    if c != '':
        mass.append(c)
    ru = []
    for i in range(len(mass)):
        ru.append([]) 
    for i in range(len(mass)):
        q = mass[i]
        k = 0
        while k < len(q):
            w =''
            p = 1
            while q[k] in alf or q[k] in alf1 or q[k] in [',','.','!','?','-']\
                  or q[k] in alf2 or q[k] in alf3:
                w += q[k]
                k += 1
                if k == len(q):
                   break
            else:
                if w != '':
                    w = w.lower()
                    ru[i].append(w)
                    p = 0
            k+=1
        if w != '' and p:
            w =  w.lower() 
            ru[i].append(w)
    ka = [0]*len(ru)
    pa = 0
    for i in range(len(ru)):
        for y in range(len(ru[i])):
            u = 0
            b = ru[i][y]
            z = b[0]
            x = 0 
            while b.count(z) >= 2:
                x +=1
                if x == len(b):
                    u = 1
                    break
                z = b[x]
            if u:
                ka[i] += 1
                pa = 1
    v = max(ka)
    if pa: 
         print()
         print('Искомое предложение:',ka.index(v))
         print(mass[ka.index(v)])
         print()
    else:
        print()
        print('Нет подходящего предложения.')
        print()
        
    for t in range(len(text)):
         print(text[t])

print()
for t in range(len(text)):
    print(text[t])

flag1 = 1
while flag1:
    flag = 1
    while flag:

        print()
        print('Что вы хотите сделать с текстом?')
        print(' 1. Удалить слово \n',\
             '2. Заменить слово \n',\
             '3. Выровнять по левому краю \n',\
             '4. Выровнять по правому краю \n',\
             '5. Выровнять по ширине \n',\
             '6. Найти предложение, содержащее максимальное количество слов,\n\
 в которых каждая буква входит не менее двух раз\n',\
             '7. Выйти из программы')
        print()
        key = input('Введите номер операции:')
        if key in ['1','2','3','4','5','6','7']:
            break
        else:
            print()
            print('Неверно! Попробуйте еще раз.')
            print()
            for t in range(len(text)):
                 print(text[t])
            print()
    if key == '1':
        r = []
        for i in range(len(text)):
            r.append([])
        for i in range(len(text)):
             q = text[i]
             k = 0
             while k < len(q):
                 w =''
                 p = 1
                 while q[k] in alf or q[k] in alf1\
                       or q[k] in alf2 or q[k] in alf3:
                     w += q[k]
                     k += 1
                     if k == len(q):
                         break
                 else:
                     if w != '':
                         r[i].append(w)
                         p = 0
                     if q[k] in [',','.','!','-',' ']:
                         r[i].append(q[k])
                 k+=1
             if w != '' and p:
                 r[i].append(w)
        udalit(text,r)
    elif key == '2':
        r = []
        for i in range(len(text)):
            r.append([])
        for i in range(len(text)):
             q = text[i]
             k = 0
             while k < len(q):
                 w =''
                 p = 1
                 while q[k] in alf or q[k] in alf1\
                       or  q[k] in alf2 or q[k] in alf3:
                     w += q[k]
                     k += 1
                     if k == len(q):
                         break
                 else:
                     if w != '':
                         r[i].append(w)
                         p = 0
                     if q[k] in [',','.','!','-',' ']:
                         r[i].append(q[k])
                 k+=1
             if w != '' and p:
                 r[i].append(w)
        
        zamenit(text,r)
    elif key == '3':
        le = text.count(' ')
        i=0
        while le>0:
            if text[i] == ' ':
                del(text[i])
                le -=1
            i+=1
            
        if len(text) == 1 or len(text) == 0:
            print()
            print(text[0])
        else:
            levo(text)
    elif key == '4':
        le = text.count(' ')
        i=0
        while le>0:
            if text[i] == ' ':
                del(text[i])
                le -=1
            i+=1
            
        if len(text) == 1 or len(text) == 0:
            print()
            print(text[0])
        else:
            pravo(text)
    elif key == '6':
        poisk(text)
    elif key == '5':
        le = text.count(' ')
        i=0
        while le>0:
            if text[i] == ' ':
                del(text[i])
                le -=1
            i+=1
            
        if len(text) == 1 or len(text) == 0:
            print()
            print(text[0])
        else:
            for i in range(len(text)):
                while text[i][0] == ' ':
                     text[i] = text[i][1:]
                while text[i][len(text[i])-1] == ' ':
                     text[i] = text[i][:-1]
            r = ['']*len(text)
            for i in range(len(text)):
                r[i] = text[i].split()
            fl = 0 
            for i in range(len(text)):
                if len(r[i]) == 1:
                    fl +=1
                    u = i
            if fl == 1:
                m = len(text[0])
                for i in range(len(text)):
                    if len(text[i]) > m:
                        m = len(text[i])
                if len(r[u][0]) == m:
                    shir(r,text)
                else:
                    print()
                    print('Невозможно выровнять по ширине.')
                    print()
                    for t in range(len(text)):
                        print(text[t])
            elif fl > 1:
                print()
                print('Невозможно выровнять по ширине.')
                print()
                for t in range(len(text)):
                    print(text[t])
            else:
                shir(r,text)
    elif key == '7':
        break


            
