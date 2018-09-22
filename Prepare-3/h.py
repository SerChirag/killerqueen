n = input()
c = 0
k = 1867
for i in range(k+1,k+n+1):
    if(i%400==0):
        c+=2
    elif(i%100==0):
        c+=1
    elif(i%4==0):
        c+=2
    else:
        c+=1
    c = c%7
c = c%7 
if(c==0):
    print "Sunday"
elif(c==1):
    print "Monday"
elif(c==2):
    print "Tuesday"
elif(c==3):
    print "Wednesday"
elif(c==4):
    print "Thursday"
elif(c==5):
    print "Friday"
else:
    print "Saturday"
