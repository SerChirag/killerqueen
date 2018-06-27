n = input()
a = map(int,raw_input().split())
b = []
for i in a:
    if(i != 0):
        b.append(i)

m = {}
for i in b:
    m[i]=1
l = m.keys()
print len(m)