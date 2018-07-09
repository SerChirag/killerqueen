n,k = map(int,raw_input().split())
a = map(int,raw_input().split())
a.sort()
prev = a[0]
c = 1
d = []
for i in range(1,n):
    if(a[i] == prev):
        c+=1
    else:
        d.append((prev,c))
        c = 1
        prev = a[i]

d.append((prev,c))
flag = 0
c = 0
element = 0
if(k == 0):
    if(d[0][0] >= 2):
        print d[0][0]-1
    else:
        print -1
else:
    for i in range(len(d)):
        c += d[i][1]
        if(c == k):
            element = d[i][0]
            flag = 1
            break
                        
        if(c > k):
            break

    if(flag and element <= 1000000000):
        print element
    else:
        print -1


