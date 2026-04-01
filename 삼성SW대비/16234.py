from collections import deque


N, L, R = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def find_union(sy, sx):
    visited[sy][sx] = True
    q = deque()
    q.append((sy, sx))
    temp_union_list = []
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and L <= abs(people[ny][nx] - people[y][x]) <= R:
                temp_union_list.append([ny, nx])
                visited[ny][nx] = True
                q.append((ny, nx))
    if temp_union_list:
        temp_union_list.append([sy,sx])
        union_list.append(temp_union_list)

def move(ul):
    length = len(ul)
    union_people = 0
    for i in ul:
        union_people += people[i[0]][i[1]]
    people_seperate = union_people // length
    for j in ul:
        people[j[0]][j[1]] = people_seperate


count = 0
while True:
    union_list = []
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                find_union(i, j)
    if not union_list:
        break
    for k in union_list:
        move(k)
    count += 1

print(count)