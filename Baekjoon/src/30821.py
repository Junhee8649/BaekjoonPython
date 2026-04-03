N = int(input())
numerator = N*(N-1)*(N-2)*(N-3)*(N-4) 
denominator = 5*4*3*2*1
stars = numerator // denominator
print(stars)