n,m = map(int,raw_input().split())
if(m == 0):
    print n,n
elif(n == 1):
    print 1,1
else:
    nk = 0
    while(nk<=n):
        val = (pow(nk,2) - nk)/2
        if(val >= m):
            break
        else:
            nk+=1   
    mx = max(0,n-nk)
    mn = n
    mk = m
    while(mn > 0 and mk>0):
        mn-=2
        mk-=1
    mn = max(0,mn)
    print mn,mx 