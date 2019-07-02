##
##N = int(input('Введите количество строк:'))
##
##a = ['']*N
##for i in range(N):
##    a[i] = input('Введите строку без пробелов:')
##M = len(a[i])
##
##for i in range(N):
##    for j in range(M):
##        if a[i][j] in ['1','2','3','4','5','6','7','8','9','0']:
##            for t in range(N):
##                s =''
##                for g in range(0,j):
##                    s+=a[t][g]
##                s+='#'
##                for g in range(j+1,M):
##                    s+=a[t][g]
##                a[t] = s
##            a[i]='#'*M
##
##for i in a:
##    print(i)
##

U = int(input('Введите длину массива:'))

b = [0]*U

for i in range(U):
    print('b[',i,']=',end='')
    b[i] = int(input())
print(b)
for i in range(U):
    k = 0
    for j in range(U):
        if b[i] == b[j] and i != j:
            b[j] = ''
            k +=1
    if k == 0:
        b[i] = ''
print(b) 
