# Защита сортировки
# Сортировка вставками
# Сушина А ИУ7-21б

from random import randint
import time

def sort(a):
    for i in range(1,len(a)):
        if a[i-1] > a[i]:
            k = a[i]
            j = i-1
            while k < a[j] and j>=0:
                a[j],a[j+1] = a[j+1], a[j] 
                j -= 1
    return a

n = randint(0,14)
a = [randint(0,20) for i in range(n)]
print('Исходный массив',a)
b = a.copy()
t1 = time.time()
b = sort(b)
t2 = time.time()
t = t2-t1
print('Отсортированный массив:',b)
print('Время:',t)

        
