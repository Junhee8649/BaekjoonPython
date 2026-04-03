from collections import deque


N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
# 북 동 남 서 
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
baby_shark = 2
count, fish_time = 0, 0

for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            sy, sx = i, j

def bfs(g, sy, sx):
    global baby_shark
    dist = [[-1] * N for _ in range(N)]
    dist[sy][sx] = 0
    can_eat = []
    q = deque([(sy, sx)])
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and g[ny][nx] <= baby_shark and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                if g[ny][nx] == baby_shark or g[ny][nx] == 0:
                    q.append((ny, nx))
                else:
                    can_eat.append([ny,nx, dist[ny][nx]])  

    if can_eat:
        can_eat.sort(key=lambda x: (x[2], x[0], x[1]))
        return (can_eat[0][2], can_eat[0][0], can_eat[0][1])
    else:
        return (-1,-1,-1)


temp_time, ty, tx = bfs(grid, sy, sx)
while temp_time != -1:
    fish_time += temp_time
    grid[sy][sx] = 0
    grid[ty][tx] = 9
    sy, sx = ty, tx
    count += 1
    if baby_shark == count:
        baby_shark += 1
        count = 0
    temp_time, ty, tx = bfs(grid, sy, sx)
print(fish_time)