from sys import stdin,stdout

def prime(x):
    s = set([])
    if(x%2 == 0):
        s.add(2)
    while(x%2==0):
        x /= 2
    for i in range(3,int(pow(x,0.5))+1,2):
        if(x%i==0):
            s.add(i)
            while(x%i==0):
                x /= i
    if(x>1):
        s.add(x)
    return s

n = int(stdin.readline())
a = []
for i in range(n):
    x = map(int,stdin.readline().split())
    a.append(x)

s1 = prime(a[0][0])
s2 = prime(a[0][1])
maha = s1 | s2
for i in range(1,n):
    if(len(maha) == 0):
        break
    x = a[i][0]
    y = a[i][1]
    g = set([])
    for i in maha:
        if(x%i == 0 or y%i == 0):
            g.add(i)
    maha = g

if(len(maha)):
    stdout.write(str(maha.pop()))
else:
    stdout.write(str(-1))
