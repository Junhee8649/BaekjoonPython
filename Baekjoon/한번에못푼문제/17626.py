import math
import sys

n = int(sys.stdin.readline())

# 1. N보다 작거나 같은 모든 제곱수를 'set'에 저장
max_val = int(math.sqrt(n))
squares = {i * i for i in range(1, max_val + 1)}

# 결과를 출력했는지 확인하는 플래그
printed = False

# 2. 1개의 제곱수로 표현 가능한 경우 (N이 제곱수)
if n in squares:
    print(1)
    printed = True

# 3. 2개의 제곱수로 표현 가능한 경우 (printed가 False일 때만 실행)
if not printed:
    for s1 in squares:
        if (n - s1) in squares:
            print(2)
            printed = True
            break  # 2를 찾았으면 더 이상 반복할 필요 없음

# 4. 3개의 제곱수로 표현 가능한 경우 (printed가 False일 때만 실행)
if not printed:
    for s1 in squares:
        # 3을 찾으면 바깥쪽 루프도 탈출하기 위한 플래그
        found_3 = False 
        for s2 in squares:
            if (n - s1 - s2) in squares:
                print(3)
                printed = True
                found_3 = True
                break  # 안쪽 루프 탈출
        if found_3:
            break  # 바깥쪽 루프 탈출

# 5. 1, 2, 3개로 안 되는 경우 (printed가 False일 때만 실행)
if not printed:
    print(4)