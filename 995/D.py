n = input()
a = []
for i in range(n):
    b = map(int,raw_input().split())
    a.append(b)
for i in range(len(a)):
    a[i].append(i)
    a[i].append((a[i][0])**2 + (a[i][1])**2)
a.sort(key = lambda x:x[3],reverse=True)
x = 0
y = 0
for i in range(0,n):
    p = (x-a[i][0])**2 + (y-a[i][1])**2
    q = (x+a[i][0])**2 + (y+a[i][1])**2
    if(p < q):
        x = x-a[i][0]
        y = y-a[i][1]
        a[i].append(1)
    else:
        x = x+a[i][0]
        y = y+a[i][1]
        a[i].append(-1)

a.sort(key = lambda x:x[2])
for i in a:
    print i[4],
print