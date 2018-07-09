a = map(int,raw_input().split())
n = a[0]
m = a[1]
for i in range(m):
    b = raw_input()
s = ""
for i in range(n):
    if(i % 2 == 0):
        s+="0"
    else:
        s+="1"

print s