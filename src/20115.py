N = int(input())
drinks = list(map(int, input().split()))
drinks.sort()
energy = drinks[-1]
for i in range(N-1):
    energy += drinks[i] / 2

print(energy)