def divide(n):
    if n == 0:
        return "-"
    line = divide(n-1)
    middle = " " * (3**(n-1))
    return line + middle + line

while True:
    try:
        n = int(input())
        print(divide(n))
    except EOFError:
        break