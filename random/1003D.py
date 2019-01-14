from sys import stdin,stdout
a = map(int,stdin.readline().split())
n = a[0]
q = a[1]
a = map(int,stdin.readline().split())
d = {}
for i in a:
    try:
        po = d[i]
        d[i] += 1
    except:
        d[i] = 1

l = d.keys()
l.sort(reverse = True)
out = []
for t in range(q):
    b = int(stdin.readline())
    c = 0
    for i in l:
        f = min(d[i],b/i)
        c += f
        b -= i*f
        if(b == 0):
            break
    
    if(b):
        out.append("-1")
    else:
        out.append(str(c))

stdout.write("\n".join(out))