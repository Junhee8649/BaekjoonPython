N = int(input())
grid = [list(map(int, input().split())) for _ in range(N*N)]
students = [[0] * N for _ in range(N)]
# 북 동 남 서
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
visited = [[False] * N for _ in range(N)]

# student는 학생 한 명의 번호와 좋아하는 학생의 번호 묶음 리스트
def seating(student):
    like_grid = [[0] * N for _ in range(N)]
    like_students = student[1:]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == True:
                continue
            for d in range(4):
                ny, nx = i + dy[d], j + dx[d]
                if 0 <= ny < N and 0 <= nx < N:
                    if students[ny][nx] in like_students:
                        like_grid[i][j] += 1
    max_count = max(max(temp) for temp in like_grid)
    like_max_students = []
    for i in range(N):
        for j in range(N):
            if like_grid[i][j] == max_count and not visited[i][j]:
                like_max_students.append([i,j])
    if len(like_max_students) == 1:
        y, x = like_max_students[0][0], like_max_students[0][1]
        students[y][x] = student[0]
        visited[y][x] = True
    # 2번 조건 시작
    else:
        zero_grid = []
        for i in like_max_students:
            zero_count = 0
            # if visited[i[0]][i[1]] == True:
            #     continue
            for d in range(4):
                ny, nx = i[0] + dy[d], i[1] + dx[d]
                if 0 <= ny < N and 0 <= nx < N:
                    if students[ny][nx] == 0:
                        zero_count += 1
            zero_grid.append(zero_count)
        max_zero_count = max(zero_grid)
        zero_max_stdents = []
        for i in range(len(zero_grid)):
            if zero_grid[i] == max_zero_count:
                zero_max_stdents.append(like_max_students[i])
        if len(zero_max_stdents) == 1:
            y, x = zero_max_stdents[0][0], zero_max_stdents[0][1]
            students[y][x] = student[0]
            visited[y][x] = True
        # 3번 조건 시작
        else:
            zero_max_stdents.sort(key=lambda x: (x[0], x[1]))
            y, x = zero_max_stdents[0][0], zero_max_stdents[0][1]
            students[y][x] = student[0]
            visited[y][x] = True
def happy():
    happy_sum = 0
    for i in range(N):
        for j in range(N):
            count = 0
            for student in grid:
                if student[0] == students[i][j]:
                    student_like = student[1:]
            for d in range(4):
                ny, nx = i + dy[d], j + dx[d]
                if 0 <= ny < N and 0 <= nx < N:
                    if students[ny][nx] in student_like:
                        count += 1
            if count == 4:
                happy_sum += 1000
            elif count == 3:
                happy_sum += 100
            elif count == 2:
                happy_sum += 10
            elif count == 1:
                happy_sum += 1
    print(happy_sum)


for student in grid:
    seating(student)
happy()