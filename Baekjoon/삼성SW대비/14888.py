from math import inf


N = int(input())
A = list(map(int, input().split()))
# 덧셈 -> 뺄셈 -> 곱셈 -> 나눗셈 순서
operators = list(map(int, input().split()))
max_answer, min_answer = -inf, inf

operator_list = []

def dfs(depth):
    global max_answer, min_answer

    if depth == N-1:
        temp = calculator(operator_list)
        max_answer = max(max_answer, temp)
        min_answer = min(min_answer, temp)
        return
    
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            operator_list.append(i)
            dfs(depth+1)
            operator_list.pop()
            operators[i] += 1

def calculator(ops):
    total = A[0]
    for i in range(N - 1):
        if ops[i] == 0:     # 덧셈
            total += A[i+1]
        elif ops[i] == 1:   # 뺄셈
            total -= A[i+1]
        elif ops[i] == 2:   # 곱셈
            total *= A[i+1]
        elif ops[i] == 3:   # 나눗셈
            if total < 0:
                total = -1 * (abs(total) // A[i+1])
            else:
                total = total // A[i+1]
    return total

dfs(0)
print(max_answer)
print(min_answer)