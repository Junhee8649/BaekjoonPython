B, N, M = map(int, input().split())
items = dict()
sum_price = 0
for _ in range(N):
    item, price = input().split()
    items[item] = price
for _ in range(M):
    want = input()
    sum_price += int(items[want])
if B >= sum_price:
    print("acceptable")
else:
    print("unacceptable")