import sys

# 반올림 방식 중 가장 직관적이고 속도도 빠름
def round_num(num):
    return int(num + 0.5)

# 대량으로 입력을 받을 때는 sys.stdin.readline을 사용하자!!
input = sys.stdin.readline
n = int(input())
level = []

for i in range(n):
    level.append(int(input()))

level.sort()
max_or_min = round_num(n * 0.15)

if max_or_min > 0:
    level = level[max_or_min:-max_or_min]

level_avg = round_num(sum(level) / len(level) if level else 0)
print(level_avg)