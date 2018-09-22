n,h,a,b,k = map(int,raw_input().split())
for t in range(k):
    t1,f1,t2,f2 = map(int,raw_input().split())
    count = abs(t1-t2)
    if(count != 0):
        if(f1<=b and f1>=a):
            count += abs(f1-f2)
        else:
            count += min(abs(f1-a)+abs(f2-a),abs(f1-b)+abs(f2-b))
    else:
        count += abs(f1-f2)
    print count