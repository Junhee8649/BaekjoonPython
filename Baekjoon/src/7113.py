n, m = map(int, input().split())
count = 0
while True:
    if n > m:
        n -= m
        count += 1
    elif n < m:
        m -= n
        count += 1
    else:
        count += 1
        break
print(count)