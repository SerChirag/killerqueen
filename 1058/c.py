n = input()
a = map(int,raw_input().split())
flag = 0
for i in a:
    if(i == 1):
        flag = 1
        break

if(flag):
    print "HARD"
else:
    print "EASY"