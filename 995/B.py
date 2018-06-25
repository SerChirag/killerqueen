n = input()
a = map(int,raw_input().split())
m = min(a)
pos = m%n
for i in range(len(a)):
    a[i] -= m
j = 0
while(a[pos]!=0):
    if(a[pos]-j <= 0):
        break
    pos+=1
    j+=1
    if(pos == len(a)):
        pos = 0
print pos+1