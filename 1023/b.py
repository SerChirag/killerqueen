n,k = map(int,raw_input().split())
if(k<=n):
    if(k%2 == 0):
        print (k/2)-1
    else:
        print k/2

else:
    mid = k/2
    mid+=1
    if(mid<=n):
        print (n-mid)+1
    else:
        print 0
