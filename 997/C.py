a = map(int,raw_input().split())
n = a[0]
x = a[1]
y = a[2]
s = raw_input()
prev = s[0]
c = 1
l = []
for i in range(1,n):
    if(s[i] == prev):
        c+=1
    else:
        l.append(prev)
        prev = s[i]
        c = 1

l.append(prev)
c = 0
for i in l:
    if(i == '0'):
        c+=1

if(c == 0):
    print 0
else:

    c1 = x*(c-1) + y
    c2 = c*y
    print (min(c1,c2))
