n, m = map(int, input().split())
bus_num = list(map(int, input().split()))
bus_price = [[0] * n] * n

for i in range(n):
    bus_price[i] = list(map(int, input().split()))

sum = 0
for j in range(m-1):
    sum += bus_price[bus_num[j]-1][bus_num[j+1]-1]

print(sum)