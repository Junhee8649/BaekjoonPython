N = input()
num_list = sorted(N, reverse=True)
answer = ""
for num in num_list:
    answer += num
print(answer)