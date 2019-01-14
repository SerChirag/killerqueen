from sys import stdin,stdout
ne = int(stdin.readline())
a  = map(int,stdin.readline().split())
p = []
n = []
z = []
for i in range(ne):
    if(a[i] > 0):
        p.append((a[i],i+1))
    elif(a[i] < 0):
        n.append((a[i],i+1))
    else:
        z.append((a[i],i+1))

steps = []
lastp = 0
if(len(p)):
    prev = p[0][1]
    lastp = prev
    for i in range(1,len(p)):
        steps.append("1 "+str(prev) + " " + str(p[i][1]))
        prev = p[i][1]
        lastp = prev

lastz = 0
if(len(z)):
    prev = z[0][1]
    lastz = prev    
    for i in range(1,len(z)):
        steps.append("1 "+str(prev)+ " " + str(z[i][1]))
        prev = z[i][1]
        lastz = prev

n.sort()

if(len(n)%2 == 0):
    if(len(n)):
        prev = n[0][1]
        for i in range(1,len(n)):
            steps.append("1 "+str(prev)+ " " +  str(n[i][1]))
            prev = n[i][1]
        if(len(p)):
            steps.append("1 " + str(prev) + " " + str(lastp))
            if(len(z)):
                steps.append("2 " + str(lastz))
        else:
            if(len(z)):
                steps.append("2 " + str(lastz))
    else:
        if(len(p) and len(z)):
            steps.append("2 " + str(lastz))
             
else:
    if(len(n)):
        prev = n[0][1]
        for i in range(1,len(n)-1):
            steps.append("1 "+str(prev)+ " " + str(n[i][1]))
            prev = n[i][1]
        if(len(p) and len(n)!=1):
            steps.append("1 " + str(prev) + " " + str(lastp))
        if(len(z)):
            steps.append("1 " + str(n[-1][1]) + " " + str(lastz))
            if(len(p)):
                steps.append("2 " + str(lastz))
            elif(len(n)!=1):
                steps.append("2 " + str(lastz))
        else:
            steps.append("2 " + str(n[-1][1]))

stdout.write("\n".join(steps))