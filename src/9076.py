T = int(input())
for _ in range(T):
    N = list(map(int, input().split()))
    N = sorted(N)[1:-1]
    if N[-1] - N[0] >= 4:
        print("KIN")
    else:
        print(sum(N))
