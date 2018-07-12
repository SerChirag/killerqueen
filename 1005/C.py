n = input()
a = map(int,raw_input().split())
d = {}
for i in a:
    d[i] = 0
for i in a:
    d[i] += 1
done = {}
count = 0
for i in a:
    try:
        co = done[i]
        pass
    except:
        p = 1
        c = 0
        flag = 0
        while(c <= 32):
            if(p-i > 0):
                try:
                    po = d[p-i]
                    if(i == p-i):
                        if(po >= 2):
                            flag = 1
                            done[i] = 1
                            done[p-i] = 1
                            break
                        else:
                            c+=1
                            p = p << 1
                    else:
                        flag = 1
                        done[i] = 1
                        done[p-i] = 1
                        break
                except:
                    c+=1
                    p = p << 1
            else:
                c+=1
                p = p << 1
        if(flag == 0):
            count+=1
            
print count

