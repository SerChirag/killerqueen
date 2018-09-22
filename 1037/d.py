from sys import stdin,stdout
n = int(stdin.readline())
m = {}
done = {}
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
curr = {1}
done[1] = 1
flag = 1
ja = 0
while(curr):
    leni = len(curr)
    check = set(a[ja:ja+leni])
    if(check == curr):
        ja+=leni
    else:
        flag = 0
        break

    ne = []
    for i in curr:
        for j in m[i]:
            try:
                po = done[j] 
            except:
                ne.append(j)
                done[j] = 1
    ne = set(ne)
    curr = ne

if(flag == 1):
    stdout.write("Yes")
else:
    stdout.write("No")
