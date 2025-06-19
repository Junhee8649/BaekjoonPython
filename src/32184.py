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

# 이제 A는 홀수, B는 짝수 (또는 A > B)
# 남은 구간은 모두 완전한 면들이므로 가로로 촬영
if A <= B:
    count += (B - A + 1) // 2

print(count)