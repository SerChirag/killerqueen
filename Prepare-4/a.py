n,m = map(int,raw_input().split())
a = map(int,raw_input().split())
m = {}
for i in range(1,len(a)):
    m[a[i]] = 1
steps = []
for i in range(n):
    b = map(int,raw_input().split())
    steps.append(b[1:])

flag = 0
ns = steps[::]
steps.extend(ns)
count = 0
for i in steps:
    count += 1
    for j in i:
        try:
            po = m[j]
            del m[j]
        except:
            m[j] = 1
    if(len(m) == 0):
        flag = 1
        break

if(flag):
    print count
else:
    print -1
