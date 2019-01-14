def check(x):
    if(x%2 == 0):
        return 0
    else:
        for i in range(3,int(pow(x,0.5))+1,+2):
            if(x%i == 0):
                return 0
        return 1


from sys import stdin,stdout
t = input()
a = []
for i in range(t):
    f = map(int,stdin.readline().split())
    a.append(f)
out = []
for i in range(t):
    x = a[i][0]
    y = a[i][1]
    if((x-y) == 1 and check(x+y)):
        out.append("YES")
    else:
        out.append("NO") 
stdout.write("\n".join(out))