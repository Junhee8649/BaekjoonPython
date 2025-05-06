case = 1
while(True):
    num = int(input())
    if num == 0: break

    n1 = 3 * num
    n2 = n1 / 2 if n1 % 2 == 0 else (n1 + 1) / 2
    n3 = 3 * n2
    n4 = n3 // 9

    print(f"{case}. {'even' if n1 % 2 == 0 else 'odd'} {int(n4)}")
    case += 1