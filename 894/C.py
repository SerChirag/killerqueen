n = input()
a = map(int,raw_input().split())
b = min(a)
f = 0
for i in a:
    if(i%b!=0):
        f=1
        break
if(f==1):
    print -1
else:
    print 2*n
    for i in a:
        print i,
        print b,
    print