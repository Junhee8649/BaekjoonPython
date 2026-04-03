P = 100 - int(input())
a = P // 25
P %= 25
b = P // 10
P %= 10
c = P // 5
P %= 5
d = P
print(a, b, c, d)