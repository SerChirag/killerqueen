from collections import Counter
n = input()
a = map(int,raw_input().split())
c  = Counter(a)
count = 0
elem = 0
maxi = 0
for i in c:
    if(c[i] == 1):
        count+=1
    else:
        if(c[i] > maxi):
            elem = i
            maxi = c[i]
if(count == n and (count%2 == 1)):
    print "NO"
elif(count%2 == 0):
    print "YES"
    m = {}
    for i in c:
        if(c[i] == 1):
            if(count%2 == 0):
                m[i] = 'A'
            else:
                m[i] = 'B'
            count-=1
        else:
            m[i] = 'A'
    s = ""
    for i in a:
        s += m[i]
    print s
elif(maxi==2):
    print "NO"
else:
    print "YES"
    m = {}
    for i in c:
        if(i == elem):
            pass
        elif(c[i] == 1):
            if(count%2 == 0):
                m[i] = 'A'
            else:
                m[i] = 'B'
            count-=1
        else:
            m[i] = 'A'
    s = ""
    flag = 0
    for i in a:
        if(i == elem):
            if(flag == 0):
                s += 'A'
                flag = 1
            else:
                s += 'B'
        else:
            s += m[i]
    print s
    