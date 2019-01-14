n = input()
a = raw_input()
from collections import Counter
v = []
for i in a:
    v.append(i)
c = Counter(v)
s = ""
for i in c:
    s += i*c[i]
print s