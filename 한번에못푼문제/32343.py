from itertools import combinations

N = int(input())
a, b = map(int, input().split())

def generate_numbers(n, count):
    """n자리에서 정확히 count개의 1을 가지는 모든 수들 생성"""
    numbers = []
    for position in combinations(range(n), count):
        num = 0
        for pos in position:
            num |= (1 << (n-1-pos))  # 왼쪽부터 pos번째에 1 설정
        numbers.append(num)
    return numbers

x_numbers = generate_numbers(N, a)
y_numbers = generate_numbers(N, b)

max_xor = 0
for x in x_numbers:
    for y in y_numbers:
        max_xor = max(max_xor, x ^ y)

print(max_xor)