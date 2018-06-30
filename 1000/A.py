n = input()
a = []
for i in range(n):
    a.append(raw_input())

b = []
for i in range(n):
    b.append(raw_input())

ma = {}
ma[1] = [0,0,0]
ma[2] = [0,0]
ma[3] = [0,0]
ma[4] = [0,0]
for i in a:
    if(len(i)==1):
        if(i == "M"):
            ma[1][0]+=1
        elif(i == "L"):
            ma[1][1]+=1
        else:
            ma[1][2]+=1
    elif(len(i)==2):
        if(i == "XL"):
            ma[2][0]+=1
        else:
            ma[2][1]+=1
    elif(len(i)==3):
        if(i == "XXL"):
            ma[3][0]+=1
        else:
            ma[3][1]+=1
    else:
        if(i == "XXXL"):
            ma[4][0]+=1
        else:
            ma[4][1]+=1

count = 0
for i in b:
    if(len(i)==1):
        if(i == "M"):
            if(ma[1][0]<=0):
                count+=1
            else:
                ma[1][0] -=1 
        elif(i == "L"):
            if(ma[1][1]<=0):
                count+=1
            else:
                ma[1][1] -=1
        else:
            if(ma[1][2]<=0):
                count+=1
            else:
                ma[1][2] -=1
    elif(len(i)==2):
        if(i == "XL"):
            if(ma[2][0]<=0):
                count+=1
            else:
                ma[2][0] -=1
        else:
            if(ma[2][1]<=0):
                count+=1
            else:
                ma[2][1] -=1
    elif(len(i)==3):
        if(i == "XXL"):
            if(ma[3][0]<=0):
                count+=1
            else:
                ma[3][0] -=1
        else:
            if(ma[3][1]<=0):
                count+=1
            else:
                ma[3][1] -=1
    else:
        if(i == "XXXL"):
            if(ma[4][0]<=0):
                count+=1
            else:
                ma[4][0] -=1
        else:
            if(ma[4][1]<=0):
                count+=1
            else:
                ma[4][1] -=1


print count