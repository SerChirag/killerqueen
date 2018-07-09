a = map(int,raw_input().split())
n = a[0]
d = a[1]
a = map(int,raw_input().split())
if(n==1):
    print 2
else:
    s = 1
    for i in range(n-1):
        if(a[i+1]-a[i] == 2*d):
            s+=1
        elif(a[i+1]-a[i] > 2*d):
            s+=2
        else:
            s+=0        
    s+=1
    print s