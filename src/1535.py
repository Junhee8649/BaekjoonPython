N = int(input())
health = [0]
happy = [0]
health += list(map(int, input().split()))
happy += list(map(int, input().split()))

dp = [[0 for _ in range(100)] for _ in range(21)]

for i in range(1, N+1):
    for h in range(1, 100):
        if health[i] > h:
            dp[i][h] = dp[i-1][h]
        else:
            dp[i][h] = max(dp[i-1][h-health[i]] + happy[i], dp[i-1][h])
print(dp[N][99])