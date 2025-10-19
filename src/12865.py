N, K = map(int, input().split())
weights = [0]
values = [0]
for _ in range(N):
    W, V = map(int, input().split())
    weights.append(W)
    values.append(V)

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for w in range(1, K+1):
        if weights[i] > w:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w-weights[i]] + values[i], dp[i-1][w])
print(dp[N][K])