n = input()
a = map(int,raw_input().split())
n = len(a)
m = 0
for i in range(0,n,2):
    b = a[i]
    for j in range(i+1,n,1):
        if(a[j]==b):
            break
    k = j
    for j in range(k,i+1,-1):
        t = a[j-1]
        a[j-1] = a[j]
        a[j] = t
        m+=1
print m


