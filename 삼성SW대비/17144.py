from collections import deque


R, C, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]
# 북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# bfs로 먼지 확산 근데 시간이나 거리가 필요한게 아니면 사실 큐를 쓸 필요는 없다!
def dust(g, r, c):
    spread = [[0]*c for _ in range(r)]
    q = deque()
    for y in range(r):
        for x in range(c):
            if g[y][x] > 0:
                temp_dust = g[y][x] // 5
                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < r and 0 <= nx < c and g[ny][nx] != -1:
                        spread[ny][nx] += temp_dust
                        spread[y][x] -= temp_dust
    for i in range(r):
        for j in range(c):
            g[i][j] += spread[i][j]

def airclean(g, r, c):
    for i in range(r):
        if g[i][0] == -1:
            machine_top, machine_bottom = i, i+1
            break
    top_road = (2*(c-1) + 2*machine_top) - 2
    bottom_road = (2*(c-1) + 2*(r-1-machine_bottom)) - 2
    direction = 1
    # direction은 동쪽부터 위는 반시계니 -1해야하고 아래는 시계니까 +1 해야함

    top_sy, top_sx, top_direction = machine_top, 1, direction, 
    ny, nx = top_sy + dy[top_direction], top_sx + dx[top_direction]
    for _ in range(top_road):
        if 0 <= ny < r and 0 <= nx < c:
            g[ny][nx], g[top_sy][top_sx] = g[top_sy][top_sx], g[ny][nx]
            ny, nx = ny + dy[top_direction], nx + dx[top_direction]
        else:
            ny, nx = ny - dy[top_direction], nx - dx[top_direction]
            top_direction = (top_direction-1) % 4
            ny, nx = ny + dy[top_direction], nx + dx[top_direction]
            g[ny][nx], g[top_sy][top_sx] = g[top_sy][top_sx], g[ny][nx]
            ny, nx = ny + dy[top_direction], nx + dx[top_direction]
    g[top_sy][top_sx] = 0

    bottom_sy, bottom_sx, bottom_direction = machine_bottom, 1, direction, 
    ny, nx = bottom_sy + dy[bottom_direction], bottom_sx + dx[bottom_direction]
    for _ in range(bottom_road):
        if 0 <= ny < r and 0 <= nx < c:
            g[ny][nx], g[bottom_sy][bottom_sx] = g[bottom_sy][bottom_sx], g[ny][nx]
            ny, nx = ny + dy[bottom_direction], nx + dx[bottom_direction]
        else:
            ny, nx = ny - dy[bottom_direction], nx - dx[bottom_direction]
            bottom_direction = (bottom_direction+1) % 4
            ny, nx = ny + dy[bottom_direction], nx + dx[bottom_direction]
            g[ny][nx], g[bottom_sy][bottom_sx] = g[bottom_sy][bottom_sx], g[ny][nx]
            ny, nx = ny + dy[bottom_direction], nx + dx[bottom_direction]
    g[bottom_sy][bottom_sx] = 0

def all_dust(g, r, c):
    answer = 0
    for i in range(r):
        for j in range(c): 
            if g[i][j] > 0:
                answer += g[i][j]
    return answer

for _ in range(T):
    dust(grid, R, C)
    airclean(grid, R, C)

answer = all_dust(grid, R, C)
print(answer)