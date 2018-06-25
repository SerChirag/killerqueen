n = input()
a = [100,20,10,5,1]
s = 0
for i in a:
    s += n/i
    n = n%i
print s