n = int(input())
p = int(input())
S = list(map(int, input().split()))

for i in range(p, p+n):
    if i not in S:
        print(i)
        break
    