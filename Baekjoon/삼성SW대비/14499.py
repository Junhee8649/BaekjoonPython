N, M, y, x, K = map(int, input().split())
dice_map = []
for i in range(N):
    dice_map.append(list(map(int, input().split())))
move = list(map(int, input().split()))
# 동 서 북 남
dy = [0,0,-1,1]
dx = [1,-1,0,0]
# 위 아래 앞 뒤 좌 우
dice = [0,0,0,0,0,0]

for i in move:
    nx = x + dx[i-1]
    ny = y + dy[i-1]
    if nx >= 0 and nx <= M-1 and ny >= 0 and ny <= N-1:
        x, y = nx, ny
        if i == 1:
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]
        elif i == 2:
            dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]
        elif i == 3:
            dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]
        elif i == 4:
            dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]

        if dice_map[y][x] == 0:
            dice_map[y][x] = dice[1]
        else:
            dice[1] = dice_map[y][x]
            dice_map[y][x] = 0
        print(dice[0])