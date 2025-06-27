from collections import deque

n = int(input())
stack = deque([0])
plus_minus = deque([])
is_possible = True
max_num = 1

for i in range(n):
    num = int(input())
    if stack[-1] == num:
        stack.pop()
        plus_minus.append("-")
        continue
    elif stack[-1] < num:
        for j in range(max_num, num+1):
            stack.append(j)
            plus_minus.append("+")
        max_num = num + 1
    else:
        is_possible = False
        break
        
    stack.pop()
    plus_minus.append("-")

if is_possible == True:
    for k in plus_minus:
        print(k)
else:
    print("NO")