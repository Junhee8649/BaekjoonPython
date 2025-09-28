N, M, A, B = map(int, input().split())
if 3*N - M > 0:
    print((3*N - M) * A + B)
else:
    print(0)