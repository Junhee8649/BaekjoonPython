N = int(input())
X = int(input())
tunas = 0

for i in range(N):
    P1, P2 = map(int, input().split())
    if abs(P1-P2) > X:
        P3 = int(input())
        tunas += P3
        continue
    tunas += max(P1, P2)
print(tunas)