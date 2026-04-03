N = int(input())
num_list = []
for i in range(N):
    num_list.append(list(map(int, input().split())))
if N >= 3:
    b = num_list[-2][-1]
    a = num_list[-3][-2] + num_list[-3][-1]
    k = (a - b) // 2
    answer = num_list[-3]
    for num in range(len(answer)):
        answer[num] -= k
    answer[-3] = k
    print(*answer)
else:
    another = num_list[0][-1] - 1
    print(1, another)