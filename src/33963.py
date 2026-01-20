N = int(input())
count = 0
money_len = len(str(N))
while True:
    N *= 2
    if len(str(N)) != money_len:
        break
    count += 1
print(count)