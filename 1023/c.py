from sys import *
n,k = map(int,stdin.readline().split())
a = raw_input()
st = []
done = [0]*n
for i in range(n):
    if(a[i] == '('):
        st.append(i)
    else:
        e = st.pop()
        done[e] = 1
        done[i] = 1
        k-=2
    if(k == 0):
        break
s = ""
for i in range(n):
    if(done[i]):
        s += a[i]

stdout.write(s)
