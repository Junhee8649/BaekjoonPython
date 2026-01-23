from math import pi


w, h = map(int, input().split())
r = int(input())
hanstar = w*h - r*r*pi/4
print(round(hanstar, 2))
print(hanstar)