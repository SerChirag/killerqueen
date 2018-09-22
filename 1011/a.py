from sys import *
n,k = map(int,stdin.readline().split())
s = stdin.readline()
s = s.rstrip('\n')
m = {}
for i in s:
    m[i] = ord(i) - ord('a') + 1
l = m.items()
l.sort()
count = 1
sumi = l[0][1]
prev = l[0][0]
for i in range(1,len(l)):
    if(count == k):
        break
    if(ord(l[i][0])-ord(prev) >= 2):
        sumi += l[i][1]
        prev = l[i][0]
        count += 1
if(count == k):
    print sumi
else:
    print -1