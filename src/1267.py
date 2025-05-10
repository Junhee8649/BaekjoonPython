def Y_phone_plan(time):
    return 10 * ((time // 30) + 1)
def M_phone_plan(time):
    return 15 * ((time // 60) + 1)

n = int(input())
time = list(map(int, input().split()))
Y_sum = 0
M_sum = 0
for i in range(n):
    Y_sum += Y_phone_plan(time[i])
    M_sum += M_phone_plan(time[i])

if Y_sum < M_sum:
    print(f"Y {Y_sum}")
elif M_sum < Y_sum:
    print(f"M {M_sum}")
else:
    print(f"Y M {Y_sum}")