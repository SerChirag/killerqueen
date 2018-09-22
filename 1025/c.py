s = raw_input()
s += s
maxi = 1
count = 1
bit = s[0]
for i in range(1,len(s)):
    if(s[i] == bit):
        maxi = max(maxi,count)
        count = 1
    else:
        count += 1
    bit = s[i]

maxi = max(maxi,count)
print maxi