def division(x, y, N):
    global white_cnt, blue_cnt
    color = paper[x][y] # 현재 영역의 첫 번째 색깔 (기준)
    
    for i in range(x, x + N):
        for j in range(y, y + N):
            # 만약 색깔이 다른 부분이 하나라도 발견되면
            if paper[i][j] != color:
                # 4등분으로 쪼개서 다시 탐색 (재귀)
                division(x, y, N // 2)                # 1사분면 (왼쪽 위)
                division(x, y + N // 2, N // 2)       # 2사분면 (오른쪽 위)
                division(x + N // 2, y, N // 2)       # 3사분면 (왼쪽 아래)
                division(x + N // 2, y + N // 2, N // 2) # 4사분면 (오른쪽 아래)
                return # 쪼갰으므로 현재 함수는 여기서 종료

    # for문을 무사히 통과했다면 (= 모두 같은 색이라면)
    if color == 0:
        white_cnt += 1
    else:
        blue_cnt += 1

N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
    
white_cnt = 0
blue_cnt = 0
division(0, 0, N) 

print(white_cnt)
print(blue_cnt)