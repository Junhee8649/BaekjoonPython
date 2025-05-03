from math import isqrt, ceil

n = int(input())
count = 0

for i in range(1, isqrt(n) + 1):
    count += n//i - i + 1

print(count)