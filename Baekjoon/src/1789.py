S = int(input())
N, i = 0, 1
while S >= i:
    N += 1
    S -= i
    i += 1
print(N)