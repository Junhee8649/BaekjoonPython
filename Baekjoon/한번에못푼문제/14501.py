N = int(input())

# 1일차 인덱스를 맞추기 위한 초기화
sangdam = [[0, 0]] 
for _ in range(N):
    sangdam.append(list(map(int, input().split())))

# 퇴사일(N+1)까지의 최대 수익을 기록할 배열
dp = [0] * (N + 2)

# 1일부터 N일까지 차례대로 진행
for i in range(1, N + 1):
    time = sangdam[i][0]
    profit = sangdam[i][1]
    
    # 1. 오늘 상담을 안 하는 경우: 내일 장부에 '오늘까지의 최대 수익'을 그대로 적어줌
    dp[i+1] = max(dp[i+1], dp[i])
    
    # 2. 오늘 상담을 하는 경우: 퇴사일을 넘기지 않는다면
    if i + time <= N + 1:
        # 상담이 끝나는 날의 장부에 '오늘까지의 수익 + 이번 상담 수익'을 적어줌
        # (만약 이미 더 큰 금액이 적혀있다면 갱신하지 않음)
        dp[i+time] = max(dp[i+time], dp[i] + profit)

# 퇴사하는 날(N+1일)에 장부에 적힌 최대 수익 출력
print(dp[N+1])