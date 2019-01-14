n = input()
a = raw_input()
m = {}
for i in range(10):
    m[i] = 0
for i in a:
    m[int(i)] += 1
print min(m[8],n/11)