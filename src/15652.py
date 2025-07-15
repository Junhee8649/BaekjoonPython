from itertools import combinations_with_replacement, product

N, M = map(int, input().split())
num_list = [num for num in range(1,N+1)]
comb = combinations_with_replacement(num_list, M)
sort_list = []

for num in comb:
    sort_list.append(list(num))

for answer in sort_list:
    for i in answer:
        print(i, end=" ")
    print()