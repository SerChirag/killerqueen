a = raw_input()
b = raw_input()
m = {}
for i in range(len(b)):
    s = ""
    for j in range(i,len(b)):
        s += b[j]
        m[s] = 1

count = 0
for i in range(len(a)):
    s = ""
    for j in range(i,len(a)):
        s += a[j]
        try:
            po = m[s]
            count+=1
        except:
            pass

print count