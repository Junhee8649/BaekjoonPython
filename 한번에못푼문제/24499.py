import sys

N, K = map(int, sys.stdin.readline().split())
apple = list(map(int, sys.stdin.readline().split()))
apple += apple[:K - 1]

# 초기 윈도우 합 계산
current_sum = sum(apple[0:K])
max_sum = current_sum

# 슬라이딩 윈도우 진행
# N == K 일 때는 루프가 돌아도 max_sum은 변하지 않습니다.
for i in range(1, N):
    current_sum = current_sum - apple[i - 1] + apple[i + K - 1]
    max_sum = max(max_sum, current_sum)
print(max_sum)