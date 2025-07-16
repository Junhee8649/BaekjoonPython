import sys

N = int(input())
all_sides = set()

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    all_sides.update([a, b, c])
if len(all_sides) == N * 3:
    print(0)
else:
    print(1)