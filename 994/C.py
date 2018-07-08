a = map(int,raw_input().split())
b = map(int,raw_input().split())
l = []
m = []
for i in range(0,len(b),2):
    p = [a[i],a[i+1]]
    l.append(p)

for i in range(0,len(b),2):
    p = [b[i],b[i+1]]
    m.append(p)

flag = 0
for i in l:
    for j in m:
        if((i[0] == j[0]) and (i[1] == j[1])):
            flag = 1
            break

if(flag == 1):
    print "Yes"
else:
    l.sort(key = lambda x:x[1])
    l.sort(key = lambda x:x[0])
    yl = l[0][1]
    xl = l[0][0]
    yh = l[3][1]
    xh = l[3][0]
    xm = 0
    ym = 0
    for i in m:
        xm+= i[0]
        ym+= i[1]
    xm = xm/4.0
    ym = ym/4.0
    for i in m:
        if(i[0]>=xl and i[0]<=xh and i[1]>=yl and i[1]<=yh):
            flag = 1
            break
    
    if(flag == 1):
        print "Yes"
    elif(xm>=xl and xm<=xh and ym>=yl and ym<=yh):
        print "Yes"
    else:
        for i in range(4):
            m[i][0],m[i][1] = m[i][0]+m[i][1],m[i][0]-m[i][1]
        
        for i in range(4):
            l[i][0],l[i][1] = l[i][0]+l[i][1],l[i][0]-l[i][1]

        m.sort(key = lambda x:x[1])
        m.sort(key = lambda x:x[0])
        yl = m[0][1]
        xl = m[0][0]
        yh = m[3][1]
        xh = m[3][0]
        xm = 0
        ym = 0
        for i in l:
            xm+= i[0]
            ym+= i[1]
        xm = xm/4.0
        ym = ym/4.0
        for i in l:
            if(i[0]>=xl and i[0]<=xh and i[1]>=yl and i[1]<=yh):
                flag = 1
                break

        if(flag == 1):
            print "Yes"
        elif(xm>=xl and xm<=xh and ym>=yl and ym<=yh):
            print "Yes"
        else:
            print "No"
        