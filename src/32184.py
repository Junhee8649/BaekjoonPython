A, B = map(int, input().split())

count = 0

# A가 짝수라면 A를 먼저 세로로 촬영
if A % 2 == 0:
    count += 1
    A += 1

# B가 홀수라면 B를 마지막에 세로로 촬영
if B % 2 == 1:
    count += 1
    B -= 1

count += (B - A + 1) // 2

print(count)