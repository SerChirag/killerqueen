s = raw_input()
t = raw_input()
s = s[::-1]
t = t[::-1]
a = len(s)
b = len(t)
i = 0
while(i < a and i < b):
    if(t[i] == s[i]):
        i+=1
    else:
        break

print a+b-2*i