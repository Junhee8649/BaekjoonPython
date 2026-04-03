temp = input().lower()
moeum = ['a','e','i','o','u']
while temp != '#':
    count = 0
    for i in temp:
        if i in moeum:
            count += 1
    print(count)
    temp = input().lower()