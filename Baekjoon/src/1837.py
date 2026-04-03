import sys


def get_primes(K):
    sieve = [True] * K
    for p in range(2, int(K**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, K, p):
                sieve[i] = False
    return [p for p in range(2, K) if sieve[p]]
input = sys.stdin.readline
P, K = map(int,input().split())
is_good = True
for num in get_primes(K):
    if P % num == 0:
        print("BAD", num)
        is_good = False
        break
if is_good:
    print("GOOD")