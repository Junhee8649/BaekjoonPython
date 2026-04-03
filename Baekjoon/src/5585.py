money = int(input())
otsuri = 1000 - money
count = 0

while otsuri != 0:
    if otsuri >= 500:
        otsuri -= 500
        count += 1
    elif otsuri >= 100:
        otsuri -= 100
        count += 1
    elif otsuri >= 50:
        otsuri -= 50
        count += 1
    elif otsuri >= 10:
        otsuri -= 10
        count += 1
    elif otsuri >= 5:
        otsuri -= 5
        count += 1
    else:
        otsuri -= 1
        count += 1
print(count)