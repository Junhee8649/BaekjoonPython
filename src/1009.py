T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    if a % 10 == 0:
        print(10)
        continue
    a = int(str(a)[-1])
    if a == 0 or a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4:
        if b % 2 == 0:
            print(6)
        else:
            print(4)
    elif a == 9:
        if b % 2 == 0:
            print(1)
        else:
            print(9)
    elif a == 2:
        if  b % 4 == 1:
            print(2)
        elif b % 4 == 2:
            print(4)
        elif b % 4 == 3:
            print(8)
        elif b % 4 == 0:
            print(6)
    elif a == 3:
        if  b % 4 == 1:
            print(3)
        elif b % 4 == 2:
            print(9)
        elif b % 4 == 3:
            print(7)
        elif b % 4 == 0:
            print(1)
    elif a == 7:
        if  b % 4 == 1:
            print(7)
        elif b % 4 == 2:
            print(9)
        elif b % 4 == 3:
            print(3)
        elif b % 4 == 0:
            print(1)
    elif a == 8:
        if  b % 4 == 1:
            print(8)
        elif b % 4 == 2:
            print(4)
        elif b % 4 == 3:
            print(2)
        elif b % 4 == 0:
            print(6)