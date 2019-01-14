from sys import stdin,stdout
n = int(stdin.readline())
count = 0
for i in range(n):
    k = int(stdin.readline())
    if(k == 1):
        pass
    else:
        count  += 1
    
stdout.write(str(count))