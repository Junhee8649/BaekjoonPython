origin_code = input()
count = int(input())
database = []

for i in range(count):
    database_code = input()
    correct = True
    for j in range(len(origin_code)):
        if origin_code[j] == "*":
            continue
        if origin_code[j] != database_code[j]:
            correct = False
            break
    if correct == True:
        database.append(database_code)

print(len(database))
for i in database:
    print(i)