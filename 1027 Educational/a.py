t = input()
import string
l = string.ascii_lowercase[::]
for q in range(t):
    a = input()
    s = raw_input()
    flag = 1
    for i in range(a/2):
        st = s[i]
        en = s[a-i-1]
        p1 = l.find(st)
        p2 = l.find(en)
        s11 = ''
        s12 = ''
        s21 = ''
        s22 = ''
        if(st != 'a'):
            s11 = l[p1-1]
        if(st != 'z'):
            s12 = l[p1+1]
        if(en != 'a'):
            s21 = l[p2-1]
        if(en != 'z'):
            s22 = l[p2+1]
        if(st == en or (s11 == s21 and len(s11)==1) or (s11 == s22 and len(s11)==1) or (s12 == s21 and len(s12)==1) or (s12 == s22 and len(s12)==1)):
            pass
        else:
            flag = 0
            break
    if(flag == 1):
        print "YES"
    else:
        print "NO"