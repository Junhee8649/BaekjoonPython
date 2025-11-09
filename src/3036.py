def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

N = int(input())
rings = list(map(int, input().split()))

for i in range(1,N):
    temp = gcd(rings[0], rings[i])
    numerator = rings[0] // temp
    denominator = rings[i] // temp
    print(f"{numerator}/{denominator}")