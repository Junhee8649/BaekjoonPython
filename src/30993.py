from math import factorial


def combination(n, r):
    return factorial(n) / factorial(n-r) / factorial(r)

n, a, b, c = map(int, input().split())

A_combination = combination(n, a)
B_combination = combination(n-a, b)
C_combination = combination(n-a-b, c)

print(int(A_combination * B_combination * C_combination))