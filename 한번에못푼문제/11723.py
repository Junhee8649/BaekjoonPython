import sys

input = sys.stdin.readline
M = int(input())
program = set()

for i in range(M):
    operation = input().split()
    if len(operation) == 2:
        op, num = operation[0], int(operation[1])
        if op == "add":
            program.add(num)
        elif op == "remove":
            program.discard(num)
        elif op == "check":
            print(1 if num in program else 0)
        elif op == "toggle":
            program.discard(num) if num in program else program.add(num)
    else:        
        if operation[0] == "all":
            program = set(range(1, 21))
        elif operation[0] == "empty":
            program = set()