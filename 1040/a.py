n,a,b = map(int,raw_input().split())
c = map(int,raw_input().split())
j = [a,b]
cost = 0
flag = 1
for i in range(0,n/2):
    if(c[i] == 2 and c[n-i-1] == 2):
        cost += 2*min(a,b)
    elif(c[i] == 2):
        cost += j[c[n-i-1]]
    elif(c[n-i-1] == 2):
        cost += j[c[i]]
    else:
        if(c[i] != c[n-i-1]):
            flag = 0
            break
if(n%2 == 1):
    if(c[(n/2)] == 2):
      cost += min(a,b)  

if(flag):
    print cost
else:
    print -1