n = int(input())
for _ in range(n):
    a, b = map(float, input().split())
    answer = abs(a-b)
    print(round(answer, 1))