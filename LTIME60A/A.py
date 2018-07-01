t = input()
for q in range(t):
    a = raw_input().split()
    s = a[0]
    x = int(a[1])
    res = 0
    for i in range(len(s)):
        l = [0]*26
        for j in range(i,len(s)):
            l[ord(s[j])-97] += 1
            c = 0
            flag = 1
            for k in range(26):
                if(l[k]>0):
                    c+=1
                    if(c == 1):
                        maxi = l[k]

                    if(l[k] != maxi):
                        flag = 0
                        break
            
            if(flag == 1 and c >= x):
                res += 1


    print res

