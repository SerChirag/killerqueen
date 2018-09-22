n,x = map(int,raw_input().split())
a = map(int,raw_input().split())
n = {}
from collections import Counter
o = Counter(a)
o = dict(o)
flag = 0
mini = 100
for i in a:
    po = o[i]
    if(po > 1):
        mini = 0
        flag = 1
        break
    else:
        do = x&i
        if(do == i):
            pass
        else:
            try:
                po = o[do]
                mini = min(mini,1)
                flag = 1
                n[do] = 1
            except:
                try:
                    po = n[do]
                    mini = min(mini,2)
                    flag = 1
                except:
                    n[do] = 1
if(flag):
    print mini
else:
    print -1
