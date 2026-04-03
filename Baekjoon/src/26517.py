k = int(input())
a, b, c, d = map(int, input().split())

if k * a + b == k * c + d:
    print(f"Yes {k * a + b}")
else:
    print("No")