n,k = map(int,raw_input().split())
for i in range(k):
    if(n%10 == 0):
        n/=10
    else:
        n-=1

print n