from sys import *
loda = []
t = int(stdin.readline())
for i in range(t):
    a,b,d = map(float,stdin.readline().split())
    loda.append(str(pow(d,2)/2))
stdout.write("\n".join(loda))
