t = input()
from sys import *
final = []
from collections import Counter
for q in range(t):
    a = input()
    a = map(int,raw_input().split())
    m = Counter(a)
    l = []
    su = 0
    ghanta = 0
    for i in m:
        if(m[i] >= 2):
            l.append(i)
            if(m[i] >= 4):
                su = 1
                ghanta = i
                break
    if(su == 1):
        final.append(str(ghanta) + " " + str(ghanta) + " " + str(ghanta) + " " + str(ghanta))
    else:
        l.sort()
        if(len(l) == 1):
            final.append(str(l[0]) + " " + str(l[0]) + " " + str(l[0]) + " " + str(l[0]))
        else:
            flag = 0
            mini = 0
            b1 = 0
            b2 = 0
            for i in range(1,len(l)):
                if(flag == 0):
                    mini = (l[i]*1.0/l[i-1])
                    b1 = l[i]
                    b2 = l[i-1]
                    flag = 1
                else:
                    loda = (l[i]*1.0/l[i-1])
                    if(loda < mini):
                        mini = loda
                        b1 = l[i]
                        b2 = l[i-1]
            final.append(str(b2) + " " + str(b2) + " " + str(b1) + " " + str(b1))

print "\n".join(final)