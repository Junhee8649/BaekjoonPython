N, M = map(int, input().split())
score = list(map(int, input().split()))
student_score = []
for i in range(M):
    student = list(input().split())
    sum = 0
    for j in range(1, N+1):
        if student[j] == "O":
            sum += score[j-1]
    student_score.append([int(student[0]), sum])
student_score.sort(key=lambda x: (-x[1], x[0]))
print(student_score[0][0], student_score[0][1])