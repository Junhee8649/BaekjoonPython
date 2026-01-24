N = int(input())
study = []
for _ in range(N):
    a, b = input().split()
    b = int(b)
    study.append([a,b])
study.sort(key=lambda x: x[1])
print(study[-1][0])