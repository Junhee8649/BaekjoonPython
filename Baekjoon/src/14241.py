N = int(input())
slime = list(map(int, input().split()))
slime.sort()
plus = slime[0]
score = 0
for i in range(1,N):
    score += plus * slime[i]
    plus += slime[i]
print(score)