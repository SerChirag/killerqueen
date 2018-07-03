a = [1, 6, 28, 120, 496, 2016, 8128, 32640]
n = input()
a.reverse()
for i in a:
    if(n%i==0):
        print i
        break