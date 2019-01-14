from sys import setrecursionlimit
setrecursionlimit(200005)
from math import factorial
count = 0
def dfs(root,m):
    global count
    try:
        po = g[root]
        for i in po:
            dfs(i,m+1)
    except:
        if(m == 1):
            pass
        else:
            count += 1
        

n = input()
g = {}
v = [0]*(n+1)
inp = []
for i in range(n-1):
    x,y = map(int,raw_input().split())
    inp.append((x,y))
    v[y] += 1
    v[x] += 1

root = 0
maxi = 0
for i in range(1,n+1):
    if(v[i] > maxi):
        root = i
        maxi = v[i]

for i in range(n-1):
    x = inp[i][0]
    y = inp[i][1]
    if(y == root):
        x,y = y,x
    try:
        po = g[x]
        g[x].append(y)
    except:
        g[x] = [y]

ans = ((n)*(n-1))/2
count = 0
dfs(root,0)
ans += count
print ans