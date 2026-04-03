N, M = map(int, input().split())
students = []
for i in range(N):
    students.append(list(map(int, input().split())))

if (N * M) % 2 != 0:
    print("No")
else:
    print("Yes")
    if M % 2 == 0:
        for i in range(N):
            for j in range(0, M, 2):
                temp = students[i][j+1] 
                students[i][j+1] = students[i][j]
                students[i][j] = temp
    else:
        for i in range(N):
            for j in range(0, M-1, 2):
                temp = students[i][j+1] 
                students[i][j+1] = students[i][j]
                students[i][j] = temp
        for k in range(0, N, 2):
            temp = students[k+1][-1]
            students[k+1][-1] = students[k][-1]
            students[k][-1] = temp
    for student in students:
        for person in student:
            print(person, end=" ")
        print()
    