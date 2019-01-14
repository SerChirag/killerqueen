from sys import stdin,stdout
n = int(stdin.readline())
a = map(int,stdin.readline().split())
x,f =  map(int,stdin.readline().split())
count = 0
k = f+x
for i in a:
    p = i/k
    rem = i%k
    count+=p*f
    if(rem>x):
        count+=f
stdout.write(str(count))