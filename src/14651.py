N = int(input())
print(0 if N == 1 else (2 * pow(3, N - 2)) % 1000000009)