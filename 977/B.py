n = input()
s = raw_input()
d = {}
for i in range(n-1):
    c = s[i]+s[i+1]
    try:
        po = d[c]
        d[c] += 1
    except:
        d[c] = 1

m = 0
l = -1
for i in d:
    if(d[i] > m):
        m = max(m,d[i])
        l = i
print l