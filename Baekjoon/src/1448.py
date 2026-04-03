import sys

N = int(input())
straw = []
for _ in range(N):
    straw.append(int(sys.stdin.readline()))
straw.sort(reverse=True)

no_triangle = True
for i in range(N-2):
    if straw[i+1] + straw[i+2] > straw[i]:
        print(straw[i] + straw[i+1] + straw[i+2])
        no_triangle = False
        break
    
if no_triangle:
    print(-1)