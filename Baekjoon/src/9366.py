T = int(input())

for i in range(T):
    triangle = list(map(int, input().split()))
    triangle.sort()
    if triangle[2] >= triangle[0] + triangle[1]:
        print(f"Case #{i+1}: invalid!")
    elif triangle[0] == triangle[1] and triangle[0] == triangle[2]:
        print(f"Case #{i+1}: equilateral")
    elif (triangle[0] == triangle[1] and triangle[0] != triangle[2]) or (triangle[0] != triangle[1] and triangle[1] == triangle[2]):
        print(f"Case #{i+1}: isosceles")
    else:
        print(f"Case #{i+1}: scalene")