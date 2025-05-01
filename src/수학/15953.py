a_list = {
    1: 5000000,
    **dict.fromkeys(range(2, 4), 3000000),
    **dict.fromkeys(range(4, 7), 2000000),
    **dict.fromkeys(range(7, 11), 500000),
    **dict.fromkeys(range(11, 16), 300000),
    **dict.fromkeys(range(16, 22), 100000)
}
b_list = {
    1: 5120000,
    **dict.fromkeys(range(2, 4), 2560000),
    **dict.fromkeys(range(4, 8), 1280000),
    **dict.fromkeys(range(8, 16), 640000),
    **dict.fromkeys(range(16, 32), 320000)
}

def prize_money(a, b):
    return a_list.get(a, 0) + b_list.get(b, 0)

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(prize_money(a, b))
