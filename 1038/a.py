n = input()
if(n == 1):
    print "No"
elif(n == 2):
    print "No"
else:
    print "Yes"
    o = 0
    e = 0
    ol = []
    el = []
    for i in range(1,n+1):
        if(i%2==0):
            e+=1
            el.append(i)
        else:
            o+=1
            ol.append(i)
    print o,
    for i in ol:
        print i,
    print
    print e,
    for i in el:
        print i,
    print