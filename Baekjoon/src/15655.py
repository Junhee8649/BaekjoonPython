from itertools import combinations

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
comb = combinations(num_list, M)
sort_list = []

for num in comb:
    sort_list.append(list(num))

for sub_list in sort_list:
    sub_list.sort()
sort_list.sort()

for answer in sort_list:
    for i in answer:
        print(i, end=" ")
    print()