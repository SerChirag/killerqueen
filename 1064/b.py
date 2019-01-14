from sys import stdin,stdout
t = int(stdin.readline())
a = []
out = []
for i in range(t):
    q = int(stdin.readline())
    a.append(q)
for i in range(t):
    m = "{0:b}".format(a[i])
    num = 0
    curr = 0
    for i in m:
        if(i == "1"):
            num+=pow(2,curr)
            curr+=1
    num+=1 
    out.append(str(num))

stdout.write("\n".join(out))