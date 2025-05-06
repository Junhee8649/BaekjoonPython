t = int(input())
count = 0
while t >= 10:
    num = 1
    for i in str(t):
        num *= int(i)
    t = num
    count += 1
print(count)