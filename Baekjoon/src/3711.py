N = int(input())
for _ in range(N):
    students = []
    G = int(input())
    for _ in range(G):
        students.append(int(input()))
    m = 1
    while True:
        student_set = set()
        for student in students:
            student_set.add(student % m)
        if len(student_set) == len(students):
            print(m)
            break
        m += 1