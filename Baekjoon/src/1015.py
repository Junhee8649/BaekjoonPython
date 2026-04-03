N = int(input())
A = list(map(int, input().split()))
temp = []
for i in range(N):
    temp.append([A[i], i])
temp.sort()

P = [0] * N
for j in range(N):
    P[temp[j][1]] = j
for num in P:
    print(num, end=" ")