from sys import *
n = int(stdin.readline())
a = map(int,stdin.readline().split())
b = map(int,stdin.readline().split())
for i in range(n):
    b[i] = b[i]-1
cost = 0
visit = ['c']*n
for i in range(n):
    node = i
    while(visit[node]=='c'):
        visit[node] = i
        node = b[node]
    
    if(visit[node]==i):
        nex = b[node]
        mini = a[node]
        while(nex != node):
            mini = min(mini,a[nex])
            nex = b[nex]
        cost += mini
stdout.write(str(cost))
