N = int(input())
people = 0
for _ in range(N):
    s,c,a,r = map(int, input().split())
    if s >= 1000 or c >= 1600 or a >= 1500 or (r <= 30 and r >= 1):
        people += 1
print(people)