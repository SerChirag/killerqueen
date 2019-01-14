from sys import stdin,stdout
n = int(stdin.readline())
a = map(int,stdin.readline().split())
m = {}
for i in a:
    try:
        po = m[i-1]
        m[i] = po+1
    except:
        m[i] = 1

m = m.items()
maxi = max(m, key = lambda x : x[1])
out = []
curr = maxi[0]
for i in range(n-1,-1,-1):
    if(a[i] == curr):
        out.append(str(i+1))
        curr-=1
out.reverse()
stdout.write(str(len(out))+"\n")
stdout.write(" ".join(out))