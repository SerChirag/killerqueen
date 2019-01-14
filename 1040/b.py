n,k = map(int,raw_input().split())
s = k+1
b = 2*k+1
r = n%b
o = 0
if(k == 0):
    print n
    for i in range(1,n+1):
        print i,
    print
    exit()
if(r == 0):
    a = []
    for i in range(s,n,b):
        a.append(str(i))
elif(r<=s):
    o = s-r
    a = []
    for i in range(s,n-1,b):
        a.append(str(i-o))
    a.append(str(n))
else:
    a = []
    for i in range(s,n,b):
        a.append(str(i))
print len(a)
print " ".join(a)