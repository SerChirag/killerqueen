t = input()
for i in range(t):
    x = input()
    flag = 0
    if(int(x**0.5)**2 == x and x > 1):
        print int(x**0.5)**2,1     
    else:
        for j in range(2,31622):
            shagga = 0
            if(int((j**2 + x)**0.5)**2 == (j**2 + x)):
                flag = 1 
                shagga = j

        if(flag == 1):
            j = shagga
            n = int((j**2 + x)**0.5)
            if(n <= 1000000000):
                print n,(n/j)
            else:
                print -1
            
            
        else:
            print -1