M, N = map(int, input().split())
answer_list = [0] * 5
for i in range(M):
    window_list = [0] * N
    input()
    for j in range(4):
        window = input()
        for k in range(1,N*5+1,5):
            if window[k] == "*":
                window_list[k//5] += 1
    for win in window_list:
        answer_list[win] += 1
input()

for answer in answer_list:
    print(answer, end=" ")