from itertools import combinations, permutations

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
comb = permutations(num_list, M)
sort_list = []

for num in comb:
    sort_list.append(list(num))

sort_list.sort()

for answer in sort_list:
    for i in answer:
        print(i, end=" ")
    print()