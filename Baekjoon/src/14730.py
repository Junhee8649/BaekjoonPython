n = int(input())
sum_f1 = 0

for i in range(n):
    c, k = map(int, input().split())
    sum_f1 += c * k

print(sum_f1)