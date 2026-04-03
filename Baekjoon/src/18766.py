T = int(input())
for _ in range(T):
    n = int(input())
    a = input().split()
    b = input().split()
    a.sort()
    b.sort()
    if a == b:
        print("NOT CHEATER")
    else:
        print("CHEATER")    