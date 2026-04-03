N = int(input())
contact = []
for _ in range(N):
    contact.append(input())
M = int(input())
count = 0
for _ in range(M):
    if input() in contact:
        count += 1
print(count)