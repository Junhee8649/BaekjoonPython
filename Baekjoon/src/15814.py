S = list(input())
T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    S[A], S[B] = S[B], S[A]
print("".join(S))