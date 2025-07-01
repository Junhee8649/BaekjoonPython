N = int(input())
people = list(map(int, input().split()))
min_time = 0

people.sort()

for i in range(N):
    for j in range(i+1):
        min_time += people[j]

print(min_time)