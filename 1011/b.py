n,m = map(int,raw_input().split())
a = map(int,raw_input().split())
from collections import Counter
a  = dict(Counter(a)).values()
p = 0
for i in range(1,m+1):
    k = 0
    for j in a:
        k += j/i
    if(k >= n):
        p+=1
    else:
        break

print p