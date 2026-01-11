N = int(input())
people = []
for _ in range(N):
    people.append(input())
people.sort()
for i in range(N):
    if len(people[i]) == 3:
        print(people[i])
        break