n = int(input())
students = input().split()
students_dic = {}
for student in students:
    students_dic[student] = 0
for i in range(n):
    love = input().split()
    for student in love:
        students_dic[student] += 1
sorted_student = sorted(students_dic.items(), key=lambda x: (-x[1], x[0]))
for key, value in sorted_student:
    print(key, value)