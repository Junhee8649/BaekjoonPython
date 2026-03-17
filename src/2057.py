from itertools import combinations
from math import factorial

N = int(input())
all_factorial = []
all_sum = set()
for i in range(20):
    if factorial(i) > N:
        break
    all_factorial.append(factorial(i))

for j in range(1, len(all_factorial) + 1):
    for combo in combinations(all_factorial, j):
        all_sum.add(sum(combo))

if N not in all_sum:
    print("NO")
else:
    print("YES")