n = input()
ma = 0
for q in range(n):
    x,y = map(int,raw_input().split())
    ma = max(ma,x+y)
print ma