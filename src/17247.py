N, M = map(int, input().split())
coordinate = []
for _ in range(N):
    coordinate.append(list(map(int, input().split())))

first_one_y = 0
second_one_y = 0
is_first_y = True
for i in range(N):
    if 1 in coordinate[i]:
        if is_first_y == True:
            first_one_y = i
            is_first_y = False
        else:
            second_one_y = i
first_one_x = 0
second_one_x = 0
for j in range(M):
    if coordinate[first_one_y][j] == 1:
        first_one_x = j

    if coordinate[second_one_y][j] == 1:
        second_one_x = j

print(abs(second_one_y - first_one_y) + abs(second_one_x - first_one_x))