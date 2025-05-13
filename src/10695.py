t = int(input())
for i in range(1, t+1):
    n, r1, c1, r2, c2 = map(int, input().split())
    if r1 - 1 == r2 or r1 + 1 == r2:
        if c1 + 2 == c2 or c1 - 2 == c2:
            print(f"Case {i}: YES")
        else:
            print(f"Case {i}: NO")
    elif r1 - 2 == r2 or r1 + 2 == r2:
        if c1 + 1 == c2 or c1 - 1 == c2:
            print(f"Case {i}: YES")
        else:
            print(f"Case {i}: NO")
    else:
        print(f"Case {i}: NO")