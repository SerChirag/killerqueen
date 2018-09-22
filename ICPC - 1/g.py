from sys import *
t = int(stdin.readline())
loda = []
for q in range(t):
    a,b,m = map(int,stdin.readline().split())
    lo = {}
    f = 1
    count = 0
    while(1):
        if(f == b):
            loda.append(str(count))
            break
        f *= a
        f = f%m
        count += 1
        

stdout.write("\n".join(loda))