from sys import stdin,stdout
n,ma = map(int,stdin.readline().split())
a = []
count = 0
for i in range(n):
    chi = stdin.readline()
    chi = chi.strip("\n")
    b = []
    for i in chi:
        b.append(i)
    a.append(b)
    for j in b:
        if(j == '#'):
            count+=1

m = {}
for i in range(n-2):
    for j in range(ma-2):
        flag = 1
        for x in range(3):
            for y in range(3):
                if(x == 1 and y == 1):
                    continue
                elif(a[x+i][y+j] == '#'):
                    continue
                else:
                    flag = 0
                    break
        
        if(flag):
            for x in range(3):
                for y in range(3):
                    if(x == 1 and y == 1):
                        pass
                    else:
                        tup = (x+i,y+j)
                        try:
                            po = m[tup]
                        except:
                            m[tup] = 1

acc = len(m)
if(acc == count):
    stdout.write("YES")
else:
    stdout.write("NO")
