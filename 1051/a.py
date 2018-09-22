from sys import stdin,stdout
import string
t = input()
for p in range(t):
    s = raw_input()
    num = []
    down = string.ascii_lowercase
    up = string.ascii_uppercase
    md = {}
    mu = {}
    c1 = 0
    c2 = 0
    c3 = 0
    for i in down:
        md[i] = 1
    for i in up:
        mu[i] = 1
    up = []
    down = []
    for j in range(len(s)):
        i = s[j]
        try:
            p = int(i)
            c1+=1
            num.append(j)
        except:
            try:
                p = mu[i]
                c2+=1
                up.append(j)
            except:
                c3+=1
                down.append(j)
    if(c1 > 0 and c2 > 0 and c3 > 0):
        print s
    elif(c1==0 and c2 ==0):
        p = list(s)
        p[0] = '1'
        p[1] = 'A'
        s = "".join(p)
        print s
    elif(c2==0 and c3 ==0):
        p = list(s)
        p[0] = 'a'
        p[1] = 'A'
        s = "".join(p)
        print s
    elif(c3==0 and c1 ==0):
        p = list(s)
        p[0] = '1'
        p[1] = 'a'
        s = "".join(p)
        print s
    elif(c1 == 0):
        p  = list(s)
        if(c2 >= 2):
            elem = up[0]
            p[elem] = '1'
        else:
            elem = down[0]
            p[elem] = '1'
        s = "".join(p)
        print s
    elif(c2 == 0):
        p  = list(s)
        if(c1 >= 2):
            elem = num[0]
            p[elem] = 'A'
        else:
            elem = down[0]
            p[elem] = 'A'
        s = "".join(p)
        print s
    else:
        p  = list(s)
        if(c1 >= 2):
            elem = num[0]
            p[elem] = 'a'
        else:
            elem = up[0]
            p[elem] = 'a'
        s = "".join(p)
        print s

    

