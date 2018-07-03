a = map(int,raw_input().split())
x = a[0]
k = a[1]
if(k == 0):
    print (2*x)%1000000007
elif(x == 0):
    print 0
else:
    lo = pow(2,k,1000000007)
    ans = lo*(2*x-1) + 1
    print ans%1000000007
