from sys import stdin, stdout 
n = int(stdin.readline())
a = map(int,stdin.readline().split())
b = map(int,stdin.readline().split())
a.sort(reverse=True)
b.sort(reverse=True)
i = 0
j = 0
turn = 0
sa = 0
sb = 0
while(i<n or j<n):
    if(turn == 0):
        if(i == n):
            j+=1
        else:
            if(j == n):
                sa += a[i]
                i+=1
            else:
                if(a[i]>b[j]):
                    sa += a[i]
                    i+=1
                else:
                    j+=1
        turn = 1
    else:
        if(j == n):
            i+=1
        else:
            if(i == n):
                sb += b[j]
                j+=1
            else:
                if(a[i]<b[j]):
                    sb += b[j]
                    j+=1
                else:
                    i+=1
        turn = 0

stdout.write(str(sa-sb))