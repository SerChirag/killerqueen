def do(x):
    if(x == 1):
        return [1]
    elif(x == 2):
        return [1,2]
    elif(x == 3):
        return [1,1,3]
    else:
        odd = ((x+1)/2)
        even = do(x-odd)
        for i in range(len(even)):
            even[i]*=2
        out = [1]*odd
        out.extend(even)
        return out

from sys import stdin,stdout
n = int(stdin.readline())
out = map(str,do(n))
stdout.write(" ".join(out))