n = input()
a = map(int,raw_input().split())
o = []
prev = a[0]
for i in range(1,n):
    if(a[i] > prev):
        prev = a[i]
    else:
        o.append(prev)
        prev = a[i]

o.append(prev)
print len(o)
for i in o:
    print i,
print

