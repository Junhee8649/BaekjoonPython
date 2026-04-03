def move(r, c, d):
    if d == 0:
        r -= 1
    elif d == 1:
        c += 1
    elif d == 2:
        r += 1
    elif d == 3:
        c -= 1
    return(r, c)

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = []
count = 0
for i in range(N):
    room.append(list(map(int, input().split())))

while True:
    if room[r][c] == 0:
        count += 1
        room[r][c] = 2

    if room[r+1][c] == 0 or room[r-1][c] == 0 or room[r][c+1] == 0 or room[r][c-1] == 0:
        d = (d - 1) % 4
        temp_r, temp_c = move(r, c, d)
        if room[temp_r][temp_c] == 0:
            r, c = temp_r, temp_c
    else:
        temp_d = (d - 2) % 4
        temp_r, temp_c = move(r, c, temp_d)
        if room[temp_r][temp_c] != 1:
            r, c = temp_r, temp_c
        else:
            break
print(count)