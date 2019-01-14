import sys, math
from sys import stdin, stdout
rem =10**9+7
sys.setrecursionlimit(10 ** 6+5)
take = lambda: map(int, stdin.readline().split())

out = []
t = int(stdin.readline())
for q in range(t):
    s,a,b,c = take()
    n = s/c
    m = (n/a)*b
    out.append(str(n+m))

stdout.write("\n".join(out))