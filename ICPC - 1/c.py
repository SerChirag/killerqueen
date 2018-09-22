from sys import *
t = int(stdin.readline())
loda = []
from collections import Counter
for q in range(t):
    n = int(stdin.readline())
    a = map(int,stdin.readline().split())
    p = Counter(a)
    l = list(p.items())
    l.sort(key = lambda x : x[0])
    maxi = 0
    if(len(l) == 1):
        maxi = 0
    else:
        for i in l:
            maxi = max(maxi,i[1])
        for i in range(1,len(l)):
            if(l[i][0]-l[i-1][0] == 1):
                maxi = max(maxi,l[i][1]+l[i-1][1])
        loda.append(str(maxi))
stdout.write("\n".join(loda))
