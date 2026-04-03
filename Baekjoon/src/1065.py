N = int(input())
count = 0

for num in range(1,N+1):
    if num < 100:
        count += 1
    else:
        str_num = str(num)
        answer = True
        for i in range(len(str_num)-2):
            if int(str_num[i]) - int(str_num[i+1]) != int(str_num[i+1]) - int(str_num[i+2]):
                answer = False
        if answer:
            count += 1

print(count)