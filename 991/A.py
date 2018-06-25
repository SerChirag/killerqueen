k = map(int,raw_input().split())
a = k[0]
b = k[1]
c = k[2]
n = k[3]
t = a + b - c
if(n < max(a,b,c)):
    print -1
elif(c > min(a,b)):
    print -1
elif(t>=n):
    print -1
elif(t < 0):
    print -1
else:
    print n-t
