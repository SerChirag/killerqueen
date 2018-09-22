n,m,k = map(int,raw_input().split())
a = []
e = (n*m)/k
for i in range(n):
    b = map(int,raw_input().split())
cla = 1
for i in range(n):
    for j in range(m):
        print min(cla,k),
        cla+=1
    print