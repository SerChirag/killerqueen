n,m = map(int,raw_input().split())
a = []
for i in range(m):
    a.append(map(int,raw_input().split()))
from collections import deque
for q in a:
    num = q[0]
    k = q[1]
    s = "{0:b}".format(num)
    s = s[::-1]
    for i in range(n-len(s)):
        s+='0'
    s = s[::-1]
    k = k%n
    s = s[k:n] + s[0:k]
    print int(s,2)