N = int(input())
M = int(input())
S = input()

P = "IO" * N + "I"
count = 0
start = 0

while True:
    pos = S.find(P, start)
    if pos == -1:
        break
    count += 1
    start = pos + 1  # 한 칸씩 이동해서 겹치는 것도 찾기

print(count)