t = input()
out = []
for q in range(t):
    a,b,c,d = map(int,raw_input().split())
    b1 = a//b    
    b2 = (c//b)
    if(c%b == 0):
        b2-=1
    b3 = (d//b)
    out.append(str(b1-(b3-b2)))

print("\n".join(out))    