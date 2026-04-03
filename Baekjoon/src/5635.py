n = int(input())
students = []
for _ in range(n):
    student = input().split()
    for i in range(1,4):
        student[i] = int(student[i])
    students.append(student)
students.sort(key=lambda x: (x[3],x[2],x[1]))
print(students[-1][0])
print(students[0][0])