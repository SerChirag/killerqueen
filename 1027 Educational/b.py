n,q = map(int,raw_input().split())
li = []
for t in range(q):
    x,y = map(int,raw_input().split())
    li.append((x,y))
flag = 0
if(n%2 == 0):
    flag = 1
base = (n**2)/2
if(flag == 0):
    base += 1
for t in range(q):
    x = li[t][0]
    y = li[t][1]
    if((x+y)%2==0):
        if(flag == 1):
            if(y%2 == 0):
                y = y/2
            else:
                y = (y+1)/2
            print 0 + ((x-1)*(n/2) + y)
        else:        
            odd = (x-1)
            loda = n*(odd/2)
            if(odd%2 == 1):
                loda += (n/2)+1
            if(y%2 == 0):
                y = y/2
            else:
                y = (y+1)/2
            print 0 + loda + y

    else:
        if(flag == 1):
            if(y%2 == 0):
                y = y/2
            else:
                y = (y+1)/2
            print base + ((x-1)*(n/2) + (y))
        else:
            odd = (x-1)
            loda = n*(odd/2)
            if(odd%2 == 1):
                loda += (n/2)
            if(y%2 == 0):
                y = y/2
            else:
                y = (y+1)/2
            print base + loda + y

