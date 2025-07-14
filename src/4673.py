def selfnum(num):
    string_num = str(num)
    for i in string_num:
        num += int(i)
    return num

list_num = list(_ for _ in range(1, 10001))
for j in range(10000):
    throw_num = selfnum(j)
    if throw_num in list_num:
        list_num.remove(throw_num)

for num in list_num:
    print(num)