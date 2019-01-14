from sys import stdin,stdout
n = int(stdin.readline())
m = {}
for q in range(n-1):
    x,y = map(int,stdin.readline().split())
    try:
        po = m[x]
        m[x].append(y)
    except:
        m[x] = [y]
    try:
        po = m[y]
        m[y].append(x)
    except:
        m[y] = [x]

a = map(int,stdin.readline().split())
pos = {}
for i in range(len(a)):
    pos[a[i]] = i
def ke(popo):
    return pos[popo]
for i in m:
    m[i].sort(key = ke)

done = {}
curr = [1]
tour = [1]
done[1] = 1
while(curr):
    nex = []
    for i in curr:
        try:
            for j in m[i]:
                aa = done.get(j,0)
                if(aa == 0):
                    tour.append(j)
                    done[j]=1
                    nex.append(j)
        except:
            pass
    curr = nex

if(a == tour):
    stdout.write("Yes")
else:
    stdout.write("No")
