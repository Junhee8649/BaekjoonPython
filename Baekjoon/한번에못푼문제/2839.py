N = int(input())
count = 0

while N >= 0:
    if N % 5 == 0:  # 5로 나누어떨어지면
        count += N // 5
        print(count)
        break
    N -= 3  # 안 되면 3kg 봉지 하나 사용
    count += 1
else:
    print(-1)  # N이 음수가 되면 불가능