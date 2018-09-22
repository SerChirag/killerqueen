n = input()
a = map(int,raw_input().split())
b = map(int,raw_input().split())
s1 = sum(a)
s2 = sum(b)
if(s1>=s2):
    print "Yes"
else:
    print "No"