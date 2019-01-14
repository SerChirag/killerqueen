n,r = map(int,raw_input().split())
a = map(int,raw_input().split())
b = [0]*n
vag = 0
for i in a:
    if(i == 1):
        vag +=1
for i in range(n):
    if(a[i]==1):
        ll = max(0,i-r+1)
        rl = min(n,i+r)
        for j in range(ll,rl):
            b[j]+=1

flag = 0
for i in b:
    if(i == 0):
        flag = 1
        break
if(flag==1):
    print -1
else:
    less = 0
    for i in range(n):
        if(a[i]==1):
            ll = max(0,i-r+1)
            rl = min(n,i+r)
            flag = 1
            for j in range(ll,rl):
                if(b[j]>1):
                    pass
                else:
                    flag = 0
                    break
            if(flag==1):
                less+=1
                for j in range(ll,rl):
                    b[j]-=1
    print vag-less
                
