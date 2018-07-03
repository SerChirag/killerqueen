n = input()
a = map(int,raw_input().split())
if(n==1):
    print -1
elif(n == 2 and a[1]==a[0]):
    print -1
else:
    l = min(a)
    m = 0
    f = 0
    index = 0
    for i in range(n):
        if(f == 0 and a[i] == l):
            index = i
            f = 1
        else:
            m += a[i]
    
    if(l == m):
        print -1
    else:
        print 1
        print index+1
    
        

        



