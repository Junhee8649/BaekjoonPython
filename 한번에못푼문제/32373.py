import sys

N, k = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

answer = True

for remainder in range(k):
    should_be = set()
    actually_is = set()
    
    pos = remainder
    while pos < N:
        should_be.add(pos)
        actually_is.add(A[pos])
        pos += k
    
    if should_be != actually_is:
        answer = False
        break

print("Yes" if answer else "No")