n = input()
a = map(int,raw_input().split())
b = map(int,raw_input().split())
m = []
maxint = 10000000000
for i in range(n):
    l = [0]*n
    m.append(l)
mini = []
for i in range(n):
    maxi = maxint
    flag = 0
    for j in range(i+1,n):
        if(a[i] < a[j]):
            flag = 1
            maxi = min(maxi,b[j])
    if(flag == 0):
        mini.append(-1)
    else:
        mini.append(maxi)

flag = 0
cobra = maxint
for i in range(n):
    maxi = maxint
    for j in range(i+1,n):
        if(a[i] < a[j] and mini[j]!=-1):
            cobra = min(cobra,b[i]+b[j]+mini[j])
            flag = 1

if(flag == 0):
    print -1
else:
    print cobra