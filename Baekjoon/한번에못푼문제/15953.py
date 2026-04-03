# 카카오 코테 여러개의 키 하나의 값 문제
a_list = {
    1: 5000000,
    # dict.fromkeys(keys, value) 함수는 주어진 키들을 모두 동일한 값으로 매핑하는 새 딕셔너리를 생성
    # **는 딕셔너리 언패킹(unpacking) 연산자
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
