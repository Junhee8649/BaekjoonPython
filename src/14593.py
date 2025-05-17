n = int(input())
max = [0] * 3
first_grade = 1

for i in range(1, n+1):
    participant = list(map(int, input().split()))
    if participant[0] > max[0]:
        max = participant
        first_grade = i
    elif participant[0] == max[0]:
        if participant[1] < max[1]:
            max = participant
            first_grade = i
        elif participant[1] == max[1]:
            if participant[2] < max[2]:
                max = participant
                first_grade = i

print(first_grade)    