ISBN = input()
sum = 0
index = 0
m = int(ISBN[12])

for i in range(0, 11, 2):
    if ISBN[i] == '*':
        index = i
        continue
    sum += int(ISBN[i])

for j in range(1, 12, 2):
    if ISBN[j] == '*':
        index = j
        continue
    sum += int(ISBN[j]) * 3

lost_num = 1

for k in range(10):
    #홀수번째
    if (index+1) % 2 != 0:
        if (sum + k + m) % 10 == 0:
            lost_num = k
    #짝수번째
    else:
        if (sum + 3*k + m) % 10 == 0:
            lost_num = k

print(lost_num)