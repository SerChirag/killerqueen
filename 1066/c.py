from sys import stdin,stdout
out = []
m = {}
t = int(stdin.readline())
l = 0
r = 0
for q in range(t):
    a,b = stdin.readline().split()
    b = int(b.strip('\n'))
    if(q == 0):
        if(a == 'L'):
            m[b] = 0
        else:
            m[b] = 0
    else:
        if(a == 'L'):
            l-=1
            m[b] = l
        elif(a == 'R'):
            r+=1
            m[b] = r
        else:
            po = m[b]
            go = abs(l-po)
            ga = abs(r-po)
            out.append(str(min(go,ga)))

stdout.write("\n".join(out))
            
