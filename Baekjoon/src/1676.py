from math import factorial

n = int(input())
n_fac = reversed(str(factorial(n)))

count = 0
for i in n_fac:
    if i == "0":
        count += 1
    else:
        break

print(count)