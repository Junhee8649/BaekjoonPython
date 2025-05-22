n = int(input())
system = {}
for i in range(n):
    train, payment = input().split()
    system[train] = payment

count = 0
for value in system:
    if int(system[value]) > int(system["jinju"]):
        count += 1
print(system["jinju"])
print(count)