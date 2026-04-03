N, M = map(int, input().split())
balls = []
for ball in range(1, N+1):
    balls.append(ball)

for _ in range(M):
    i, j = map(int, input().split())
    temp = balls[i-1]
    balls[i-1] = balls[j-1]
    balls[j-1] = temp

for ball in balls:
    print(ball, end=" ")