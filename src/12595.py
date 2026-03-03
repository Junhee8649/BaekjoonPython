N = int(input())
for i in range(N):
    G = int(input())
    people = list(map(int, input().split()))
    for j in range(G):
        if people.count(people[j]) == 1:
            print(f"Case #{i+1}: {people[j]}")
            break