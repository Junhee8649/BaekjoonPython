n = int(input())
is_choose = False
for _ in range(n):
    num = int(input())
    if not is_choose:
        main_num = num
        is_choose = True
        continue
    if num % main_num == 0:
        print(num)
        is_choose = False