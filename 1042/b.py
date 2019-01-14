from fractions import gcd
a,b,x,y = map(int,raw_input().split())
h = gcd(x,y)
x /= h
y /= h
s1 = a/x
s2 = b/y
print min(s1,s2)