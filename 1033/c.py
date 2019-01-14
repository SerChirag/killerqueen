n = input()
a = map(int,raw_input().split())
ans = [0]*n
m = {}
d = {}
m[n] = 0
for i in range(n):
    d[a[i]] = i

for i in range(n-1,0,-1):
    c = 0 
    pos = d[i]
    for j in range(pos+i,n,i):
        if(a[j] > i and m[a[j]] == 0):
            c = 1
            break
    for j in range(pos-i,-1,-1*i):
        if(a[j] > i and m[a[j]] == 0):
            c = 1
            break
    m[i] = c

s = ""
for i in a:
    if(m[i] == 1):
        s+="A"
    else:
        s+="B"

print s