t = int(input())
for k in range(t):
    n, m = map(int, input().split())
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, m + 1):
        for j in range(min(i, n), 0, -1):
            dp[j] = (dp[j] + dp[j-1])

    print(dp[n])