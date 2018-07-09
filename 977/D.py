n = input()
a = map(int,raw_input().split())
d = {}
for i in a:
    d[i] = 1

start = 0
for i in a:
    f2 = 0
    f3 = 0
    if(i%2==1):
        f2 = 1
    else:
        try:
            po = d[i/2]
        except:
            f2 = 1
    try:
        po = d[i*3]
    except:
        f3 = 1
    
    if(f2 and f3):
        start = i
        break

o = []
o.append(start)
curr = start
for j in range(n-1):
    try:
        po = d[curr*2]
        o.append(curr*2)
        curr = curr*2
    except:
        try:
            po = d[curr/3]
            o.append(curr/3)
            curr = curr/3
        except:
            pass
for i in o:
    print i,
print