from math import sqrt

def distance(start, end):
    return sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)

coordinate = []
for _ in range(4):
    coordinate.append(list(map(int, input().split())))

all_destination = []
for i in range(1,4):
    sum1 = distance(coordinate[0], coordinate[i])
    sum2 = distance(coordinate[0], coordinate[i])
    if i == 1:
        second_1_distance = distance(coordinate[1], coordinate[2])
        second_2_distance = distance(coordinate[1], coordinate[3])
        sum1 += second_1_distance + distance(coordinate[2], coordinate[3])
        sum2 += second_2_distance + distance(coordinate[3], coordinate[2])
    elif i == 2:
        second_1_distance = distance(coordinate[2], coordinate[1])
        second_2_distance = distance(coordinate[2], coordinate[3])
        sum1 += second_1_distance + distance(coordinate[1], coordinate[3])
        sum2 += second_2_distance + distance(coordinate[3], coordinate[1])
    elif i == 3:
        second_1_distance = distance(coordinate[3], coordinate[1])
        second_2_distance = distance(coordinate[3], coordinate[2])
        sum1 += second_1_distance + distance(coordinate[1], coordinate[2])
        sum2 += second_2_distance + distance(coordinate[2], coordinate[1])
    all_destination.append(sum1)
    all_destination.append(sum2)

print(int(min(all_destination)))