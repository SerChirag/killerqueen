n,m = map(int,raw_input().split())
a = raw_input()
b = raw_input()
c = a.split('*')
if(len(c) == 1):
    if(a == b):
        print "YES"
    else:
        print "NO"
else:
    if(b.startswith(c[0]) and b[len(c[0]):].endswith(c[1])):
        print "YES"
    else:
        print "NO"
    
