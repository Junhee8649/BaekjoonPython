from collections import deque


N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
# 북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
answer = 0

def bfs(g):
    visited = [[False] * M for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(M):
            if g[i][j] == 2:
                q.append((i, j))
                visited[i][j] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                if g[ny][nx] != 1:
                    visited[ny][nx] = True 
                    g[ny][nx] = 2
                    q.append((ny, nx))
    count = 0
    for i in range(N):
        for j in range(M):
            if g[i][j] == 0:
                count += 1
    return count

def dfs(depth, start):
    global answer
    if depth == 3:
        temp = [row[:] for row in grid]
        count = bfs(temp)
        answer = max(answer, count)
        return answer
    for i in range(start, N * M):
        y = i // M
        x = i % M
        if grid[y][x] == 0:
            grid[y][x] = 1
            dfs(depth+1, i + 1)
            grid[y][x] = 0
dfs(0, 0)
print(answer)