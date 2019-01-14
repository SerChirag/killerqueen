from collections import deque
from sys import stdin,stdout
n,m = map(int,stdin.readline().split())
r,c = map(int,stdin.readline().split())
x,y = map(int,stdin.readline().split())
a = []
for i in range(n):
    b = stdin.readline()
    b = b.strip('\n')
    b = list(b)
    a.append(b)
count = 0
r-=1
c-=1
d = deque()
d.append((r,c,x,y))
a[r][c] = '+'
while(d):
    r,c,x,y = d.pop()
    try:
        po = a[r-1][c]
        if(po == '.'):
            d.append((r-1,c,x,y))
            a[r-1][c] = '+'
    except:
        pass
    try:
        po = a[r+1][c]
        if(po == '.'):
            d.append((r+1,c,x,y))
            a[r+1][c] = '+'
    except:
        pass
    try:
        po = a[r][c-1]
        if(x>0 and po == '.'):
            d.appendleft((r,c-1,x-1,y))
            a[r][c-1] = '+'
    except:
        pass
    try:
        po = a[r][c+1]
        if(y>0 and po == '.'):
            d.appendleft((r,c+1,x,y-1))
            a[r][c+1] = '+'
    except:
        pass
    

for i in a:
    for j in i:
        if(j == '+'):
            count+=1

stdout.write(str(count))