from sys import stdin,stdout
from collections import Counter
n = int(stdin.readline())
a = []
m = {}
for i in range(n):
	p = stdin.readline().strip('\n')
	c = Counter(p)
	s = []
	for j in c:
		if(c[j]&1):
			s.append(j)
	s.sort()
	s = "".join(s)	
	m[s] = m.get(s,0)+1

count = 0
for i in m:
	count += (m[i]*(m[i]-1))/2
for i in m:
	for j in range(len(i)):
		s = i[:j] + i[j+1:]
		count += m.get(s,0)*m[i] 

stdout.write(str(count))