from sys import stdin,stdout
import threading
threading.stack_size(2**26)
import sys
sys.setrecursionlimit(0x1000000)
count = 0
def solve():
    n,q = map(int,stdin.readline().split())
    m = {}
    out = []
    for i in range(1,n+1):
        m[i] = []
    a = map(int,stdin.readline().split())
    for i in range(1,n):
        m[a[i-1]].append(i+1)

    tour = []
    start = {}
    end = {}
    def dfs(node):
        global count
        start[node]=count
        tour.append(node)
        count+=1
        for i in m[node]:
            dfs(i)
        end[node] = count
    dfs(1) 
    for t in range(q):
        u,k = map(int,raw_input().split())
        # print end[u]-start[u]
        # print tour
        if(end[u]-start[u] < k):
            print("-1")
        else:
            print(tour[start[u]+k-1])

threading.Thread(target=solve).start()
