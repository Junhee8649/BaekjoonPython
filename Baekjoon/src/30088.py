def prefix_sum(data):
    n = len(data)
    prefix_sums = [0] * n
    prefix_sums[0] = data[0]
    for i in range(1, n):
        prefix_sums[i] = prefix_sums[i-1] + data[i]
    return prefix_sums

N = int(input())
people = []
for _ in range(N):
    person = list(map(int, input().split()))
    people.append(sum(person[1:]))
people.sort()
print(sum(prefix_sum(people)))