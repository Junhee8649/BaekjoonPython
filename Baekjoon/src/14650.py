from itertools import product

N = int(input())
numbers = [0,1,2]
count = 0
for com in product(numbers, repeat=N-1):
    if sum(com) % 3 == 1 or sum(com) % 3 == 2:
        count += 1
print(count)