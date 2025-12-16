N = int(input())
price = []
for _ in range(N):
    price.append(int(input()))
support = max(price) // 2
pay = min(price) - support

if pay >= 0:
    print(pay)
else:
    print(0)