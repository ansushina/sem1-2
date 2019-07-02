# Программа для кодировки строки шифром виженера
# Сушина АД ИУ7-11б

# alf - алфавит
# a -строка
# mat - мартица алфавита
# i,j,k,u,t,p,s,q - рабочие переменные
# key - ключевое слово

key = input('key:')
a = input('word:') 

alf =['А', 'Б', 'В', 'Г', 'Д', 'Е','Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М',\
      'Н','О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ',\
      'Ы','Ь', 'Э', 'Ю', 'Я']

mat = []
for i in range (len(alf)):
    mat.append(['']*len(alf))

for i in range(len(alf)):
    mat[0][i] = alf[i]

for i in range(len(alf)):
    mat[i] = alf[i:]+alf[:i]
k =''
for i in range(len(key)):
    if key[i].isalpha():
        t = 1
        u = key[i]
        if not key[i] in alf:
            u = key[i].upper()
            if not u in alf:
                t = 0
        if t:
            k += u
if k == '':
    print('Неверный ключ. Слово нельзя закодировать.')
else:
    j = 0
    p = 0
    s = ''
    for i in range(len(a)):
        if a[i].isalpha():
            t = 1
            q = a[i]
            if not q in alf:
                if i == 0:
                    s += ' ' 
                q = a[i].upper()
                if not q in alf:
                    t = 0
                else:
                    q = mat[alf.index(q)][alf.index(k[j])]
                    q = q.lower()
            else:
                q = mat[alf.index(a[i])][alf.index(k[j])]
            if t:
                s += q
                p += 1
                j = p%(len(k))
            else:
                s += a[i]
        else:
            s += a[i]
    print()
    print('Закодированное слово:',s)
