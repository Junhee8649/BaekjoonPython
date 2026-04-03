N = input()
N_list = []
for i in N:
    N_list.append(i)
all_sum = 0
if '0' in N_list:
    for i in N_list:
        all_sum += int(i)
    if all_sum % 3 == 0:
        N_list.sort(reverse=True)
        biggest = ''.join(N_list)
        print(biggest)
    else:
        print(-1)
else:
    print(-1)