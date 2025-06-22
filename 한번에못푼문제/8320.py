# 이중 for문 없애기 위한 수학 공식 이용
from math import isqrt, ceil

n = int(input())
count = 0

for i in range(1, isqrt(n) + 1):
    count += n//i - i + 1

print(count)