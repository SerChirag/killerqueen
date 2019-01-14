def build():
    for i in range(n):
        tree[n+i] = a[i]
    for i in range(n-1,-1,-1):
        tree[i] = tree[i<<1] & tree[i<<1|1]

def query(l,r):
    res = 1
    l += n
    r += n
    while(l<r):
        print tree[l],tree[r],l,r
        if(l & 1):
            res = res & tree[l]
            l+=1
        if(r & 1):
            r-=1
            res = res & tree[r]
        l >>= 1
        r >>= 1
    return res


t = input()
for qu in range(t):
    n,q = map(int,raw_input().split())
    a = map(int,raw_input().split())
    tree = [0]*2*n
    build()
    print tree
    for lo in range(q):
        l,r = map(int,raw_input().split())
        print query(l-1,r-1)