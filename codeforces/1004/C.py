n = input()
a = map(int,raw_input().split())
l = {}
r = []
ro = {}
for i in range(n):
    try:
        po = l[a[i]]
    except:
        l[a[i]] = (i)
count = 0
for i in range(n-1,-1,-1):
    r.append(count)
    try:
        po = ro[a[i]]
    except:
        ro[a[i]] = 1
        count += 1
r.append(count)
r.reverse()
c = 0
for i in l:
    c += r[l[i]+1]
print c