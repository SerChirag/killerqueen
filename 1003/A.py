n = input()
a = map(int,raw_input().split())
d = {}
for i in a:
    try:
        po = d[i]
        d[i] += 1
    except:
        d[i] = 1

m = 0
for i in d:
    m = max(d[i],m)
print m