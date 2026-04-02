N = int(input())
grid = [list(map(int, input().split())) for _ in range(N*N)]
students = [[0] * N for _ in range(N)]
# 북 동 남 서
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
visited = [[False] * N for _ in range(N)]

# student는 학생 한 명의 번호와 좋아하는 학생의 번호 묶음 리스트
def seating(student):
    like_students = student[1:]
    candidates = [] # 후보 칸들을 담을 리스트
    
    for i in range(N):
        for j in range(N):
            if visited[i][j] == True:
                continue
            
            # 현재 칸(i, j) 기준 좋아하는 학생 수와 빈 칸 수 카운트
            like_count = 0
            zero_count = 0
            for d in range(4):
                ny, nx = i + dy[d], j + dx[d]
                if 0 <= ny < N and 0 <= nx < N:
                    if students[ny][nx] in like_students:
                        like_count += 1
                    if students[ny][nx] == 0:
                        zero_count += 1
            
            # 조건 1, 2, 3을 튜플로 한 번에 묶어서 후보에 추가
            # 내림차순(가장 많은 것 우선)을 위해 count 앞에는 마이너스(-)를 붙임
            candidates.append((-like_count, -zero_count, i, j))
            
    # 튜플 정렬 (1순위: -like_count, 2순위: -zero_count, 3순위: i 오름차순, 4순위: j 오름차순)
    candidates.sort()
    
    # 정렬된 리스트의 0번째가 가장 우선순위가 높은 칸
    y, x = candidates[0][2], candidates[0][3]
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