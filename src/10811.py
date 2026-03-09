N, M = map(int, input().split())
basket = [i for i in range(1, N+1)]
for i in range(M):
    i, j = map(int, input().split())
    basket = basket[0:i-1] + basket[-N-1+j:-N-2+i:-1] + basket[j:]
print(*basket)