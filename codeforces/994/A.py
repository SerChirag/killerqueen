a = map(int,raw_input().split())
a = map(int,raw_input().split())
b = map(int,raw_input().split())
m = {}
for i in b:
    m[i] = 1
for j in a:
    try:
        do = m[j]
        print j,
    except:
        pass

print