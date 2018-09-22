import string
n,k = map(int,raw_input().split())
s = raw_input()
m = {}
for i in s:
    try:
        po = m[i]
        m[i]+=1
    except:
        m[i]=1
al = string.ascii_uppercase[:k]
flag = 1
mi = 10000000
for i in al:
    try:
        po = m[i]
        mi = min(m[i],mi)
        del m[i]
    except:
        flag = 0
        break
if(flag == 1):
    s = mi*k
    for i in m:
        s += m[i]
    print s

else:
    print 0