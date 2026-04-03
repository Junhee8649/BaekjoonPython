import sys


N = int(input())
A = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0] * 1001
for i in range(1,len(A)):
    dp[i] = A[i]

for i in range(2, N+1):
    for j in range(1, i):
        if A[j] < A[i]:
            dp[i] = max(dp[j] + A[i], dp[i])
    
print(max(dp[1:N+1]))