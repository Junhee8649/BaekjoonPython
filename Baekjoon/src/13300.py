N, K = map(int, input().split())
room = [[0 for _ in range(2)] for _ in range(6)]
min_room = 0
for _ in range(N):
    S, Y = map(int, input().split())
    room[Y-1][S] += 1
for i in range(6):
    for j in range(2):
        temp = room[i][j] // K
        if room[i][j] % K > 0:
            min_room += (temp+1)
        else:
            min_room += temp
print(min_room)