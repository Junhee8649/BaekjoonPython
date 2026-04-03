def is_prime(num):
    if num < 2: return False
    for i in range(2, num):
        if num % i == 0: return False
    return True

T = int(input())
for _ in range(T):
    N = int(input())
    answer = []
    for A in range(1000):
        if is_prime(A*N+A*A):
            answer.append([A, A+N])
    print(len(answer))
    if len(answer) > 0:
        for A, B in answer:
            print(A, B)