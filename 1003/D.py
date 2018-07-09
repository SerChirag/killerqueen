a = map(int,raw_input().split())
n = a[0]
q = a[1]
a = map(int,raw_input().split())
d = {}
for i in a:
    try:
        po = d[i]
        d[i] += 1
    except:
        d[i] = 1

l = d.keys()
l.sort(reverse = True)
for t in range(q):
    b = input()
    c = 0
    for i in l:
        f = min(d[i],b/i)
        c += f
        b -= i*f
        if(b == 0):
            break
    
    if(b):
        print -1
    else:
        print c