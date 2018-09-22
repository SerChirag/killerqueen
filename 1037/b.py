n,s = map(int,raw_input().split())
a = map(int,raw_input().split())
a.sort()
k = (n/2)
m1 = 0
m2 = 0
if(a[k] == s):
    print 0
elif(a[k]>s):
    count = 0
    for i in range(k,-1,-1):
        if(a[i]<=s):
            break
        else:
            count += abs(a[i]-s)
    print count
else:
    count = 0
    for i in range(k,n):
        if(a[i]>=s):
            break
        else:
            count += abs(a[i]-s)
    print count
    
