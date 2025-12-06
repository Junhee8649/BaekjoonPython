N = int(input())
students = []
for _ in range(N):
    student = input().split()
    name = student[0]
    kr = int(student[1])
    eg = int(student[2])
    math = int(student[3])
    students.append([name, kr, eg, math])
students.sort(key=lambda x: (-x[1],x[2],-x[3],x[0]))
for student in students:
    print(student[0])
