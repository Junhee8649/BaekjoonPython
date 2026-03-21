N = int(input())
students = []
for i in range(N):
    student = list(map(int, input().split()))
    if sum(student) >= 512:
        students.append(sum(student))
if students:
    print(min(students))
else:
    print(-1)