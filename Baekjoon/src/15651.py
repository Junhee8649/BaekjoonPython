from itertools import product

N, M = map(int, input().split())
num_list = [num for num in range(1,N+1)]
comb = product(num_list, repeat=M)
sort_list = []

for num in comb:
    sort_list.append(list(num))

for answer in sort_list:
    for i in answer:
        print(i, end=" ")
    print()