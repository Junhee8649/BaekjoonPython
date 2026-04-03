I = int(input())
sum = 0

for i in range(1, I+1):
    if I % i == 0:
        sum += i

print(sum)