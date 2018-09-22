def computeGCD(x, y): 
   while(y): 
       x, y = y, x % y 
   return x

def get(x):
    global spf
    p = {}
    while(x != 1):
        p[spf[x]] = 1
        x = x/spf[x]
    return p

from sys import stdin,stdout
from collections import Counter
n = int(stdin.readline())
m = {}
a = map(int,stdin.readline().split())
c = Counter(a)
count1 = c[1]  
if(count1 == n):
    stdout.write("-1")
else:
    bla = []
    for i in a:
        if(i != 1):
            bla.append(i)
    a = bla
    #ma = 15000001
    ma = 15001
    guga = a[0]
    for i in a:
        guga = computeGCD(i,guga)
    if(guga != 1 and count1>0):
        stdout.write(str(count1))
    else:
        if(guga != 1):
            for i in range(n):
                a[i] = a[i]/guga
        spf = [0]*ma
        spf[1] = 1
        for i in range(2,ma):
            spf[i] = i
        for i in range(4,ma,2):
            spf[i] = 2
        i = 3
        while(i*i<ma):
            if(spf[i] == i):
                j = pow(i,2)
                for k in range(j,ma,i):
                    if(spf[k] == k):
                        spf[k] = i
            i+=1
            
        for i in range(len(a)):
            elem = a[i]
            p = get(elem)
            for i in p:
                try:
                    po = m[i]
                    m[i] += 1
                except:
                    m[i] = 1

        l = m.items()
        l.sort(key = lambda x : x[1])
        if(len(l)>0):
            stdout.write(str(n-l[-1][1]))
        else:
            stdout.write("-1")