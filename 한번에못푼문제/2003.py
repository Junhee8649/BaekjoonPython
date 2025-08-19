N, M = map(int, input().split())
A = list(map(int, input().split()))
end, count, interver_sum = 0, 0, 0

for start in range(N):
    while interver_sum < M and end < N:
        interver_sum += A[end]
        end += 1
    if interver_sum == M:
        count += 1
    interver_sum -= A[start]
print(count)