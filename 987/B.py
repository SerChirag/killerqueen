from math import log
a = map(int,raw_input().split())
x = a[0]
y = a[1]
lx = log(x)
ly = log(y)
p1 = y*lx
p2 = x*ly
if(p1 > p2):
    print ">"
elif(p1 < p2):
    print "<"
else:
    print "="