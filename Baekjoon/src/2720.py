T = int(input())
money = [25, 10, 5, 1]
for _ in range(T):
    money_count = [0,0,0,0]
    C = int(input())
    for i in range(4):
        money_count[i] = C // money[i]
        C -= money_count[i] * money[i]
    print(*money_count)