t = input()
for qo in range(t):
    a = raw_input()
    b = raw_input()
    q = input()
    m = []
    for i in range(len(b)):
        l = [False]*len(a)
        m.append(l)
    for i in range(len(b)):
        for j in range(len(a)):
            if(i == 0 and j == 0):
                if(a[0] == '0' or b[0] == '0'):
                    m[0][0] = True
                else:
                    m[0][0] = False
            elif(i == 0):
                if(a[j] == '0'):
                    m[0][j] = True
                else:
                    m[0][j] = not m[0][j-1]
            elif(j == 0):
                if(b[i] == '0'):
                    m[i][0] = True
                else:
                    m[i][0] = not m[i-1][0]
            else:
                if(m[i][j-1] == False):
                    m[i][j] = True
                elif(m[i-1][j] == False):
                    m[i][j] = True
                else:
                    pass

    s = ""
    for tu in range(q):
        x,y = map(int,raw_input().split()) 
        if(m[x-1][y-1]):
            s+="1"
        else:
            s+="0"
    print s