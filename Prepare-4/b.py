from sys import stdin,stdout
a = stdin.readline()
a = a.strip("\n")
b = stdin.readline()
b = b.strip("\n")
count = 0
for i in range(len(a)-len(b)+1):
    flag = 1
    for j in range(len(b)):
        if(a[i+j] == b[j]):
            flag = 0
            break
    if(flag):
        count+=1

stdout.write(str(count))