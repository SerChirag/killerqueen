def check(x,y):
    if(a[x] == '?'):
        if(a[y] == ')' or a[y] == '?'):
            return 1
    elif(a[x] == '('):
        if(a[y] == ')' or a[y] == '?'):
            return 1
    else:
        return 0

from sys import stdin,stdout
a = stdin.readline()
n = len(a)
bogus = [[0 for j in range(n)] for i in range(n)]
l = {}        
count = 0
for i in range(1,n+1,2):
    x = 0
    y = i
    if(i == 1):
        for j in range(n,i,-1):
            if(a[x] == '?'):
                if(a[y] == ')' or a[y] == '?'):
                    bogus[x][y] = 1
                    count += 1
                    try:
                        chomu = l[y]
                        l[y].append(x)
                    except:
                        l[y] = []
                        l[y].append(x)
                
            elif(a[x] == '('):
                if(a[y] == ')' or a[y] == '?'):
                    bogus[x][y] = 1
                    count += 1
                    try:
                        chomu = l[y]
                        l[y].append(x)
                    except:
                        l[y] = []
                        l[y].append(x)
            else:
                pass

            x += 1
            y += 1
            
    elif(i%2 == 0):
        pass
    
    else:
        for j in range(n,i,-1):
        
            if(bogus[x+1][y-1] == 1 and check(x,y) == 1):
                
                bogus[x][y] = 1
                count += 1
                try:
                    chomu = l[y]
                    l[y].append(x)
                except:
                    l[y] = []
                    l[y].append(x)

            else:

                try:
                    chomu = l[y]
                    for k in chomu:
                        
                        if(bogus[x][k-1] == 1):
                            bogus[x][y] = 1
                            count += 1
                            try:
                                nomu = l[y]
                                l[y].append(x)
                            except:
                                l[y] = []
                                l[y].append(x)
                            
                            break
                except:
                    pass
                
                

            x += 1
            y += 1

stdout.write(str(count))