B, C, D = map(int, input().split())
burger = list(map(int, input().split()))
side = list(map(int, input().split()))
juice = list(map(int, input().split()))

max_sum = sum(burger) + sum(side) + sum(juice)
discount_sum = 0
count = min(B, C, D)

for i in range(count):
    burger_choice = max(burger)
    side_choice = max(side)
    juice_choice = max(juice)   

    discount_sum += (burger_choice + side_choice + juice_choice) * 0.9
    burger.remove(burger_choice)
    side.remove(side_choice)
    juice.remove(juice_choice)

if len(burger) != 0:
    for i in burger:
        discount_sum += i
        
if len(side) != 0:
    for i in side:
        discount_sum += i

if len(juice) != 0:
    for i in juice:
        discount_sum += i

print(max_sum)
print(int(discount_sum))