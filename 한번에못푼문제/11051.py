# dp와 이항계수
n, k = map(int, input().split())
mod = 10007

# 동적 계획법을 이용한 이항 계수 계산
dp = [0] * (k + 1)
dp[0] = 1

for i in range(1, n + 1):
    for j in range(min(i, k), 0, -1):
        dp[j] = (dp[j] + dp[j-1]) % mod

print(dp[k])