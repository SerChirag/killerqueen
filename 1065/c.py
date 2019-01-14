import sys, math
from sys import stdin, stdout
rem =10**9+7
sys.setrecursionlimit(10 ** 6+5)
take = lambda: map(int, stdin.readline().split())

n,k = take()
a = take()
a.sort(reverse = True)
mi = min(a)
ma = max(a)
count = 0
p = []
curr = ma
for i in range(1,n):
    val = curr-(a[i]*i)
    p.append(val)
    curr += a[i]
p.append(curr)
times = 0
prev = 0
curr = p[0]
prev = 0
for i in range(1,n):
    if(curr >= k):
        times += curr/k
        curr = curr%k
        prev = p[i]
    else:
        curr += (p[i] - prev)

if(curr > 0):
    times += 1
print times