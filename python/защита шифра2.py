alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alf1 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТВУФХЦЧШЩЪЫЬЭЮЯ'

a = input('Введите строку:')

k = 0
d =[]
while k < len(a):
    q =''
    p = 1
    while a[k] in alf or a[k] in alf1:
        q += a[k]
        k +=1
        if k == len(a):
            break
    else:
        if q != '':
            d.append(q)
            p = 0
    k +=1
    
if q != '' and p:
    d.append(q)
print()
print('Исходный массив:',d)

for i in range(len(d)):
    for j in range(len(d)-1):
        if len(d[j]) > len(d[j+1]):
            d[j],d[j+1]=d[j+1],d[j]
print()
print('Полученный массив:',d) 

