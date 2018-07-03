from collections import deque
p = map(int,raw_input().split())
n = p[0]
m = p[1]
gold = map(int,raw_input().split())
ma = {}
vis = {}
for i in range(m):
    k = map(int,raw_input().split())
    vis[k[0]] = 1
    vis[k[1]] = 1
    try:
        po = ma[k[0]]
        ma[k[0]].append(k[1])
    except:
        ma[k[0]] = []
        ma[k[0]].append(k[1])

    try:
        po = ma[k[1]]
        ma[k[1]].append(k[0])
    except:
        ma[k[1]] = []
        ma[k[1]].append(k[0]) 

lo = []
for i in vis:
    if(vis[i]):
        j = []
        q = deque()
        q.append(i)
        while(q):
            node = q.popleft()
            vis[node] = 0
            j.append(node)
            for g in ma[node]:
                if(vis[g]):
                    q.append(g)
            
        lo.append(j)

ghanta = {}
for i in range(1,n+1):
    ghanta[i] = 1
s = 0
for i in lo:
    mi = 10000000001
    for p in i:
        ghanta[p] = 0
        mi = min(mi,gold[p-1])
    s+=mi

for i in ghanta:
    if(ghanta[i]):
        s+=gold[i-1]

print s




