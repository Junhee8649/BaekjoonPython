from collections import deque

N, K, L = map(int, input().split())
dust_grid = [list(map(int, input().split())) for _ in range(N)]
cleaner_list = [list(map(int, input().split())) for _ in range(K)]
for i in range(K):
    cleaner_list[i][0] -= 1
    cleaner_list[i][1] -= 1
# 북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
# 청소 방향 우선순위대로의 순서 0번 인덱스부터 오른쪽 -> 아래 -> 왼 -> 위 순서
clean_choose_dr = [[0,1,2], [1,2,3], [2,3,0], [3,0,1]]

def move(sy, sx, cleaner_positions):
    # 현재 서 있는 곳이 오염되어 있다면 거리가 0이므로 이동 없이 제자리 유지!
    if dust_grid[sy][sx] > 0:
        return sy, sx
    visited = [[False] * N for _ in range(N)]
    q = deque()
    q.append((sy, sx, 0))
    temp_close = []
    visited[sy][sx] = True
    min_dist = (N * N) + 1
    while q:
        y, x, dist = q.popleft()
        # 최적화 1: 이미 찾은 최소 거리보다 같거나 멀어지면 더 뻗어나갈 필요 없음
        if dist >= min_dist:
            continue
        for d in range(4):
            ny, nx, ndist = y + dy[d], x + dx[d], dist + 1
            # 최적화 2: 2차원 배열 cleaner_positions로 O(1) 확인
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and dust_grid[ny][nx] != -1 and not cleaner_positions[ny][nx]:
                if dust_grid[ny][nx] > 0:
                    temp_close.append([ndist,ny,nx])
                    min_dist = ndist # 먼지를 찾았으니 최소 거리 갱신
                else:
                    q.append((ny, nx, ndist))
                visited[ny][nx] = True
    # 다 이동했는데 먼지 없으면 에러 나니까
    if not temp_close:
        return sy, sx
    temp_close.sort()
    y, x = temp_close[0][1], temp_close[0][2]
    return y, x

def clean(y, x):
    temp = []
    for i in range(4):
        temp_dust = dust_grid[y][x]
        for j in clean_choose_dr[i]:
            ny, nx = y + dy[j], x + dx[j]
            if 0 <= ny < N and 0 <= nx < N and dust_grid[ny][nx] > 0:
                if dust_grid[ny][nx] > 20:
                    temp_dust += 20
                else:
                    temp_dust += dust_grid[ny][nx]
        temp.append([temp_dust,i])
    temp.sort(key=lambda x: (-x[0], x[1]))
    choose_d = temp[0][1]
    if dust_grid[y][x] > 20:
        dust_grid[y][x] -= 20
    else:
        dust_grid[y][x] = 0
    for i in clean_choose_dr[choose_d]:
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < N and 0 <= nx < N and dust_grid[ny][nx] > 0:
            if dust_grid[ny][nx] > 20:
                dust_grid[ny][nx] -= 20
            else:
                dust_grid[ny][nx] = 0

def dust_all_sum():
    # 동시 추가지만 이전 행동이 영향을 안주니까 덮어쓸 임시 배열 필요없음
    for i in range(N):
        for j in range(N):
            if dust_grid[i][j] > 0:
                dust_grid[i][j] += 5

def dust_spread():
    current_grid = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if dust_grid[i][j] == 0:
                temp_dust_sum = 0
                for d in range(4):
                    ny, nx = i + dy[d], j + dx[d]
                    if 0 <= ny < N and 0 <= nx < N and dust_grid[ny][nx] > 0:
                        temp_dust_sum += dust_grid[ny][nx]
                temp_dust_sum //= 10
                current_grid[i][j] = temp_dust_sum
    for i in range(N):
        for j in range(N):
            dust_grid[i][j] += current_grid[i][j]

def print_all_dust():
    answer = 0
    for i in range(N):
        for j in range(N):
            if dust_grid[i][j] > 0:
                answer += dust_grid[i][j]
    print(answer)
    
for _ in range(L):
    # 최적화 2: 로봇 이동 전, 2차원 배열로 로봇 위치 세팅
    cleaner_positions = [[False] * N for _ in range(N)]
    for cy, cx in cleaner_list:
        cleaner_positions[cy][cx] = True

    for i in range(K):
        sy, sx = cleaner_list[i][0], cleaner_list[i][1]
        # 현재 로봇이 이동할 거니까 내 자리는 비워주기
        cleaner_positions[sy][sx] = False 
        y, x = move(sy, sx, cleaner_positions)
        cleaner_list[i][0], cleaner_list[i][1] = y, x
        # 이동한 새 위치 갱신
        cleaner_positions[y][x] = True

    for i, j in cleaner_list:
        clean(i, j)
    dust_all_sum()
    dust_spread()
    print_all_dust()