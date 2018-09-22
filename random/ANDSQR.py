def chiggy(a,start,end):
    p = a[start]
    for i in range(start,end):
        p = p&a[i]
    return p

a = [1,3,3,4,5,6,7,8,9]
l1 = chiggy(a,0,6)
l2 = chiggy(a,0,3)
l3 = chiggy(a,3,6)
print l1,l2,l3