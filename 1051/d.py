import sys
range = xrange
input = raw_input

MOD = 998244353
MOD2 = 998244353

n,k = [int(x) for x in input().split()]

DP = [[[0]*4 for _ in range(2*(i+1)+3)] for i in range(n)]
patterns = [0,1,2,3]
for p in patterns:
    if p==0 or p==3:
        DP[0][1][p]=1
    else:
        DP[0][2][p]=1
for i in range(1,n):
    D = DP[i-1]
    E = DP[i]
    for K in range(1,2*(i+1)+1):
        ans = E[K]
        ans[0]  = D[K-1][3] + D[K][2]   + D[K][1]   + D[K][0]
        ans[1]  = D[K-1][3] + D[K-2][2] + D[K][1]   + D[K-1][0]        
        ans[0] = ans[0]%MOD
        ans[1] = ans[1]%MOD        
        ans[2] = ans[1]
        ans[3] = ans[0]
        
        
print sum(DP[n-1][k])%MOD
#print sum(DP[(n-1,k,p)] for p in patterns)%MOD