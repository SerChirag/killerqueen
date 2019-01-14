from sys import stdout,stdin
n,m = map(int,stdin.readline().split())
mod = 998244353
bo = m
a = stdin.readline()
b = stdin.readline()
a = a.strip('\n')
b = b.strip('\n')
a = a[::-1]
b = b[::-1]
s = [0]*200001
for i in range(m):
    xo = ""
    for j in range(min(bo,n)):
        if(a[j] == "1" and b[j] == "1"):
            xo+="1"
        else:
            xo+="0"
    c = 0
    j = 0
    while(j<len(xo) or c==1):
        xomo = 0
        try:
            xomo = int(xo[j])
        except:
            xomo = 0
        temp = (s[j]^xomo)^c
        c = (s[j]&xomo)|(s[j]&c)|(c&xomo)
        s[j] = temp
        j+=1
    bo-=1
    b = b[1:]

flag = 0
susu = ""
s.reverse()
for i in s:
    if(i == 0):
        if(flag==0):
            continue
        else:
            susu+="0"
    else:
        flag = 1
        susu+="1"

susu = susu[::-1]
num = 0
ghoda = 1
for i in range(len(susu)):
    if(susu[i]=='1'):
        num+=ghoda
    num = num%mod
    ghoda = ghoda << 1
stdout.write(str(num))
