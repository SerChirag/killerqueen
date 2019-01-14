n = input()
a = list(raw_input())
a = [int(i) for i in a]
pre = []
cost = 0
for i in a[::-1]:
    cost += i
    pre.append(cost)

pre = pre[::-1]
cost = 0
flag = 0
for i in range(0,n-1):
    cost += a[i]
    fcost = 0
    flag = 0
    for j in range(i+1,n):
        fcost += a[j]
        if(fcost == cost):
            flag = 1
            fcost = 0
        if(fcost > cost):
            break
    if(fcost == 0 and flag == 1):
        print "YES"
        exit()
print "NO"
