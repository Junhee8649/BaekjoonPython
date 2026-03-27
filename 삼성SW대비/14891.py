from collections import deque


def wheel(gear, clock):
    # gear는 이미 선택된 톱니바퀴 리스트
    gear = deque(gear)
    gear.rotate(clock)
    return gear

# 왼쪽 톱니들을 연쇄적으로 확인하는 함수
def check_left(gears, gear_num, clock):
    if gear_num < 0:
        return
    # 인덱스 음수 나올 수 있어서 본 톱니바퀴가 아니라 왼쪽 톱니바퀴를 중심으로 gear_num으로 잡은거
    if gears[gear_num][2] != gears[gear_num+1][6]:
        check_left(gears, gear_num - 1, -clock)
        gears[gear_num] = wheel(gears[gear_num], clock)

# 오른쪽 톱니들을 연쇄적으로 확인하는 함수
def check_right(gears, gear_num, clock):
    if gear_num > 3:
        return
    if gears[gear_num][6] != gears[gear_num-1][2]:
        check_right(gears, gear_num + 1, -clock)
        gears[gear_num] = wheel(gears[gear_num], clock)

def set_score(gears):
    one = 1 if gears[0][0] == 1 else 0
    two = 2 if gears[1][0] == 1 else 0
    three = 4 if gears[2][0] == 1 else 0
    four = 8 if gears[3][0] == 1 else 0
    score = one + two + three + four
    return score

gears = [list(map(int, input())) for _ in range(4)]
K = int(input())
for _ in range(K):
    gear_num, clock = map(int, input().split())
    gear_num -= 1
    check_left(gears, gear_num-1, -clock)
    check_right(gears, gear_num+1, -clock)
    gears[gear_num] = wheel(gears[gear_num], clock)
score = set_score(gears)
print(score)    