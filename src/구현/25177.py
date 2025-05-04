n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
max_value = 0

if n < m:
    for i in range(0, n):
        max_value = max(b[i] - a[i], max_value)
    for j in range(n, m):
        max_value = max(b[j], max_value)
else:
    for i in range(0, m):
        max_value = max(b[i] - a[i], max_value)
    
print(max_value)