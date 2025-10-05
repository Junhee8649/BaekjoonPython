N = int(input())
num = []
if N % 2 == 0:
    last = N
else:
    last = N-1
for first in range(1, last//2+1):
    num.append(N-first+1)
    num.append(first)
if last == N-1:
    num.append(last//2+1)
reverse = num[::-1]
print(*reverse)