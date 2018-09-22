n,m,k = map(int,raw_input().split())
if(m<k):
    p = m*1.0/k
    print p
elif(m==k):
    p = ((m-1)*1.0/k) + (1.0/k)*(1.0/(n+1))
    print p
else:
    b = m-k+1
    p = ((k-1)*1.0/k) 
    p2 = ((1.0/k)*b/(1.0*(b+n)))
    print p+p2