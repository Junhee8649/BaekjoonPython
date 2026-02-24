from collections import deque


students = int(input())
lines = list(map(int, input().split()))
new_lines = deque()

for i in range(students):
    new_lines.insert(lines[i], i+1)

new_lines.reverse()
print(*new_lines)