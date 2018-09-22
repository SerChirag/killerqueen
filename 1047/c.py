def seive():
    
from fractions import gcd
n = input()
a = map(int,raw_input().split())
guga = a[0]
for i in a:
    guga = gcd(guga,i)
a = [i//g for i in a]
