import sys


def insertion_sort(A, N, K):
    temp = 0
    for i in range(1, N):
        loc = i - 1
        newItem = A[i]

        while 0 <= loc and newItem < A[loc]:
            A[loc + 1] = A[loc]
            temp += 1
            loc -= 1
            if temp == K:
                return A
        if loc + 1 != i:
            A[loc + 1] = newItem
            temp += 1
            if temp == K:
                return A
    return -1
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))
answer = insertion_sort(A, N, K)

if type(answer) == list:
    print(*answer)
else:
    print(answer)