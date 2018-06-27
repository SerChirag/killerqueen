import math

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

a = map(int,raw_input().split())
l = a[0]
r = a[1]
x = a[2]
y = a[3]
product = x*y
p = list(divisorGenerator(product))
f = 0
for i in range(len(p)):
    if(p[i]>=l):
        f = 1
        break
print i
if(f==1):
    count = 0
    for j in range(i,len(p)):
        if(p[j]>r):
            break
        else:
            m1 = product/p[j]
            if(m1<=r):
                print(p[j],m1)
                count+=1
    print count
else:
    print 0

