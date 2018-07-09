n = input()
a = map(int,raw_input().split())
d = {}
for i in range(n-1,-1,-1):
    try:
        po = d[a[i]+1]
        d[a[i]] = [po[0]+1,i,po[1]]
    except:
        d[a[i]] = [1,i,-1]


m = 0
me = 0
for i in d:
    if(d[i][0] > m):
        m = d[i][0]
        me = i

o = []
while(1):
    try:
        po = d[me]
        o.append(po[1])
        me+=1
        if(po[2] == -1):
            break
    except:
        break

print len(o)
for i in o:
    print i+1,
print 