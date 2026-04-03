n = int(input())
time = 0
count = 1
minus = False
x, y = 0, 0

while time < n:  
    if x == y:
        for _ in range(count):
            if time == n: 
                break
            if minus:
                y -= 1
            else:
                y += 1
            time += 1
    else:
        for _ in range(count):
            if time == n:  
                break
            if minus:
                x -= 1
            else:
                x += 1
            time += 1
        count += 1
        minus = not minus

print(x, y)