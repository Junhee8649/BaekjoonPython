P, M, C = map(int, input().split())
X = int(input())
answer = 10**9
for i in range(1, P+1):
    for j in range(1, M+1):
        for k in range(1, C+1):
            answer = min(abs((i+j)*(j+k)-X),answer)
print(answer)