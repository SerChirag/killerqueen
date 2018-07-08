p = map(int,raw_input().split())
a = p[0]
b = p[1]
x = p[2]
bc = b
ac = a-1
xc = x
s = "0"
while(xc):
    if(s[-1] == "0"):
        if(bc):
            s+="1"
            bc-=1
        else:
            s+="0"
            ac-=1
    else:
        if(ac):
            s+="0"
            ac-=1
        else:
            s+="1"
            bc-=1
    xc-=1

sw = ""
for i in s:
    if(i == "0"):
        sw += i
        if(ac):
            sw += "0"*ac
            ac = 0
    else:
        sw += i
        if(bc):
            sw += "1"*bc
            bc = 0

print sw

