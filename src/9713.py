T = int(input())
for _ in range(T):
    N = int(input())
    answer = 0
    for num in range(1, N+1, 2):
        answer += num
    print(answer)