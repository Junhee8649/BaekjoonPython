from collections import deque

S = input().strip()
stack = deque(S[0])
S = S[1:]
for s in S:
    if len(stack) == 0:
        stack.append(s)
        continue
    if stack[-1] == '(' and s == ')':
        stack.append(s)
        stack.pop()
        stack.pop()
        continue
    stack.append(s)

print(len(stack))