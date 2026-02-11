sleep = int(input())
get_up = int(input())
total_time = 0

if sleep <= 23 and sleep >= 20:
    total_time += 24 - sleep + get_up
else:
    total_time += (get_up - sleep)

print(total_time)