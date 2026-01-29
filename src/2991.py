A, B, C, D = map(int, input().split())
people = list(map(int, input().split()))
time = 0

for person in people:
    time = person
    A_time, C_time = time, time
    count = 0
    while True:
        A_time -= A
        if A_time <= 0:
            count += 1
            break
        A_time -= B
        if A_time <= 0:
            break
    while True:
        C_time -= C
        if C_time <= 0:
            count += 1
            break
        C_time -= D
        if C_time <= 0:
            break
    print(count)