num_list = list(map(int, input().split()))
sort_num = sorted(num_list)

while num_list != sort_num:
    for i in range(len(num_list)-1):
        if num_list[i] > num_list[i+1]:
            temp = num_list[i]
            num_list[i] = num_list[i+1]
            num_list[i+1] = temp
            print(*num_list)
            