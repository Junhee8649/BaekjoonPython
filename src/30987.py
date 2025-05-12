x1, x2 = map(int, input().split())
a, b, c, d, e = map(int, input().split())

new_a = a / 3
new_b = (b - d) / 2
new_c = c - e

integral = (new_a * x2**3 + new_b * x2**2 + new_c * x2) - (new_a * x1**3 + new_b * x1**2 + new_c * x1)

print(int(integral))