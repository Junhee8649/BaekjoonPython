# dp는 Top-down으로 점화식을 즉, 마지막 배열을 그 전 배열로부터 생각하며 점화식을 생각하고 구현은 바텀업으로 구현하자!
n = int(input())
dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = dp[i-1] + 2*dp[i-2]
print(dp[n] % 10007)