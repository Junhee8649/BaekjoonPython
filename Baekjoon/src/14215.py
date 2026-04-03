sticks = list(map(int, input().split()))
sticks.sort()
a = sticks[0]
b = sticks[1]
c = sticks[2]
if c < (a + b):
    print(a+b+c)
else:
    print((a+b)*2-1)