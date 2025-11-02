N = int(input())
dp = [0] * 11
dp[2] = 1

for i in range(3,N+1):
    if i % 2 == 0:
        a, b = i // 2, i // 2
    else:
        a, b = i // 2 + 1, i // 2
    dp[i] = dp[a] + dp[b] + a*b

print(dp[N])