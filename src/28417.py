N = int(input())
people = []
for _ in range(N):
    person = list(map(int, input().split()))
    run = person[:2]
    trick = person[2:]
    trick.sort(reverse=True)
    score = max(run) + trick[0] + trick[1]
    people.append(score)
print(max(people))