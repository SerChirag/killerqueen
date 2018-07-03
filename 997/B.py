a = map(int,raw_input().split())
n = a[0]
b = a[1]
a = map(int,raw_input().split())
l = []
o = 0
e = 0
for i in range(n-1):
    if(a[i]%2==0):
        e+=1
    else:
        o+=1
    if(o == e):
        l.append(abs(a[i]-a[i+1]))

l.sort()
c = 0
count = 0
for i in l:
    if(c+i>b):
        break
    else:
        count += 1
        c += i

print count

