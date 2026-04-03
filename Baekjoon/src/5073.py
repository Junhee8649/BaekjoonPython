triangle = list(map(int, input().split()))

while triangle[0] != 0 or triangle[1] != 0 or triangle[2] != 0:
    triangle.sort()
    if triangle[0] + triangle[1] > triangle[2]:
        if triangle[0] == triangle[1] and triangle[1] == triangle[2]:
            print("Equilateral")
        elif triangle[0] != triangle[1] and triangle[0] != triangle[2] and triangle[1] != triangle[2]:
            print("Scalene")
        else:
            print("Isosceles")
    else:
        print("Invalid")
    
    triangle = list(map(int, input().split()))