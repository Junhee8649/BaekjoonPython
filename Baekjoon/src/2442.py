N = int(input())

for i in range(1, N+1):
    a = " " * (N-i)
    b = "*" * (i*2 - 1)
    print(a+b)