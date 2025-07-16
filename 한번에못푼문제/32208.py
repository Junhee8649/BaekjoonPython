import sys

N = int(input())
for _ in range(N):
    x,y,z = map(int, sys.stdin.readline().split())
    if (x+y+z) % 2 ==0:
        print("YES")
    else:
        print("NO")