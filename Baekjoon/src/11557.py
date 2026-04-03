T = int(input())
for _ in range(T):
    schools = []
    N = int(input())
    for _ in range(N):
        school = input().split()
        school[1] = int(school[1])
        schools.append(school)
    schools.sort(key=lambda x: x[1])
    print(schools[-1][0])