import sys

input = sys.stdin.readline
N, K = map(int, input().split())
coins = []
sum = 0
count = 0

for i in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)

for j in coins:
    while sum + j <= K:
        count += (K-sum) // j
        sum += ((K-sum) // j) * j
    if sum == K:
        break

print(count)