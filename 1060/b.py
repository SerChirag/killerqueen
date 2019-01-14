n = input()
s = len(str(n))
try :
    p = int("9"*(s-1))
except:
    p = 0
a = n-p
s = 0
for i in str(a):
    s += int(i)
for i in str(p):
    s += int(i)

print s