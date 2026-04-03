from math import comb

n, k = map(int, input().split())
pascal = comb(n-1, k-1)
print(pascal)