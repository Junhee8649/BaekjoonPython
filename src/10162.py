T = int(input())
A, B, C = 0, 0, 0

if T >= 300:
    A = T // 300
    T = T % 300

if T >= 60:
    B = T // 60
    T = T % 60

if T >= 10:
    C = T // 10
    T = T % 10

if T > 0:
    print(-1)
else:
    print(A, B, C)