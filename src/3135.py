A, B = map(int, input().split())
N = int(input())
like = [abs(A-B)-1]
for i in range(N):
    temp = int(input())
    like.append(abs(temp - B))
print(min(like) + 1)