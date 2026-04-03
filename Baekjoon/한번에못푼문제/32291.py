import sys
import math

x = int(sys.stdin.readline())
target = x + 1

divisors = []

for i in range(1, int(math.sqrt(target)) + 1):
    # 약수를 찾아 일단
    if target % i == 0:
        if i <= x:
            divisors.append(i)
        # 약수를 항상 쌍이니까 전자는 중복 방지
        if i != target // i and target // i <= x:
            divisors.append(target // i)

divisors.sort()
print(*divisors)