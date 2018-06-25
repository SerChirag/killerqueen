n = input()
a = map(int,raw_input().split())
s = 0
for i in a:
    s += i
v = s/(n*1.0)
if(v >= 4.5):
    print 0
else:
    a.sort()
    j = 0
    for i in a:
        j+=1
        s += 5
        s -= i
        v = s/(n*1.0)
        if(v >= 4.5):
            break
    print j
