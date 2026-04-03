from collections import deque
import sys

N = int(input())
stack = deque()
for i in range(N):
    num = list(map(int, sys.stdin.readline().split()))
    if num[0] == 1:
        stack.append(num[1])
    elif num[0] == 2:
        if len(stack) == 0:
            print(-1)
        else:
            temp = stack.pop()
            print(temp)
    elif num[0] == 3:
        print(len(stack))
    elif num[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif num[0] == 5:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])