n, T = map(int, input().split())
time = list(map(int, input().split()))
sum, count = 0, 0

for i in time:
    sum += i
    if sum <= T:
        count += 1
    else:
        break

print(count)