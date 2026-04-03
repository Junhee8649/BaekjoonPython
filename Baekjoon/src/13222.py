from math import sqrt


N, W, H = map(int, input().split())
access_len = sqrt(W**2 + H**2)
for i in range(N):
    match = int(input())
    if match <= access_len:
        print("YES")
    else:
        print("NO")