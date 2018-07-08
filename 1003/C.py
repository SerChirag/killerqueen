a = map(int,raw_input().split())
n = a[0]
k = a[1]
a = map(int,raw_input().split())
m = 0
for i in range(0,n-k+1):
    s = 0
    for j in range(k):
        s += a[i+j]
    avg = s*1.0/k
    m = max(m,avg)
    curr = k+1
    for j in range(i+k,n):
        s += a[j]
        avg = s*1.0/curr
        m = max(m,avg)
        curr +=1

print m
    