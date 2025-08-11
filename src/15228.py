from math import ceil

n = int(input())
min_day = n

for k in range(n):
    printers = 2 ** k  
    statue_days = ceil(n / printers) 
    total_days = k + statue_days
    min_day = min(min_day, total_days)

print(min_day)