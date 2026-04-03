N, A, B = map(int, input().split())
A_onion, B_onion = 1, 1
for _ in range(N):
    A_onion += A
    B_onion += B
    if B_onion > A_onion:
        temp = A_onion
        A_onion = B_onion
        B_onion = temp
    elif A_onion == B_onion:
        B_onion -= 1
print(A_onion, B_onion)