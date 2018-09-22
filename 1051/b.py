from sys import stdin,stdout
l,r  = map(int,stdin.readline().split())
stdout.write("YES")
stdout.write("\n")
a  = []
for i in range(l,r+1,2):
    s = str(i)+" "+str(i+1)
    a.append(s)
stdout.write("\n".join(a))