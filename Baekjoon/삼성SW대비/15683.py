from math import inf


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
answer = inf

cctv_list = []
for y in range(N):
    for x in range(M):
        if 1 <= grid[y][x] <= 5:
            cctv_list.append((y, x, grid[y][x]))

modes = [
    [], # 0번 인덱스 안 씀
    [[0], [1], [2], [3]],          # 1번: 1방향 (4가지 경우)
    [[0, 2], [1, 3]],              # 2번: 2방향 (2가지 경우)
    [[0, 1], [1, 2], [2, 3], [3, 0]], # 3번: 직각 2방향 (4가지 경우)
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], # 4번: 3방향 (4가지 경우)
    [[0, 1, 2, 3]]                 # 5번: 4방향 모두 (1가지 경우)
]

def dfs(depth, current_grid):
     global answer

     if depth == len(cctv_list):
        temp = count_blind_spot(current_grid)
        answer = min(answer, temp)
        return
     y, x, type = cctv_list[depth]

     for i in modes[type]:
         temp_grid = [row[:] for row in current_grid]
         # 모든 방향을 다 돌기 위해서 ex) 2번 타입이고 처음 도는거면 [0,2]를 돌기 위해서 d가 0이랑 2가 되는거임
         for d in i:
            watch(y, x, d, temp_grid)
         dfs(depth + 1, temp_grid)
    
# watch가 무거워지지 않기 위해서 무조건 준 방향으로만 직진해서 #붙이고(0인 빈칸에만) 외부에서 모든 방향을 설정해서 방향마다 watch를 돌리자!
def watch(y, x, d, current_grid):
    ny = y + dy[d]
    nx = x + dx[d]

    while True:
        if 0 <= ny < N and 0 <= nx < M and current_grid[ny][nx] != 6:
            if current_grid[ny][nx] == 0:
                current_grid[ny][nx] = '#'
            ny += dy[d]
            nx += dx[d]
        else:
            break   

def count_blind_spot(current_grid):
    return sum(row.count(0) for row in current_grid)

dfs(0, grid)
print(answer)