M = list(map(int, input().split()))
N = int(input())
money = 0
for _ in range(N):
    B, S, L = map(float, input().split())
    if S >= 2 and L >= 17:
        money += M[int(B)]
print(money)