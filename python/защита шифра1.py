alf='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alf1 ='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
a  = input('word')

k =[]
i = 0
s =''
while i < len(a):
    while a[i] in alf or a[i] in alf1:
        s += a[i]
        i += 1
        if i == len(a):
            break
    else:
        k.append(s)
        s = ''
    i += 1
k.append(s)

b = [] 
for i in range(len(k)):
    if k[i] != '':
         b.append(k[i])

def sort(b):
    mini = b[0]
    for i in range(len(b)):
        j = 0
        r = b[i]
        while j < len(b[i]):
            q = r[j]
            if r[j] in alf1:
                   q = r[j].lower()
                   f = 1
            if alf.index(q) < alf.index(mini[j]):
                mini = b[i] 
                break
            elif alf.index(q) == alf.index(mini[j]):
                j+=1
            else:
                break
    return mini 

d = ''
for h in range(len(b)):
    o = sort(b)
    d += o+' '
    b.remove(o)
print(d)
