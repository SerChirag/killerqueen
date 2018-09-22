n = input()
a  = raw_input()
m = {}
for i in a:
    try:
        po = m[i]
        m[i] += 1
    except:
        m[i] = 1

flag = 0
if(len(m) == 1):
    print "Yes"
else:
    for i in m:
        if(m[i] > 1):
            flag = 1
            break
    if(flag):
        print "Yes"
    else:
        print "No"