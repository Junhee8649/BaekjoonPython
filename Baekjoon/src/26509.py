n = int(input())
for _ in range(n):
    tri1 = list(map(int, input().split()))
    tri2 = list(map(int, input().split()))
    tri1.sort()
    tri2.sort()
    if (tri1[0] ** 2 + tri1[1] ** 2) == tri1[2] ** 2 and tri1 == tri2:
        print("YES")
    else:
        print("NO")