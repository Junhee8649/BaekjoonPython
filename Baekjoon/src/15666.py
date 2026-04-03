from itertools import combinations_with_replacement, product

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
comb = combinations_with_replacement(num_list, M)
sort_list = []

for num in comb:
    sort_list.append(list(num))

for sub_list in sort_list:
    sub_list.sort()
sort_list.sort()
set_list = set(tuple(x) for x in sort_list)
result_list = [list(x) for x in set_list]
for sub_list in result_list:
    sub_list.sort()
result_list.sort()
for answer in result_list:
    for i in answer:
        print(i, end=" ")
    print()