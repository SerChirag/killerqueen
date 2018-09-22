def floydWarshall(graph): 
    for k in range(V): 
        for i in range(V):  
            for j in range(V): 
                dist[i][j] = min(dist[i][j],dist[i][k]+ dist[k][j]) 

from sys import maxint,stdin,stdout
n,m = map(int,stdin.readline().split())
a = []
for i in range(n):
    p = []
    for j in range(n):
        p.append(maxint)
    a.append(p)
q = stdin.readline()
for i in range(m):
    x,y,w = map(int,stdin.readline().split())
    a[x-1][y-1] = w


ql = []
out = []
for i in range(q):
    x,y = map(int,stdin.readline().split())
    out.append(str(a[x-1][y-1]))
stdout.write("\n".join(out))