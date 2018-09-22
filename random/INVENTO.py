from math import log
t = input()
for qu in range(t):
    x = input()
    n = "{0:b}".format(x)
    print len(n)