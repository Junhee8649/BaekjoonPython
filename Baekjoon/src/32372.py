def direction(x,y,num,all_map):
    if num == 1:
        for i in range(len(all_map)):
            if all_map[i][0] >= x or all_map[i][1] != y:
                all_map[i] = [0, 0]
    elif num == 2:
        for i in range(len(all_map)):
            if all_map[i][0] >= x or all_map[i][1] <= y:
                all_map[i] = [0, 0]
    elif num == 3:
        for i in range(len(all_map)):
            if all_map[i][0] != x or all_map[i][1] <= y:
                all_map[i] = [0, 0]
    elif num == 4:
        for i in range(len(all_map)):
            if all_map[i][0] <= x or all_map[i][1] <= y:
                all_map[i] = [0, 0]
    elif num == 5:
        for i in range(len(all_map)):
            if all_map[i][0] <= x or all_map[i][1] != y:
                all_map[i] = [0, 0]
    elif num == 6:
        for i in range(len(all_map)):
            if all_map[i][0] <= x or all_map[i][1] >= y:
                all_map[i] = [0, 0]
    elif num == 7:
        for i in range(len(all_map)):
            if all_map[i][0] != x or all_map[i][1] >= y:
                all_map[i] = [0, 0]
    else:
        for i in range(len(all_map)):
            if all_map[i][0] >= x or all_map[i][1] >= y: 
                all_map[i] = [0, 0]
    return all_map
        


N, M = map(int, input().split())
all_map = []
for i in range(1,N+1):
    for j in range(1,N+1):
        all_map.append([i,j])
for _ in range(M):
    x, y, num = map(int, input().split())
    temp = direction(x,y,num,all_map)
for answer in temp:
    if answer != [0, 0]:
        print(*answer)
        break