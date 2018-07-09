from math import log
from sys import stdin, stdout
a = map(int,raw_input().split())
n = a[0]
q = a[1]
a = map(int,raw_input().split())
d = [0]*32
for j in a:
    i = int(log(j,2))
    d[i-1] += 1
d.reverse()
inp = stdin.readlines()
for t in inp:
    b = int(t.strip())
    c = 0
    sw = pow(2,32)
    for j in range(len(d)):
        f = min(d[j],b/sw)
        c += f
        b -= sw*f
        sw /= 2
        if(b == 0):
            break
    
    if(b):
        print -1
    else:
        print c
    
