N = int(input())
A, B = map(int, input().split())
chicken = 0
while N > 0:
    if A > 1:
        A -= 2
        chicken += 1
        N -= 1
    elif B > 0:
        B -= 1
        chicken += 1
        N -= 1
    else:
        break
print(chicken)