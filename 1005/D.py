a = raw_input()
a = a[::-1]
c = 0
s = 0
conti = 0
for i in range(len(a)):
    s += int(a[i])
    conti +=1
    if(s%3 == 0):
        c+=1
        s = 0
        conti = 0
    elif(int(a[i])%3 == 0):
        c+=1
        s = 0
        conti = 0
    elif(conti == 3):
        c+=1
        s = 0
        conti = 0
    else:
        pass

print c
