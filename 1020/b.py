n = input()
m = {}
l = []
p = map(int,raw_input().split())
for i in range(n):
    m[i] = p[i]-1
for i in range(n):
    done = [0]*n
    curr = i
    while(1):
        if(done[curr]):
            break
        else:
            done[curr] = 1
            curr = m[curr]
    l.append(curr+1)
for i in l:
    print i,
print
        
    
