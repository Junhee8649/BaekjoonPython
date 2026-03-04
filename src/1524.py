T = int(input())

for i in range(T):
    space = input()
    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_S = max(S)
    max_B = max(B)

    if max_S >= max_B:
        print("S")
    else:
        print("B")