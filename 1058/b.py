n,d = map(int,raw_input().split())
q = input()
a = []
for j in range(q):
    x,y = map(int,raw_input().split())
    v1 = x+y-d
    v2 = x+y-2*n+d
    v3 = x-y-d
    v4 = -1*(y-x-d)
    if((v1>0 and v2>0) or (v1<0 and v2 <0)):
            print "NO"
    else:
        if((v3>0 and v4>0) or (v3<0 and v4<0)):
            print "NO"
        else:
            print "YES"