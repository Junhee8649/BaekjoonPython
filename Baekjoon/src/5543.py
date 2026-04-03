high_burger = int(input())
middle_burger = int(input())
low_burger = int(input())
coke = int(input())
sprite = int(input())

cheapest_set = min(high_burger, middle_burger, low_burger) + min(coke, sprite) - 50

print(cheapest_set)