N = int(input())
meeting = []

for i in range(N):
    time = list(map(int, input().split()))
    meeting.append(time)

meeting.sort(key=lambda x: (x[1], x[0]))
count = 1
min = meeting[0][1]

for j in range(1, N):
    if meeting[j][0] < min:
        continue
    else:
        count += 1
        min = meeting[j][1]

print(count)