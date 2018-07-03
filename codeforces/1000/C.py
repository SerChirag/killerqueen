n = input()
a = []
k = {}
for i in range(n):
    b = map(int,raw_input().split())
    a.append((b[0],1))
    a.append((b[1],-1))

a.sort()
b = []
prev = a[0][0]
print a
tot = a[0][1]
for i in range(1,len(a)):
    if(a[i][0] == prev):
        tot += a[i][1]
    else:
        b.append((prev,tot))
        tot = a[i][1]
        prev = a[i][0]

if(tot!=0):
    b.append((prev,tot))

po = {}
for i in range(n):
    po[i+1] = 0

po[b[0][1]] += 1
for i in range(1,len(b)):
    try:
        po[abs(b[i][1])] += 1
    except:
        pass
    try:
        po[abs(b[i][1]-b[i-1][1])] += abs(b[i][0]-b[i-1][0])-1
    except:
        pass
    print po
for i in po:
    print po[i],
print