import sys

n, t = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
sort_list = sorted(num_list[:t]) + num_list[t:]
print(*sort_list)