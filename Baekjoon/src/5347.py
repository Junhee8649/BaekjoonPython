def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

def lcm_by_gcd(a, b):
    return (a * b) // gcd(a, b)

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(lcm_by_gcd(a, b))