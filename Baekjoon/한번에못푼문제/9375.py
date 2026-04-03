T = int(input())

for _ in range(T):
    n = int(input())
    
    clothes_count = {}
    for _ in range(n):
        name, category = input().split()
        clothes_count[category] = clothes_count.get(category, 0) + 1
    
    result = 1
    for count in clothes_count.values():
        result *= (count + 1)
    
    print(result - 1)