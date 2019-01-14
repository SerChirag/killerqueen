a = map(int,raw_input().split())
n = a[0]
m = a[1]
a = [0]
ap = map(int,raw_input().split())

a.extend(ap)
a.append(m)
c = 1
if(n%2==1):
    c = -1
sp = 0
sn = 0
r = []
r.append([sp,sn])
for i in range(n,-1,-1):
    if(c==-1):
        sn += c*(a[i+1]-a[i])
    else:
        sp += c*(a[i+1]-a[i])
    r.append([sp,sn])
    c *= -1

r.pop()
r.reverse()
cur = sp
sw = 0
for i in range(len(r)-1):
    if(a[i+1]-a[i]>1):

        gain = abs(r[i][1])-r[i][0]
        if(i%2==0):
            gain -= 1
        else:
            gain += a[i+1]-a[i]-1
        sw = max(sw,gain)

print max(cur+sw,m-(cur+sw))