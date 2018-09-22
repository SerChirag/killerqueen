from sys import stdin,stdout
n = int(stdin.readline())
a = map(int,stdin.readline().split())
m = 0
flag = 0
if(n == 1):
    stdout.write(str(a[0]))
elif(n == 2):
    stdout.write(str(abs(a[1]-a[0])))
else:
    flag = 0
    lastm = 0
    for i in range(n):
        index = 0
        mindex = 0
        mpindex = 0
        prev = "c"
        m = 0
        if(a[i] != "c"):
            if(prev == "c"):
                prev = a[i]
                index = i
            else:
                if(flag == 0):
                    m = max(m,abs(prev-a[i]))
                else:
                    lo = -1*abs(prev)
                    mo = abs(a[i])
                    if(abs(lo-mo)>m):
                        m = abs(lo-mo)
                        mpindex = index
                        mindex = i
                    index = i
                    prev = a[i]
            a[mpindex] = "c"
            a[mindex] = m
            lastm = m
        if(flag == 0):
            flag = 1
    print m