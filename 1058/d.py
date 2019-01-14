from fractions import gcd
n,m,k = map(int,raw_input().split())
flag = 1
if(k%2 == 0):
    k /= 2
    flag = 0
if(m*n%k == 0):
    g = gcd(k,n)
    a = n/g
    k = k/g
    b = m/k
    if(flag):
        if(a<n):
            a *= 2
        else:
            b *= 2
    print "YES"
    print 0,0
    print 0,a
    print b,0
else:
    print "NO"