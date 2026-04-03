import sys

def prefix_sum(data):
    n = len(data)
    prefix_sums = [0] * n
    prefix_sums[0] = data[0]
    for k in range(1, n):
        prefix_sums[k] = prefix_sums[k-1] + data[k]
    return prefix_sums
N, M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
num_list = prefix_sum(data)
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i == j:
        print(data[i-1])
    elif i == 1:
        print(num_list[j-1])
    else:
        print(num_list[j-1] - num_list[i-2])