from collections import deque


N, K = map(int, input().split())
A = list(map(int, input().split()))
A = deque(A)
robots = [0] * N
robots = deque(robots)
answer = 0

while A.count(0) < K:
    A.rotate(1)
    robots.rotate(1)
    # 타일이랑 로봇이 한칸씩 순환했으니 내리는칸 로봇 있다면 즉시 내려지도록 robots[-1]을 0으로 함
    robots[0], robots[-1] = 0, 0
    # 가장 먼저 오른 로봇부터 움직여야하므로 역순으로 탐색하며 이동
    for i in range(len(robots)-1, 0, -1):
        if robots[i-1] == 1 and robots[i] == 0 and A[i] >= 1:
            robots[i], robots[i-1] = robots[i-1], robots[i]
            A[i] -= 1
    # 로봇 이동 후 내리는 칸에 로봇 있다면 즉시 내려지도록 robots[-1]을 0으로 함
    robots[-1] = 0
    if A[0] != 0 and robots[0] == 0:
        robots[0] = 1
        A[0] -= 1
    answer += 1

print(answer)