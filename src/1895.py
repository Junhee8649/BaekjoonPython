def nine_median(list):
    list = sorted(list)
    return list[4]

R, C = map(int, input().split())
I, J = [], []
for _ in range(R):
    I.append(list(map(int, input().split())))
T = int(input())

for i in range(R-2):
    for j in range(C-2):
        temp_list = []
        for k in range(3):
            for l in range(3):
                temp_list.append(I[i+k][j+l])
        J.append(nine_median(temp_list))
count = 0
for a in J:
    if a >= T:
        count += 1
print(count)