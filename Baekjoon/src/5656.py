def operation(a, b, op):
    a, b = int(a), int(b)
    if op == ">":
        return a > b
    elif op == ">=":
        return a >= b
    elif op == "<":
        return a < b
    elif op == "<=":
        return a <= b
    elif op == "==":
        return a == b
    else:
        return a != b
    
a, op, b = input().split()
count = 0
while op != "E":
    count += 1
    if operation(a, b, op):
        answer = "true"
    else:
        answer = "false"
    print(f"Case {count}: {answer}")
    a, op, b = input().split()