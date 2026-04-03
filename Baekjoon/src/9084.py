T = int(input())
for i in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    money = int(input())
    dp = [0] * (money+1)
    dp[0] = 1
    for coin in coins:
        for j in range(coin, money+1):
            dp[j] = dp[j-coin] + dp[j]
    print(dp[money])